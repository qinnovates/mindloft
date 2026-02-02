"""
Neurogenesis Optimization
Bayesian optimization for discovering therapeutic parameters
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

from .parameters import NeurogenesisParameters
from .stem_cell import NeuralStemCell, CellCyclePhase
from .pathology import AlzheimersPathology, FunctionalMetrics

# Optional imports - graceful fallback if not available
try:
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, Matern
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

try:
    from scipy.optimize import differential_evolution
    from scipy.stats import norm
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


class NeurogenesisOptimizer:
    """
    Machine learning optimization loop for discovering neurogenesis triggers
    Combines Bayesian optimization with simulation-based evaluation
    """

    def __init__(self, pathology: AlzheimersPathology):
        """
        Initialize optimizer

        Args:
            pathology: Alzheimer's pathology to attempt to reverse
        """
        self.pathology = pathology
        self.bounds = NeurogenesisParameters.get_bounds()
        self.param_names = NeurogenesisParameters.get_parameter_names()

        # History
        self.X_history: List[np.ndarray] = []
        self.y_history: List[float] = []
        self.best_params: Optional[NeurogenesisParameters] = None
        self.best_score: float = -np.inf

        # Gaussian Process for Bayesian optimization
        if HAS_SKLEARN:
            self.gp = GaussianProcessRegressor(
                kernel=Matern(nu=2.5, length_scale=1.0),
                n_restarts_optimizer=5,
                normalize_y=True,
                random_state=42
            )
        else:
            self.gp = None

    def simulate_intervention(self, params: NeurogenesisParameters,
                              duration_hours: float = 168) -> FunctionalMetrics:
        """
        Run simulation with given parameters and measure functional recovery
        Duration: 168 hours = 1 week (typical neurogenesis timescale)

        Args:
            params: Intervention parameters
            duration_hours: Simulation duration

        Returns:
            Functional recovery metrics
        """
        # Initialize neural stem cell population
        n_nsc = 100
        stem_cells = [
            NeuralStemCell(
                position=np.random.uniform(-500, 500, 3)  # μm, subventricular zone
            ) for _ in range(n_nsc)
        ]

        # Create local copy of pathology for this simulation
        pathology = AlzheimersPathology(
            plaque_density=self.pathology.plaque_density,
            Abeta_oligomer_conc=self.pathology.Abeta_oligomer_conc,
            tau_hyperphosphorylation=self.pathology.tau_hyperphosphorylation,
            microtubule_stability=self.pathology.microtubule_stability,
            synapse_density=self.pathology.synapse_density,
            glucose_hypometabolism=self.pathology.glucose_hypometabolism,
            mitochondrial_dysfunction=self.pathology.mitochondrial_dysfunction
        )

        # Simulation loop
        dt = 0.1  # hours
        t = 0
        new_neurons = 0

        while t < duration_hours:
            # Update pathology (may be modulated by intervention)
            self._update_pathology(pathology, params, dt)

            # Update each stem cell
            new_cells = []
            for cell in stem_cells:
                daughter = cell.update_cell_cycle(params, dt)
                if daughter is not None:
                    new_cells.append(daughter)
                    new_neurons += 1

                # Update differentiation and metabolism
                cell.update_differentiation(params, dt)
                cell.update_metabolism(params, dt)

            stem_cells.extend(new_cells)
            t += dt

        # Compute metrics from final state
        metrics = FunctionalMetrics.from_simulation(stem_cells, params, pathology)

        return metrics

    def _update_pathology(self, pathology: AlzheimersPathology,
                          params: NeurogenesisParameters,
                          dt: float):
        """
        Model how intervention affects pathology progression/reversal

        Args:
            pathology: Pathology state to update
            params: Intervention parameters
            dt: Time step in hours
        """
        # Neurogenesis may help clear amyloid (microglial activation)
        if params.BDNF_concentration > 50e-12:
            pathology.plaque_density *= (1 - 0.001 * dt)
            pathology.Abeta_oligomer_conc *= (1 - 0.001 * dt)

        # Improved metabolism reduces tau phosphorylation
        if params.ATP_ADP_ratio > 15:
            pathology.tau_hyperphosphorylation *= (1 - 0.002 * dt)
            pathology.microtubule_stability = 1 - 0.8 * pathology.tau_hyperphosphorylation

        # Anti-inflammatory effects of theta stimulation
        if 4 < params.theta_frequency < 7:
            pathology.microglial_activation *= (1 - 0.001 * dt)
            pathology.IL1_beta *= (1 - 0.001 * dt)

        # Metabolic improvement
        if params.glucose_concentration > 8:
            pathology.glucose_hypometabolism *= (1 - 0.001 * dt)

    def acquisition_function(self, X: np.ndarray) -> float:
        """
        Expected Improvement acquisition function for Bayesian optimization

        Args:
            X: Parameter vector to evaluate

        Returns:
            Expected improvement value
        """
        if not HAS_SKLEARN or self.gp is None:
            return np.random.random()

        if len(self.X_history) < 5:
            return np.random.random()  # Random exploration initially

        mu, sigma = self.gp.predict(X.reshape(1, -1), return_std=True)
        sigma = sigma[0]
        mu = mu[0]

        if sigma < 1e-10:
            return 0.0

        # Expected improvement
        improvement = mu - self.best_score
        Z = improvement / sigma

        if HAS_SCIPY:
            ei = improvement * norm.cdf(Z) + sigma * norm.pdf(Z)
        else:
            # Simplified EI without scipy
            ei = max(0, improvement)

        return ei

    def _random_sample(self) -> np.ndarray:
        """Generate random sample within bounds"""
        return np.array([
            np.random.uniform(b[0], b[1])
            for b in self.bounds
        ])

    def optimize(self, n_iterations: int = 100,
                 exploration_weight: float = 0.1,
                 verbose: bool = True) -> NeurogenesisParameters:
        """
        Main optimization loop

        Args:
            n_iterations: Number of optimization iterations
            exploration_weight: Weight for exploration noise
            verbose: Print progress

        Returns:
            Best parameters found
        """
        if verbose:
            print("Starting neurogenesis parameter optimization...")
            print(f"Pathology severity: {self.pathology.get_severity_score():.3f}")

        for i in range(n_iterations):
            # Select next parameters to try
            if i < 10 or not HAS_SCIPY or not HAS_SKLEARN:
                # Random initial exploration
                X_next = self._random_sample()
            else:
                # Bayesian optimization
                if len(self.X_history) >= 5:
                    self.gp.fit(np.array(self.X_history), np.array(self.y_history))

                # Optimize acquisition function
                result = differential_evolution(
                    lambda x: -self.acquisition_function(x),
                    bounds=self.bounds,
                    maxiter=50,
                    seed=i,
                    workers=1
                )
                X_next = result.x

            # Add exploration noise
            noise = exploration_weight * np.random.randn(len(X_next))
            ranges = np.array([b[1] - b[0] for b in self.bounds])
            X_next = X_next + noise * ranges * 0.05

            # Clip to bounds
            X_next = np.clip(
                X_next,
                [b[0] for b in self.bounds],
                [b[1] for b in self.bounds]
            )

            # Evaluate
            params = NeurogenesisParameters.from_vector(X_next)
            metrics = self.simulate_intervention(params)
            score = metrics.compute_composite_score()

            # Update history
            self.X_history.append(X_next)
            self.y_history.append(score)

            if score > self.best_score:
                self.best_score = score
                self.best_params = params
                if verbose:
                    print(f"Iteration {i}: New best score = {score:.4f}")

        return self.best_params

    def analyze_parameter_importance(self) -> Dict[str, float]:
        """
        Analyze which parameters most strongly influence recovery

        Returns:
            Dictionary mapping parameter names to correlation with score
        """
        if len(self.X_history) < 20:
            return {}

        X = np.array(self.X_history)
        y = np.array(self.y_history)

        correlations = {}
        for i, name in enumerate(self.param_names):
            corr = np.corrcoef(X[:, i], y)[0, 1]
            if not np.isnan(corr):
                correlations[name] = corr

        return dict(sorted(correlations.items(),
                          key=lambda x: abs(x[1]), reverse=True))

    def get_optimization_summary(self) -> Dict:
        """Get summary of optimization results"""
        return {
            'n_iterations': len(self.X_history),
            'best_score': self.best_score,
            'best_params': self.best_params.to_vector().tolist() if self.best_params else None,
            'parameter_importance': self.analyze_parameter_importance(),
            'score_history': self.y_history
        }


class AlzheimersReversalExperiment:
    """
    Test which pathological feature is most reversible through neurogenesis
    """

    def __init__(self):
        self.pathology_types = [
            'amyloid_plaques',
            'tau_tangles',
            'neuroinflammation',
            'synaptic_loss',
            'metabolic_dysfunction'
        ]

    def create_isolated_pathology(self, pathology_type: str,
                                  severity: float = 0.5) -> AlzheimersPathology:
        """
        Create pathology with only one component elevated

        Args:
            pathology_type: Type of pathology to simulate
            severity: Severity level (0-1)

        Returns:
            Pathology with isolated feature
        """
        pathology = AlzheimersPathology()

        if pathology_type == 'amyloid_plaques':
            pathology.plaque_density = severity * 1000  # plaques/mm³
            pathology.Abeta_oligomer_conc = severity * 5  # nM

        elif pathology_type == 'tau_tangles':
            pathology.tangle_density = severity
            pathology.tau_hyperphosphorylation = severity
            pathology.microtubule_stability = 1 - 0.8 * severity

        elif pathology_type == 'neuroinflammation':
            pathology.microglial_activation = severity
            pathology.IL1_beta = severity * 50  # pg/mL
            pathology.TNF_alpha = severity * 30  # pg/mL

        elif pathology_type == 'synaptic_loss':
            pathology.synapse_density = 1 - severity

        elif pathology_type == 'metabolic_dysfunction':
            pathology.glucose_hypometabolism = severity
            pathology.mitochondrial_dysfunction = severity

        return pathology

    def run_reversal_experiment(self, n_iterations: int = 30,
                                severity: float = 0.7,
                                verbose: bool = True) -> Dict[str, Dict]:
        """
        Test neurogenesis-mediated reversal for each pathology type

        Args:
            n_iterations: Optimization iterations per pathology
            severity: Pathology severity level
            verbose: Print progress

        Returns:
            Results dictionary for each pathology type
        """
        results = {}

        for ptype in self.pathology_types:
            if verbose:
                print(f"\n{'='*60}")
                print(f"Testing reversal of: {ptype}")
                print('='*60)

            # Create isolated pathology
            pathology = self.create_isolated_pathology(ptype, severity=severity)

            # Run optimization
            optimizer = NeurogenesisOptimizer(pathology)
            best_params = optimizer.optimize(n_iterations=n_iterations, verbose=verbose)

            # Measure final recovery
            metrics = optimizer.simulate_intervention(best_params, duration_hours=336)
            recovery_score = metrics.compute_composite_score()

            results[ptype] = {
                'recovery_score': recovery_score,
                'new_neurons': metrics.neuron_count,
                'synaptic_density': metrics.synapse_density,
                'cognitive_score': (metrics.pattern_completion +
                                   metrics.pattern_separation) / 2,
                'best_params': best_params,
                'optimization_history': optimizer.y_history
            }

        return results

    def print_results(self, results: Dict[str, Dict]):
        """Pretty print reversal experiment results"""
        print("\n" + "="*60)
        print("ALZHEIMER'S PATHOLOGY REVERSAL EXPERIMENT RESULTS")
        print("="*60)

        # Sort by recovery score
        sorted_results = sorted(
            results.items(),
            key=lambda x: x[1]['recovery_score'],
            reverse=True
        )

        print("\nRanking by Reversibility:\n")
        for rank, (ptype, data) in enumerate(sorted_results, 1):
            print(f"{rank}. {ptype}:")
            print(f"   Recovery score: {data['recovery_score']:.3f}")
            print(f"   New neurons: {data['new_neurons']:.2f}x baseline")
            print(f"   Synaptic density: {data['synaptic_density']:.2f}")
            print(f"   Cognitive score: {data['cognitive_score']:.3f}")
            print()

        # Summary
        best = sorted_results[0]
        worst = sorted_results[-1]
        print(f"Most reversible: {best[0]} (score: {best[1]['recovery_score']:.3f})")
        print(f"Least reversible: {worst[0]} (score: {worst[1]['recovery_score']:.3f})")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Create moderate AD pathology
    pathology = AlzheimersPathology(
        plaque_density=500,
        Abeta_oligomer_conc=2.0,
        tau_hyperphosphorylation=0.4,
        microtubule_stability=0.7,
        synapse_density=0.6,
        glucose_hypometabolism=0.3
    )

    print("="*60)
    print("NEUROGENESIS PARAMETER OPTIMIZATION")
    print("="*60)
    print(f"Initial pathology severity: {pathology.get_severity_score():.3f}")

    # Run optimization
    optimizer = NeurogenesisOptimizer(pathology)
    optimal_params = optimizer.optimize(n_iterations=50)

    print("\n" + "="*60)
    print("OPTIMAL PARAMETERS DISCOVERED:")
    print("="*60)
    if optimal_params:
        print(f"ATP/ADP ratio: {optimal_params.ATP_ADP_ratio:.2f}")
        print(f"Oxygen saturation: {optimal_params.oxygen_saturation:.2f}")
        print(f"Substrate stiffness: {optimal_params.substrate_stiffness:.0f} Pa")
        print(f"Theta frequency: {optimal_params.theta_frequency:.2f} Hz")
        print(f"BDNF concentration: {optimal_params.BDNF_concentration*1e12:.2f} pM")
        print(f"Wnt activity: {optimal_params.Wnt_activity:.2f}")
        print(f"Temperature: {optimal_params.local_temperature - 273.15:.2f}°C")

    # Parameter importance
    importance = optimizer.analyze_parameter_importance()
    if importance:
        print("\nParameter Importance (top 10):")
        for name, corr in list(importance.items())[:10]:
            print(f"  {name}: {corr:+.3f}")

    # Run reversal experiment
    print("\n" + "="*60)
    print("RUNNING PATHOLOGY REVERSAL EXPERIMENT")
    print("="*60)

    experiment = AlzheimersReversalExperiment()
    results = experiment.run_reversal_experiment(n_iterations=20)
    experiment.print_results(results)
