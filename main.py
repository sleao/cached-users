import os
import sys
import csv
import requests

API_URL = 'https://jsonplaceholder.typicode.com/users'
HEADERS = 'mail,website,hemisferio,username'.split(',')

def _hemis(lat):
    if float(lat) > 0: return "norte"
    else: return "sul"

def _save_cache(info):
    with open('cache.csv','a') as f:
        f.write(','.join(info)+'\n')

def _load_cache():
    cache = {}
    try:
        with open('cache.csv','r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                mail, website, hemisferio = (
                    row['mail'],
                    row['website'],
                    row['hemisferio'])

                cache[row['username']] = {
                        'mail':mail,
                        'website':website,
                        'hemisferio':hemisferio
                        }
            return cache


    except FileNotFoundError:
        open('cache.csv','w').write(','.join(HEADERS)+ '\n')
        return


def _call_api(username):
    payload = {'username': username}
    if res := requests.get(API_URL,payload).json():
        user = res[0]
        email, website, hemisferio = (
            user['email'],
            user['website'],
            _hemis(user['address']['geo']['lat']))

        _save_cache([email,website,hemisferio,username])
        return (email,website,hemisferio)

    else: print('Usuário não encontrado na API')

def _get_user(username):
    try:
        user = cache[username]
        return user
    except KeyError:
        return _call_api(username)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        # Seu código entra aqui
        cache = _load_cache()
        res = _get_user(username)
        print(f"User: {username}\nMail: {res['mail']}\n" +
            f"Website: {res['website']}\nHemisferio: {res['hemisferio']}")

    else:
        print("passe um username")
