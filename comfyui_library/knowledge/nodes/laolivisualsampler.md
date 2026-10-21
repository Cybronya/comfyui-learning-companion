# LaoliVisualSampler

## 节点类型

`LaoliVisualSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型_1:MODEL`（1 次）
- `正面_1:CONDITIONING`（1 次）
- `负面_1:CONDITIONING`（1 次）
- `Latent:LATENT`（1 次）
- `VAE_1:VAE`（1 次）
- `模型_2:MODEL`（1 次）
- `正面_2:CONDITIONING`（1 次）
- `负面_2:CONDITIONING`（1 次）
- `VAE_2:VAE`（1 次）
- `放大模型:UPSCALE_MODEL`（1 次）

## 输出

- `一阶预览:IMAGE`（1 次）
- `最终图像:IMAGE`（1 次）
- `分块解码:IMAGE`（1 次）
- `终Latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["当前设置", 824603180991545, 30, 3, "res_multistep", "simple", 1, "enable", 0, 30, "disable", "[1.0000, 0.9888, 0.9770, 0.9`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
