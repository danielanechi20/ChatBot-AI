from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckReturnPolicy(Action):

    def name(self) -> Text:
        return "action_check_return_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        days = next(tracker.get_latest_entity_values("days"), None)
        allowed_days = 30  # Define your return policy here

        if days:
            days = int(days)
            if days <= allowed_days:
                response = f"Yes, you can return items within {days} days."
            else:
                response = f"Sorry, items can only be returned within {allowed_days} days."
        else:
            response = "Could you specify the number of days?"

        dispatcher.utter_message(text=response)
        return []




class ActionRecommendOutfit(Action):

    def name(self) -> Text:
        return "action_recommend_outfit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the user message
        user_message = tracker.latest_message.get('text', '').lower()

        # Define recommendations based on occasion
        outfit_recommendations = {
            "wedding": "For a wedding, I recommend a chic cocktail dress or a tailored suit. Pair it with elegant heels or formal shoes.",
            "beach party": "For a beach party, try a flowy sundress or shorts with a breezy linen shirt. Don’t forget sandals!",
            "business meeting": "A business meeting calls for a crisp blazer, a button-up shirt, and tailored trousers or a pencil skirt.",
            "casual weekend": "For a casual weekend look, go for jeans and a comfy t-shirt or a relaxed-fit dress with sneakers.",
            "date night": "For a date night, a little black dress or a stylish shirt with chinos is a great choice."
        }

        # Default response if no occasion matches
        default_response = "I'm not sure what to recommend for that occasion. Can you provide more details?"

        # Match the occasion in the user message
        recommended_outfit = None
        for occasion, recommendation in outfit_recommendations.items():
            if occasion in user_message:
                recommended_outfit = recommendation
                break

        # Respond with the recommendation or the default response
        if recommended_outfit:
            dispatcher.utter_message(text=recommended_outfit)
        else:
            dispatcher.utter_message(text=default_response)

        return []
