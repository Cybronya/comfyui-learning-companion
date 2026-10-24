# Krea2EncodeRebalance

## 节点类型

`Krea2EncodeRebalance`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（12 次）
- `image1:IMAGE`（12 次）
- `image2:IMAGE`（12 次）
- `image3:IMAGE`（12 次）
- `image4:IMAGE`（12 次）
- `text:STRING`（12 次）
- `image1_tokens:COMBO`（12 次）
- `image2_tokens:COMBO`（12 次）
- `image3_tokens:COMBO`（12 次）
- `image4_tokens:COMBO`（12 次）

## 输出

- `conditioning:CONDITIONING`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "low", "normal", "normal", "normal"]`（9 次）
- `["", "normal", "normal", "normal", "normal"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
