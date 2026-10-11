# ComfyUILTX25MSRMultiReferenceGuide

## 节点类型

`ComfyUILTX25MSRMultiReferenceGuide`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `latent:LATENT`（2 次）
- `pic1:IMAGE`（2 次）
- `pic2:IMAGE`（2 次）
- `pic3:IMAGE`（2 次）
- `pic4:IMAGE`（2 次）
- `background:IMAGE`（2 次）
- `msr_parameters:LTX_MSR_REFERENCE_PARAMETERS`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.7000000000000002, "33", false, 256, 64]`（1 次）
- `[0.7000000000000002, "33", false, 256, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
