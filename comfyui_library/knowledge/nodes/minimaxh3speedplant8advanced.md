# MiniMaxH3SPEEDPlanT8Advanced

## 节点类型

`MiniMaxH3SPEEDPlanT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `spectrum_profile:H3_T8_SPEED_PROFILE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `steps:INT`（1 次）
- `scales:STRING`（1 次）
- `transition_mode:COMBO`（1 次）
- `manual_transition_sigmas:STRING`（1 次）
- `delta:FLOAT`（1 次）
- `shift_video:FLOAT`（1 次）
- `transform:COMBO`（1 次）

## 输出

- `speed_plan:H3_T8_SPEED_PLAN`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 576, 8, "0.5,1.0", "manual_sigmas", "0.85", 0.01, 12, "dct", "require_validated_profile", "error"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
