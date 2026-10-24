# WildcardEncode //Inspire

## 节点类型

`WildcardEncode //Inspire`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `seed:INT`（1 次）

## 输出

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `populated_text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", "A1111", "", "", false, "Select the LoRA to add to the text", "Select the Wildcard to add to the text", 4187081`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
