# CLIPTextEncode (NSP)

## 节点类型

`CLIPTextEncode (NSP)`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）

## 输出

- `conditioning:CONDITIONING`（2 次）
- `parsed_text:STRING`（2 次）
- `raw_text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Noodle Soup Prompts", "__", 700511043270646, "randomize", "milk cup"]`（1 次）
- `["Noodle Soup Prompts", "__", 580973521320442, "randomize", "The white kitten is resting in the flowers"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
