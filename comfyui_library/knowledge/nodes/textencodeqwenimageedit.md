# TextEncodeQwenImageEdit

## 节点类型

`TextEncodeQwenImageEdit`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `clip:CLIP`（4 次）
- `vae:VAE`（4 次）
- `image:IMAGE`（4 次）
- `prompt:STRING`（4 次）

## 输出

- `CONDITIONING:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
