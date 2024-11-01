def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
# inner_function() Ошибка из-за вызова функции вне пределов ее видимости
