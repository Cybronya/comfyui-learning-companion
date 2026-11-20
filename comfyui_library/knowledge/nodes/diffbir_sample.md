# DiffBIR_sample

## 节点类型

`DiffBIR_sample`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `stage1_model:STAGE1`（2 次）
- `cldm:CLDM`（2 次）
- `diffusion:DIFFUSION`（2 次）
- `infer_type:INFER_TYPE`（2 次）
- `image:IMAGE`（2 次）
- `upscale_ratio:FLOAT`（1 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 20, 4, true, true, 512, 480, "young woman, fashion model, hand rest on chin, earrings, ring, best quality, hdr, 4k",`（1 次）
- `[2, 20, 4, true, true, 512, 256, "best quality,4k,hdr", "blurry,low quality,", 603628655585256, "randomize", "cuda"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
