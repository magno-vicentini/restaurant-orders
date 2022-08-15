class TrackOrders:

    def __init__(self):
        self.requests_list = list()

    def __len__(self):
        return len(self.requests_list)

    def add_new_order(self, customer, order, day):
        return self.requests_list.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        requests_by_customer = list()
        foods_by_customer = dict()
        for info in self.requests_list:
            if info[0] == customer:
                requests_by_customer.append(info[1])
        for food in requests_by_customer:
            if food in foods_by_customer:
                foods_by_customer[food] += 1
            else:
                foods_by_customer[food] = 1
        most_request = max(
            foods_by_customer, key=lambda f: foods_by_customer[f]
            )
        return most_request

    def get_never_ordered_per_customer(self, customer):
        orders_foods = set()
        customer_orders = set()
        for info in self.requests_list:
            orders_foods.add(info[1])
            if info[0] == customer:
                customer_orders.add(info[1])
        return orders_foods.symmetric_difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        all_days = set()
        customer_days = set()
        for info in self.requests_list:
            all_days.add(info[2])
            if info[0] == customer:
                customer_days.add(info[2])
        return all_days.symmetric_difference(customer_days)

    def get_busiest_day(self):
        all_days = list()
        count_days = dict()
        for info in self.requests_list:
            all_days.append(info[2])
        for day in all_days:
            if day in count_days:
                count_days[day] += 1
            else:
                count_days[day] = 1
        most_visited = max(count_days, key=lambda f: count_days[f])
        return most_visited

    def get_least_busy_day(self):
        all_days = list()
        count_days = dict()
        for info in self.requests_list:
            all_days.append(info[2])
        for day in all_days:
            if day in count_days:
                count_days[day] += 1
            else:
                count_days[day] = 1
        less_visited = min(count_days, key=lambda f: count_days[f])
        return less_visited
