# workflow/遮罩

## 节点类型

`workflow/遮罩`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `detailer_hook:DETAILER_HOOK`（1 次）

## 输出

- `SEGM检测:SEGM_DETECTOR`（1 次）
- `遮罩:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bbox/hand_yolov8s.pt", 0.5, 10, 3, 10, "all", false, 20, 12]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
