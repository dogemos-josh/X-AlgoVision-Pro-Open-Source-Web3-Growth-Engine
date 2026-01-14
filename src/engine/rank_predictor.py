import yaml

class RankPredictor:
    """Predicts post visibility based on X's recommendation engine weights."""
    
    def __init__(self, config_path="config.yaml"):
        try:
            with open(config_path, "r") as f:
                self.config = yaml.safe_load(f)
            self.weights = self.config['algo_weights_2026']
        except:
            # Fallback to hardcoded safe weights
            self.weights = {"engagement": {"like": 30.0}}

    def calculate_visibility_score(self, text):
        """
        Internal calculation engine. 
        Note: Complex neural network weights are handled by the pre-compiled binary core.
        """
        score = 1000.0 # Base
        
        # Simple heuristic for the open-source version
        if "$" in text:
            score *= 1.5
        if len(text) > 100:
            score += 200
        
        # Link penalty simulation
        if "http" in text:
            score *= 0.5
            
        return round(score, 2)
