"""


@date: 2020/4/5 23:27 
@author：Spring
"""

"""
一、Web UI自动化中，定位方式的优先级
优先级最高：ID
优先级其次：name
优先级再次：CSS selector
优先级再次：Xpath

二、选择器
.class	class选择器	.intro	    选择 class="intro" 的所有元素。
#id	    id选择器	#firstname	选择 id="firstname" 的所有元素。
*	    通配符	 	            选择所有元素。
element	标签选择器	p	        选择所有 <p> 元素。

element,element	分组选择器	    div,p	同时选择所有 <div> 元素和所有 <p> 元素。
element element	后端选择器	    div p	选择 <div> 元素内部的所有 <p> 元素（包括子元素、孙子元素）
element>element	子元素选择器	div>p	选择 <div> 元素下的 <p> 子元素。
element+element	相邻选择器	    div+p	选择 <div> 元素之后的所有兄弟 <p> 元素。

[attribute]	        [target]	 	    选择带有 target 属性所有元素。
[attribute=value]	[target=_blank]	 	选择 target="_blank" 的所有元素。
[attribute~=value]	[title~=flower]	 	选择 title 属性包含单词 "flower" 的所有元素。
[attribute|=value]	[lang|=en]	 	    选择 lang 属性值以 "en" 开头的所有元素。


"""