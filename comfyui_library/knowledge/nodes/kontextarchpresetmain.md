# KontextArchPresetMain

## 节点类型

`KontextArchPresetMain`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `时间:COMBO`（3 次）
- `天气:COMBO`（3 次）
- `建筑结构:COMBO`（3 次）
- `建筑材料:COMBO`（3 次）
- `周边环境:COMBO`（3 次）
- `玻璃效果:COMBO`（3 次）
- `天空效果:COMBO`（3 次）
- `custom_prompt:STRING`（3 次）

## 输出

- `prompt:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["清晨", "阴天", "混凝土结构", "无", "住宅区", "内透灯光", "多云", ""]`（1 次）
- `["正午", "阴天", "无", "玻璃幕墙", "校园", "镜面玻璃", "多云", ""]`（1 次）
- `["无", "无", "无", "无", "无", "无", "无云", "\n\n\n"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
