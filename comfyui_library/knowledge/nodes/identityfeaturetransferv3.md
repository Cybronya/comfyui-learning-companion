# IdentityFeatureTransferV3

## 节点类型

`IdentityFeatureTransferV3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `subject_mask:MASK`（2 次）
- `preset:COMBO`（2 次）
- `reference_index:INT`（2 次）
- `double_schedule:STRING`（2 次）
- `single_schedule:STRING`（2 次）
- `double_sim:FLOAT`（2 次）
- `single_sim:FLOAT`（2 次）
- `commit_margin:FLOAT`（2 次）
- `commit_confirm:INT`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MIDUM_LOCK", 0, "0-3:mid=0.25; 4:mid=0.35; 5:mid=0.65; 6-7:mid=0.45", "0:mid=0.35; 1:mid=0.25; 2-10:mid=0.30; 11-19:mi`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
