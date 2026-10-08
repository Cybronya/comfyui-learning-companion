# TextEncodeQwenImageEdit_lrzjason

## 节点类型

`TextEncodeQwenImageEdit_lrzjason`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `enable_resize:BOOLEAN`（1 次）
- `resolution:COMBO`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `IMAGE:IMAGE`（1 次）
- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Change hair to black", true, 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
