# LTX2STGGuider

## 节点类型

`LTX2STGGuider`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `sigmas:SIGMAS`（1 次）
- `cfg_per_step:STRING`（1 次）
- `stg_scale_per_step:STRING`（1 次）
- `stg_rescale_per_step:STRING`（1 次）
- `cfg_mode:COMBO`（1 次）
- `cfg_min:FLOAT`（1 次）
- `cfg_max:FLOAT`（1 次）

## 输出

- `GUIDER:GUIDER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2.0, 1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0", "1.0, 1.0, 1.0, 0.7, 0, 0, 0.0, 0.0, 0.0", "1.0, 1.0, 1.0, 1.0, 1.0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
