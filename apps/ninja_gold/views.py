# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

def index(request):

    if 'gold' not in request.session: 
        request.session['gold'] = 0
    if 'list' not in request.session:
        request.session['list'] = []

    return render(request, 'ninja_gold/index.html')

def calculate(request):

    if request.POST['location'] == 'farm':
        gold = random.randint(10,20)
        request.session['gold'] += gold
        cash = {

            'input': "Earned "+str(gold)+"golds from the farm!"+datetime.strftime(datetime.today(), '(%Y/%m/%d %I:%M %p)'),
            'color': 'green'

        }
        request.session['list'].insert(0,cash)

    if request.POST['location'] == 'cave':
        gold = random.randint(5,10)
        request.session['gold'] += gold
        cash = {

            'input': "Earned "+str(gold)+" golds from the cave!"+datetime.strftime(datetime.today(), '(%Y/%m/%d %I:%M %p)'),
            'color': 'green'

        }
        request.session['list'].insert(0,cash)

    if request.POST['location'] == 'house':
        gold = random.randint(2,5)
        request.session['gold'] += gold
        cash = {

            'input': "Earned "+str(gold)+" golds from the house!"+datetime.strftime(datetime.today(), '(%Y/%m/%d %I:%M %p)'),
            'color': 'green'

        }
        request.session['list'].insert(0,cash)

    if request.POST['location'] == 'casino':
        chance = random.randint(0,1)

        if chance == 0:
            gold = random.randint(0,50)
            request.session['gold'] += gold
            cash = {

            'input': "Etered a casino and won "+str(gold)+" golds from the casino!"+datetime.strftime(datetime.today(), '(%Y/%m/%d %I:%M %p)'),
            'color': 'green'

            }
            request.session['list'].insert(0,cash)
        else:
            gold = random.randint(0,50)
            request.session['gold'] -= gold
            if request.session['gold'] <= 0:
                cash = {

                    'input': "Earned a casino and lost all your gold... ouch!"+datetime.strftime(datetime.today(), '(%Y/%m/%d %I:%M %p)'),
                    'color': 'green'
                    
                    }
                request.session['list'].insert(0,cash)

            else:
                cash = {
                    'input': "Entered a casino and  "+str(gold)+" golds from the casino!"+datetime.strftime(datetime.today(), '(%Y/%m/%d %I:%M %p)'),
                    'color': 'red'
                    }

                request.session['list'].insert(0,cash)

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')