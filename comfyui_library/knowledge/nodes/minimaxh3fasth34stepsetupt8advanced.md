# MiniMaxH3FastH34StepSetupT8Advanced

## 节点类型

`MiniMaxH3FastH34StepSetupT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `av_latent:LATENT`（3 次）
- `task_family:COMBO`（3 次）
- `attention_profile:COMBO`（3 次）

## 输出

- `model:MODEL`（3 次）
- `sampler:SAMPLER`（3 次）
- `sigmas:SIGMAS`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ref2va_untrained_exp", "external_vsa_if_available"]`（2 次）
- `["t2va_only", "external_vsa_if_available"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
