from django.http import HttpResponse
from django.shortcuts import render

#Home page using html as a function
def indexh(request):
    return render(request, 'index.html')

#another page after work of text function
def text(request):
    #get the text
    analyze_txt = request.POST.get('analyze_txt','default')
    
    # check checkBox value
    remove_punctuation = request.POST.get('check_on', 'off')
    fullcaps = request.POST.get('CAPATILIZE', 'off')
    remove_newLine = request.POST.get('remove_newLine', 'off')
    extra_space = request.POST.get('extra_space', 'off')
    character_counter = request.POST.get('character_counter', 'off')
    
    
    #check which check box is on
    
    #remove_punctuation check box's function
    if(remove_punctuation == 'on'):
        Analyzed = ""
        punctuations = '''!@#$%^&*()_-+=:;|\[]{}"'?/>.<,`~'''
        
        for char in analyze_txt:
            if char not in punctuations:
                Analyzed = Analyzed + char
                
        parameters = {"purpose":"Text Manuplator","analyzed_text":Analyzed}
        analyze_txt = Analyzed
                
    #fullcaps check box's function
    if(fullcaps == 'on'):
        Analyzed = ""
        
        for char in analyze_txt:
            Analyzed += char.upper()
            
        parameters = {"purpose":"Text Manuplator","analyzed_text":Analyzed}
        analyze_txt = Analyzed
            
    #remove_newLine check box's function
    if(remove_newLine == "on"):
        Analyzed = ""
        for char in analyze_txt:
            if char != '\n' and char != '\r':
                Analyzed += char 
        parameters = {"purpose":"Text Manuplator","analyzed_text":Analyzed} 
        analyze_txt = Analyzed
                
    #extra_space check box's function
    if(extra_space == "on"):
        Analyzed = ""
        for index, char in enumerate(analyze_txt):
            if  not((analyze_txt[index] == " ") and (analyze_txt[index+1] == " ")):
                Analyzed += char
        parameters = {"purpose":"Text Manuplator","analyzed_text":Analyzed}
        analyze_txt = Analyzed
                
    #character_counter check box's function            
    if(character_counter == 'on'):
        count = 0
        for char in analyze_txt:
            count+=1
            
        parameters = {"purpose":"Text Manuplator","analyzed_text":Analyzed}
        Analyzed = (f'The String is (-{analyze_txt}-) and In this string there are total {count} characters.')
        
            
    if(remove_punctuation != 'on' and fullcaps != 'on' and remove_newLine != "on" and extra_space != 'on' and character_counter != 'on'):
        return HttpResponse("Error!!! - Please select any operation.")

    
    #defied parameters using dictionary
    
    
    return render(request, 'analyze.html', parameters)

    
    