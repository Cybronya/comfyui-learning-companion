# MiniMaxH3FunControlApplyT8Advanced

## 节点类型

`MiniMaxH3FunControlApplyT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `control_net:H3_T8_FUN_CONTROL`（2 次）
- `vae:VAE`（2 次）
- `control_video:IMAGE`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `length:INT`（2 次）
- `control_kind:COMBO`（2 次）
- `fit_mode:COMBO`（2 次）

## 输出

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1344, 768, 124, "pose", "exact", 1, 0, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
