#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 01:35:51 2019

@author: paawansharma
"""

def dec_to_rom(number):
    
    """
    Takes in an integer and outputs a string representing it in Roman numerals
    For values greater than 4999, parentheses represent multiplication by 1000
    e.g., (V) means 5000
    """
    
    if type(number) != int:
        raise TypeError
    
    main_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC",
                    50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    output = ""
    
    if number >= 5000:
        
        thousands = int(number / 1000)
        thousands_r = dec_to_rom(thousands)
        remain_after_thousands = number - thousands * 1000
        remain_after_thousands_r = dec_to_rom(remain_after_thousands)
        
        while thousands_r[-1] == "I":
            thousands -= 1
            thousands_r = dec_to_rom(thousands)
            remain_after_thousands = number - thousands * 1000
            remain_after_thousands_r = dec_to_rom(remain_after_thousands)
            
        try:
            while thousands_r[-1] == "V" and thousands_r[-2] == "I":
                thousands -= 4
                thousands_r = dec_to_rom(thousands)
                remain_after_thousands += 4000
                remain_after_thousands_r = dec_to_rom(remain_after_thousands)
                
        except IndexError:
            pass
        
        return "".join(["(", thousands_r, ")", remain_after_thousands_r])
    
    while number > 0:
        for i in range(len(symbols)):
            while number >= main_values[i]:
                number -= main_values[i]
                output += symbols[main_values[i]]
            
    return output


def rom_to_dec(roman):
    
    roman_2 = roman.upper()
    symbols = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    i = 0 # need to rename this
    states = []
    output = 0
    
    brackets = roman_2.count("(")
    while brackets:
        if roman_2 == "()":
            roman_2 = ""
            break
            
        opening_bracket = roman_2.rindex("(")
        closing_bracket = roman_2.index(")")
        bracketed = roman_2[opening_bracket+1:closing_bracket]
        roman_2 = roman_2[:opening_bracket] + roman_2[closing_bracket+1:]
        output += rom_to_dec(bracketed) * 1000 ** brackets
        brackets -= 1
        
    while i < len(roman_2):
        if i != len(roman_2) - 1:
            a = symbols[roman_2[i]] # rename a
            b = symbols[roman_2[i+1]] # rename b
            
            if a >= b:
                states.append(1)
                
            else:
                states.append(0)
                
        i += 1
        
    if roman_2:
        output += symbols[roman_2[-1]]
        
    for place in range(len(states)):
        if states[place]:
            output += symbols[roman_2[place]]
        else:
            output -= symbols[roman_2[place]]
            
    if dec_to_rom(output) == roman.upper():
        return output
    
    else:
        print("%s is not a Roman number. %d is represented by %s." % (roman, output, dec_to_rom(output)))
        return output