# Django代码规范

## Python 风格
- 除非另有规定，否则请遵循 PEP 8 风格指南。 
你可以使用类似 pep8 的工具检查你的代码， 但是，请记住 PEP 8 只是个指南，并非强制约束，因此应当以你所处项目/团队的风格为主。 
一个比较大的例外就是，PEP 8 规定代码行长最长不能超过 79 个字符。问题是现在是 21 世纪了，我们有高分辨率的显示器可以显示超过 79 个字符的代码行。如果这这个约定让代码看起来很丑或难以阅读的话，那么就没必要限制行长不超过 79 个字符。

- 使用4个空格进行缩进。注意设置不要混入`tab`了

- 使用下划线而不是小驼峰法（camelCase）命名变量、函数及方法名（比如，poll.get_unique_voters()，不要使用 poll.getUniqueVoters）。

	```python
	def render_to_response():
	```

- 使用首字母大写（InitialCaps）的方式命名类名。

	```python
	class HttpResponse(HttpResponseBase):
	```

- 文档字符串中，使用动词（action words）。比如：

	```python
	def foo():
	    """
	    Calculates something and returns the result.
	    """
	    pass
	```

	反例：
	
	```python
	def foo():
	    """
	    Calculate something and return the result.
	    """
	    pass
	```
	我们写中文就可以了^_^
	
- 单双引号问题，一般变量可以使用单引号，写文档用双引号
- 使用中文，加上文件头，为了兼容性，使用中文时使用unicode

	```python
	#coding=utf-8
	
	hello = u'你好'
	```

	
## 模板风格
- 在模板中，大括号及标签内容之间使用一个（只需一个）空格。 
	应该这样：
	
	```html
	{{ foo }}
	```
	
	别这样：
	
	```
	{{foo}}
	```

## 视图风格
- 在视图中，视图函数的第一个参数应该被命名为 request。 
	应该这样：
	
	```python
	def my_view(request, foo):
	    # ...
	```
	
	别这样：
	
	```python
	def my_view(req, foo):
	    # ...
	```    

## 模型风格
- 字段名应该全部小写，使用下划线代替小驼峰法。 应该这样：

	```python
	class Person(models.Model):
	    first_name = models.CharField(max_length=20)
	    last_name = models.CharField(max_length=40)
	```
	别这样：
	
	```python
	class Person(models.Model):
	    FirstName = models.CharField(max_length=20)
	    Last_Name = models.CharField(max_length=40)
	```    
    
- `class Meta` 应该在字段被定义后才出现，使用一个空行分隔。 应该这样：

	```python
	class Person(models.Model):
	    first_name = models.CharField(max_length=20)
	    last_name = models.CharField(max_length=40)
	
	    class Meta:
	        verbose_name_plural = 'people'
	```        
	        
	别这样：
	
	```python
	class Person(models.Model):
	    first_name = models.CharField(max_length=20)
	    last_name = models.CharField(max_length=40)
	    class Meta:
	        verbose_name_plural = 'people'
	```        
	        
	也别这样：
	
	
	```python
	class Person(models.Model):
	    class Meta:
	        verbose_name_plural = 'people'
	
	    first_name = models.CharField(max_length=20)
	    last_name = models.CharField(max_length=40)
	```    
    
- model 内的类和方法的定义顺序应该遵循如下顺序（不是所有项都是必需的）：

	1. 所有的数据库字段
	2. 自定义管理器属性（manager attributes）
	3. `class Meta`
	4. `def __unicode__()`
	5. `def __str__()`
	6. `def save()`
	7. `def get_absolute_url()`
	8. 其他自定义方法

- 如果一个 model 字段定义了 `choices`，那么定义的多元元组的名称应该全部大写。例如：

	```python
	class MyModel(models.Model):
	    DIRECTION_UP = 'U'
	    DIRECTION_DOWN = 'D'
	    DIRECTION_CHOICES = (
	        (DIRECTION_UP, 'Up'),
	        (DIRECTION_DOWN, 'Down'),
	    )
	```    