def constructWord(input_word, word_list):
    current = []
    def backstrack(start):
        if start==len(input_word):
            result.append(list(current))
            # print(result)
            return
        for word in word_list:
            if input_word.startswith(word, start):
                current.append(word)
                backstrack(start+len(word))
                current.pop()
    result = []
    backstrack(0)
    print(result)
    return result
constructWord('apple', ['ap', 'pple', 'app', 'apl', 'appl', 'le', 'ple'])

            
    
            