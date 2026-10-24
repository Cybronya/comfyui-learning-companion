# CLIPTextEncodeWithWeight //Inspire

## 节点类型

`CLIPTextEncodeWithWeight //Inspire`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `clip:CLIP`（10 次）
- `text:STRING`（4 次）
- `strength:FLOAT`（2 次）
- `add_weight:FLOAT`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["grungy, cluttered, disorganized, noisy, blurry, amateurish, sloppy, unattractive, cheap", 1, 0]`（4 次）
- `["", 1, 0]`（3 次）
- `["corporate branding style, clean, modern, sleek, minimalist, business-oriented, retail packaging style, vibrant, entici`（2 次）
- `["\n\n", 1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
