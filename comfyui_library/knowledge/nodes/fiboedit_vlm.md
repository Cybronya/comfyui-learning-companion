# FiboEdit_VLM

## 节点类型

`FiboEdit_VLM`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `quantization:COMBO`（4 次）
- `temperature:FLOAT`（4 次）
- `top_p:FLOAT`（4 次）
- `max_new_tokens:INT`（4 次）
- `seed:INT`（4 次）
- `keep_model_loaded:BOOLEAN`（4 次）
- `prompt:STRING`（4 次）
- `json_prompt:STRING`（4 次）

## 输出

- `STRING:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", 0.2, 0.9, 4096, 1318, "randomize", false, "加一顶帽子", ""]`（1 次）
- `["none", 0.2, 0.9, 4096, 1746, "randomize", false, "将衣服变成黑色礼服", ""]`（1 次）
- `["none", 0.2, 0.9, 4096, 1346, "randomize", false, "加一顶帽子，衣服变成红色，头发变成金色", ""]`（1 次）
- `["none", 0.2, 0.9, 4096, 689, "randomize", false, "加一顶帽子", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
