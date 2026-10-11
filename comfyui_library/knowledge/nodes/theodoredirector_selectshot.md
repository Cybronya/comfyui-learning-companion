# TheodoreDirector_SelectShot

## 节点类型

`TheodoreDirector_SelectShot`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `plan:THEODORE_DIRECTOR_PLAN`（3 次）
- `queue_index:INT`（3 次）
- `base_seed:INT`（3 次）
- `resume_mode:COMBO`（3 次）

## 输出

- `SHOT:THEODORE_DIRECTOR_SHOT`（3 次）
- `prompt:STRING`（3 次）
- `negative_prompt:STRING`（3 次）
- `duration_seconds:FLOAT`（3 次）
- `seed:INT`（3 次）
- `shot_id:STRING`（3 次）
- `active_index:INT`（3 次）
- `source_index:INT`（3 次）
- `active_count:INT`（3 次）
- `is_first:BOOLEAN`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 123456790, "resume"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
