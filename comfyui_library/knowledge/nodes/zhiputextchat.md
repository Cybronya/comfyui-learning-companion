# ZhipuTextChat

## 节点类型

`ZhipuTextChat`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `zhipu_client:ZHIPU_CLIENT`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `max_tokens:INT`（1 次）
- `seed:INT`（1 次）
- `system_prompt:STRING`（1 次）

## 输出

- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["（特写肖像，一位美丽的东亚中国女性：1.2），（完美无瑕的陶瓷肌，极致光滑的皮肤纹理，气垫粉底效果：1.5），无皮肤瑕疵，无毛孔，无痤疮，无疤痕，肤色均匀，柔和的自然光，专业摄影，超真实，8K。", "glm-4.5-flash", 0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
