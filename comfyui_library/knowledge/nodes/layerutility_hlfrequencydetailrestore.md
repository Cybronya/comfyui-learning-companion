# LayerUtility: HLFrequencyDetailRestore

## 节点类型

`LayerUtility: HLFrequencyDetailRestore`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `detail_image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `keep_high_freq:INT`（3 次）
- `erase_low_freq:INT`（3 次）
- `mask_blur:INT`（3 次）

## 输出

- `image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[6, 6, 0]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
