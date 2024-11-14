def test_function():
    def test_function():
        print('Я в области видимости функции test_function')
    inner_function() # ничего не возвращает
inner_function()  ## Не работает! (ошибка)
test_function()