# PiDPrepare

## 节点类型

`PiDPrepare`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `latent:LATENT`（15 次）
- `caption:STRING`（15 次）
- `vae:VAE`（15 次）
- `baseline_image:IMAGE`（15 次）
- `backbone:COMBO`（15 次）
- `pid_ckpt_type:COMBO`（15 次）
- `scale:INT`（15 次）
- `sigma:FLOAT`（15 次）
- `auto_download:BOOLEAN`（15 次）
- `cleanup_after_prepare:BOOLEAN`（15 次）

## 输出

- `prepared:PID_PREP`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["zimage", "2kto4k", 4, 0, true, true, ""]`（6 次）
- `["zimage", "2kto4k", 4, 0, false, true, ""]`（3 次）
- `["zimage", "2kto4k", 4, 0.30000000000000004, false, true, ""]`（2 次）
- `["flux", "2kto4k", 4, 0, true, true, ""]`（1 次）
- `["flux2", "2kto4k", 4, 0, true, true, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
