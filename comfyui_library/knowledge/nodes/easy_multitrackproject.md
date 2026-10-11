# easy multitrackProject

## 节点类型

`easy multitrackProject`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `tracks_info:TRACKS_INFO`（2 次）
- `model_loader:FAST_MODEL_LOADER`（2 次）
- `model_loader_2nd:FAST_MODEL_LOADER`（2 次）
- `sampler:SAMPLER`（2 次）
- `sampler_2nd:SAMPLER`（2 次）
- `sigmas:SIGMAS`（2 次）
- `sigmas_2nd:SIGMAS`（2 次）
- `project_name:STRING`（2 次）
- `project_save:COMBO`（2 次）
- `segment_start_number:INT`（2 次）

## 输出

- `PROJECT_NAME:STRING`（2 次）
- `LOCKED_AUDIO:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "override", 1, -1, 962882747170081, "randomize", "medium", "single", false, false, 1.25, "None"]`（1 次）
- `["666", "override", 1, -1, 389483696530308, "randomize", "medium", "single", false, false, 1, "None"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
