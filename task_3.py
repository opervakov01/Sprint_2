class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return points
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return points
        else:
            points = 101 - place
            return points



class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return points
        else:
            points = meters * 0.5
            return points

