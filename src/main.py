import flet as ft
from engine.rank_predictor import RankPredictor
from engine.web3_monitor import Web3AlphaMonitor

def main(page: ft.Page):
    page.title = "X-AlgoVision Pro | Web3 Growth Engine"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 900
    page.window_height = 700
    page.padding = 30

    predictor = RankPredictor()
    monitor = Web3AlphaMonitor()

    # Simple Header
    header = ft.Column([
        ft.Text("X-AlgoVision Pro", size=32, weight="bold", color="blueviolet"),
        ft.Text("Ready for Algorithm Sync (T-minus 5 days)", size=14, color="grey")
    ])

    # Input Section
    input_field = ft.TextField(
        label="Post Draft",
        hint_text="Type your post or thread hook here...",
        multiline=True,
        min_lines=6,
        border_color="blueviolet"
    )

    result_text = ft.Text(size=24, weight="bold")

    def analyze_click(e):
        score = predictor.calculate_visibility_score(input_field.value)
        result_text.value = f"Estimated Visibility Score: {score} pts"
        result_text.color = "green" if score > 1500 else "orange"
        page.update()

    page.add(
        header,
        ft.Divider(height=20, color="transparent"),
        input_field,
        ft.ElevatedButton("Run Algorithmic Analysis", on_click=analyze_click, icon=ft.icons.ANALYTICS),
        ft.Divider(height=20),
        result_text,
        ft.Text("Trending Web3 Boosts: $SOL, $ETH, Airdrop, AI-Agents", italic=True, color="grey")
    )

if __name__ == "__main__":
    ft.app(target=main)
