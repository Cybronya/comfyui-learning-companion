# LTXVImgToVideoConditionOnly

## 节点类型

`LTXVImgToVideoConditionOnly`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `vae:VAE`（11 次）
- `image:IMAGE`（11 次）
- `latent:LATENT`（11 次）
- `strength:FLOAT`（11 次）
- `bypass:BOOLEAN`（11 次）

## 输出

- `latent:LATENT`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, false]`（8 次）
- `[0.7, false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
