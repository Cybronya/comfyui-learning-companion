# SAM3BBoxCollector

## 节点类型

`SAM3BBoxCollector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `bboxes:STRING`（2 次）
- `neg_bboxes:STRING`（2 次）

## 输出

- `positive_bboxes:SAM3_BOXES_PROMPT`（2 次）
- `negative_bboxes:SAM3_BOXES_PROMPT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[{\"x1\":421.8340454161721,\"y1\":163.0052656979243,\"x2\":902.0788247847681,\"y2\":716.9849792076183}]", "[]", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
