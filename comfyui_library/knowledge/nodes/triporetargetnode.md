# TripoRetargetNode

## 节点类型

`TripoRetargetNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `original_model_task_id:RIG_TASK_ID`（14 次）

## 输出

- `model_file:STRING`（14 次）
- `retarget task_id:RETARGET_TASK_ID`（14 次）
- `GLB:FILE_3D_GLB`（14 次）
- `FBX:FILE_3D_FBX`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["preset:idle", "glb", true, false]`（12 次）
- `["preset:walk", "glb", true, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
