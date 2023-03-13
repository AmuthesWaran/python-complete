# LIFO - Last In - First Out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("Redirect", browsing_session[-1])
browsing_session.pop()
browsing_session.pop()
if not browsing_session:
    print("Disabled")
