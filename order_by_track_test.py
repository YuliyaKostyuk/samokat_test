#Юлия Костюк, 11 когорта, - Финальный проект QA
import sender_stand_request


def positive_assert(track):
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200


def test_order_by_track_get_success_response():
    track = sender_stand_request.get_track()
    positive_assert(track)