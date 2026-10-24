# ChatGLM4TranslateTextNode

## 节点类型

`ChatGLM4TranslateTextNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `from_translate:COMBO`（10 次）
- `to_translate:COMBO`（10 次）
- `model:COMBO`（10 次）
- `max_tokens:INT`（10 次）
- `temperature:FLOAT`（10 次）
- `top_p:FLOAT`（10 次）
- `text:STRING`（10 次）

## 输出

- `text:STRING`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ru", "en", "glm-4-flash", 1024, 0.95, 0.7, ""]`（4 次）
- `["ru", "en", "glm-4-flash", 1024, 0.95, 0.7, "hand"]`（2 次）
- `["ru", "en", "glm-4-flash", 1024, 0.95, 0.7, "this is an image of man char15,char15 wearing brown hanfu,"]`（2 次）
- `["ru", "en", "glm-4-flash", 1024, 0.95, 0.7, "将两张图融合，让左图的女子戴上右图的粉色耳机，女子表情惊讶，拿起了宝剑"]`（1 次）
- `["ru", "en", "glm-4-flash", 1024, 0.95, 0.7, "两人侧身面对面，深情对望，\n"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
