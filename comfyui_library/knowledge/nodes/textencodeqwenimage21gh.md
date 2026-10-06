# TextEncodeQwenImage21GH

## 节点类型

`TextEncodeQwenImage21GH`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 17 个 workflow 中。

## 输入

- `clip:CLIP`（17 次）
- `vae:VAE`（17 次）
- `mask:MASK`（17 次）
- `image_01:IMAGE`（17 次）
- `image_02:IMAGE`（17 次）
- `image_03:IMAGE`（17 次）
- `image_04:IMAGE`（17 次）
- `image_05:IMAGE`（17 次）
- `image_06:IMAGE`（17 次）
- `image_07:IMAGE`（17 次）

## 输出

- `positive:CONDITIONING`（17 次）
- `negative:CONDITIONING`（17 次）
- `latent:LATENT`（17 次）
- `info:QWEN_IMAGE_21_GH_RESTORE_INFO`（17 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 1024, 1024, "填充", "自动"]`（17 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
