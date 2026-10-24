# ACEPlusLoraProcessor

## 节点类型

`ACEPlusLoraProcessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `reference_image:IMAGE`（10 次）
- `edit_image:IMAGE`（10 次）
- `edit_mask:MASK`（10 次）
- `use_reference:BOOLEAN`（8 次）
- `height:INT`（8 次）
- `width:INT`（8 次）
- `task_type:COMBO`（8 次）
- `max_seq_length:INT`（8 次）

## 输出

- `IMAGE:IMAGE`（10 次）
- `MASK:MASK`（10 次）
- `OUT_H:INT`（10 次）
- `OUT_W:INT`（10 次）
- `SLICE_W:INT`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 1024, 1024, "repainting", 3072]`（4 次）
- `[true, 1024, 1024, "repainting", 4096]`（2 次）
- `[false, 1024, 1024, "recolorizing", 4096]`（1 次）
- `[false, 1024, 1024, "no_preprocess", 4096]`（1 次）
- `[true, 1024, 1024, "recolorizing", 3072]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
