# ColorTransfer

## 节点类型

`ColorTransfer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image_target:IMAGE`（5 次）
- `image_ref:IMAGE`（5 次）
- `method:COMBO`（5 次）
- `source_stats:COMFY_DYNAMICCOMBO_V3`（5 次）
- `source_stats.target_index:INT`（5 次）
- `strength:FLOAT`（5 次）

## 输出

- `image:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mkl_lab", "target_frame", 0, 0.7500000000000001]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
