# workflow>TTP-工作区域

## 节点类型

`workflow>TTP-工作区域`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `参考图像:IMAGE`（1 次）
- `模型:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `BasicGuider model:MODEL`（1 次）
- `clip_name1:COMBO`（1 次）
- `clip_name2:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `sampler_name:COMBO`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `降噪输出:LATENT`（1 次）
- `RECONSTRUCTED_IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default", "euler", 316430325547060, "fixed", "4x_NMKD-Si`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
