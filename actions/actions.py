from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore
from spotipy import Spotify # type: ignore
import os

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_greet")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_goodbye")
        return []

class ActionAffirm(Action):
    def name(self) -> Text:
        return "action_affirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_affirm")
        return []

class ActionDeny(Action):
    def name(self) -> Text:
        return "action_deny"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_deny")
        return []

class ActionHappy(Action):
    def name(self) -> Text:
        return "action_happy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_happy")
        return []

class ActionCheerUp(Action):
    def name(self) -> Text:
        return "action_cheer_up"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cheer_up")
        return []

class ActionDidThatHelp(Action):
    def name(self) -> Text:
        return "action_did_that_help"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_did_that_help")
        return []

class ActionBookRecommendation(Action):
    def name(self) -> Text:
        return "action_book_recommendation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_book_recommendation")
        return []

class ActionBookDetails(Action):
    def name(self) -> Text:
        return "action_book_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_book_details")
        return []

class ActionFeedbackReceived(Action):
    def name(self) -> Text:
        return "action_feedback_received"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_feedback_received")
        return []

class ActionLatestBookReleases(Action):
    def name(self) -> Text:
        return "action_latest_book_releases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_latest_book_releases")
        return []

class ActionPopularAuthors(Action):
    def name(self) -> Text:
        return "action_popular_authors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_popular_authors")
        return []

class ActionSearchBook(Action):
    def name(self) -> Text:
        return "action_search_book"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_search_book")
        return []

class ActionWeatherInfo(Action):
    def name(self) -> Text:
        return "action_weather_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_weather_info")
        return []

class ActionBuilderInfo(Action):
    def name(self) -> Text:
        return "action_builder_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_builder_info")
        return []

class ActionRestaurantInfo(Action):
    def name(self) -> Text:
        return "action_restaurant_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_restaurant_info")
        return []

class ActionInsultResponse(Action):
    def name(self) -> Text:
        return "action_insult_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_insult_response")
        return []

class ActionJoke(Action):
    def name(self) -> Text:
        return "action_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_joke")
        return []

class ActionWhereFrom(Action):
    def name(self) -> Text:
        return "action_wherefrom"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_wherefrom")
        return []

class ActionHowOld(Action):
    def name(self) -> Text:
        return "action_howold"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_howold")
        return []

class ActionWhoAmI(Action):
    def name(self) -> Text:
        return "action_whoami"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_whoami")
        return []

class ActionLanguages(Action):
    def name(self) -> Text:
        return "action_languages"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_languages")
        return []

class ActionWhatIsMyName(Action):
    def name(self) -> Text:
        return "action_whatismyname"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_whatismyname")
        return []

class ActionSongRecommendation(Action):

    def name(self) -> Text:
        return "action_song_recommendation"

class ActionGiveDetails(Action):
    def name(self) -> Text:
        return "action_give_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Fetch the value of the book or author slot from the tracker
        book = tracker.get_slot("book")
        author = tracker.get_slot("author")
        
        if book:
            # Provide details about the book
            #details = fetch_book_details(book)
            details = "The book details"
            dispatcher.utter_message(text=details)
        elif author:
            # Provide details about the author
            details = "The author details"
            #details = fetch_author_details(author)
            dispatcher.utter_message(text=details)
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't find any details.")

        return []

class ActionLatestBookReleases(Action):
    def name(self) -> Text:
        return "action_latest_book_releases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Fetch latest book releases from your data source
        book_releases = ["Book 1", "Book 2", "Book 3"]  # Example data
        dispatcher.utter_message(template="utter_latest_book_releases", book_releases=book_releases)
        return []

class ActionPopularAuthors(Action):
    def name(self) -> Text:
        return "action_popular_authors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Fetch popular authors from your data source
        popular_authors = ["Author 1", "Author 2", "Author 3"]  # Example data
        dispatcher.utter_message(template="utter_popular_authors", popular_authors=popular_authors)
        return []    

class ActionSearchBook(Action):
    def name(self) -> Text:
        return "action_search_book"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Implement your logic to search for books here
        dispatcher.utter_message(template="utter_Search_book")
        return []
