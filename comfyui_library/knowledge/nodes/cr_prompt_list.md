# CR Prompt List

## 节点类型

`CR Prompt List`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `prepend_text:STRING`（5 次）
- `multiline_text:STRING`（5 次）
- `append_text:STRING`（5 次）
- `start_index:INT`（5 次）
- `max_rows:INT`（5 次）

## 输出

- `prompt:STRING`（5 次）
- `body_text:STRING`（5 次）
- `show_help:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "一张超写实的特写肖像，描绘了一位面对风暴的年迈渔夫。雨滴划过他饱经风霜的脸庞，积聚在诉说着海洋故事的深深皱纹里。他穿着一件质感鲜明的亮黄色雨衣，与背景中动荡海洋的深沉忧郁的蓝色和灰色形成对比。他的眼神锐利如钢，反射出一生的坚韧。`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
