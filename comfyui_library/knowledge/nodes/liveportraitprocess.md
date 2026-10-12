# LivePortraitProcess

## 节点类型

`LivePortraitProcess`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `pipeline:LIVEPORTRAITPIPE`（5 次）
- `crop_info:CROPINFO`（5 次）
- `source_image:IMAGE`（5 次）
- `driving_images:IMAGE`（5 次）
- `opt_retargeting_info:RETARGETINGINFO`（5 次）

## 输出

- `cropped_image:IMAGE`（5 次）
- `output:LP_OUT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 0.03, true, 1, "constant", "relative", 3e-06, true, 1.0030000000000001]`（2 次）
- `[false, 0.03, true, 1, "constant", "relative", 3e-06, true, 1]`（1 次）
- `[false, 0.03, true, 1, "constant", "relative", 3e-06, false, 1]`（1 次）
- `[true, 0.03, true, 1, "constant", "relative", 3e-06, false, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
