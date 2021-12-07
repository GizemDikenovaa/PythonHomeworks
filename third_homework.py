import datetime


class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def show_info(self):
        print("""Platform: {} \nOptin: {} \nGlobal Frequency Capping: {} \nStart Date:{} \nEnd Date:{} \nLanguage:{} 
        \nPush Type:{}"""
              .format(self.platform, self.optin, self.global_frequency_capping, self.start_date, self.end_date,
                      self.language, self.push_type))

    def send_push(self):
        return print("Push sent \n")


class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page

    def show_info(self):
        print("""Platform: {} \nOptin: {} \nGlobal Frequency Capping: {} \nStart Date:{} \nEnd Date:{} \nLanguage:{} 
        \nPush Type:{} \nTrigger Page:{}"""
              .format(self.platform, self.optin, self.global_frequency_capping, self.start_date, self.end_date,
                      self.language, self.push_type, self.trigger_page))


class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date

    def show_info(self):
        print("""Platform: {} \nOptin: {} \nGlobal Frequency Capping: {} \nStart Date:{} \nEnd Date:{} \nLanguage:{} 
         \nPush Type:{} \nSend Date:{}""".format(self.platform, self.optin, self.global_frequency_capping,
                                                 self.start_date, self.end_date, self.language, self.push_type,
                                                 self.send_date))


class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

    def show_info(self):
        print("""Platform: {} \nOptin: {} \nGlobal Frequency Capping: {} \nStart Date:{} \nEnd Date:{} \nLanguage:{} 
        \nPush Type:{} \nSegment Name:{}"""
              .format(self.platform, self.optin, self.global_frequency_capping, self.start_date, self.end_date,
                      self.language, self.push_type, self.segment_name))


class PriceAlertPush(WebPush):

    def discount_price(self, price_info, discount_rate):
        return price_info - (price_info * (discount_rate / 100))


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def show_info(self):
        print("""Platform: {} \nOptin: {} \nGlobal Frequency Capping: {} \nStart Date:{} \nEnd Date:{} \nLanguage:{} 
        \nPush Type:{} \nStock info:{}""".format(self.platform, self.optin, self.global_frequency_capping,
                                                 self.start_date, self.end_date, self.language, self.push_type,
                                                 self.stock_info))

    def stock_update(self):
        if self.stock_info == True:
            return not self.stock_info


p1 = TriggerPush("Mobile", True, 1, datetime.datetime.now(), datetime.datetime.now(), "English", "Trigger", "Cartpage")
p1.show_info()
p1.send_push()

p2 = BulkPush("Mobile", True, 3, datetime.datetime.now(), datetime.datetime.now(), "English", "Bulk",
              datetime.datetime.now())
p2.show_info()
p2.send_push()

p3 = SegmentPush("Mobile", True, 2, datetime.datetime.now(), datetime.datetime.now(), "English", "Segment", "City")
p3.show_info()
p3.send_push()

p4 = PriceAlertPush("Mobile", True, 4, datetime.datetime.now(), datetime.datetime.now(), "English", "Price Alert")
p4.show_info()
new_price = p4.discount_price(50, 45)
print(new_price)
p4.send_push()

p5 = InstockPush("Mobile", True, 6, datetime.datetime.now(), datetime.datetime.now(), "English", "Instock", True)
p5.show_info()
print(p5.stock_update())
