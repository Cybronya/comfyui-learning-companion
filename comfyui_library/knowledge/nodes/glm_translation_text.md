# GLM_Translation_Text

## 节点类型

`GLM_Translation_Text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text_input:STRING`（2 次）
- `from_language:COMBO`（2 次）
- `to_language:COMBO`（2 次）
- `api_key:STRING`（2 次）
- `model_name:STRING`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `max_tokens:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `translated_text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你好，世界！", "zh", "en", "4bdd550b5af04cadadd24ca88e4fc336.WvodCetE1kVWYdv9", "glm-4-flash-250414", 0.1, 0.7, 1024, 983447`（1 次）
- `["你好，世界！", "zh", "en", "4bdd550b5af04cadadd24ca88e4fc336.WvodCetE1kVWYdv9", "glm-4-flash-250414", 0.1, 0.7, 1024, 186164`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
