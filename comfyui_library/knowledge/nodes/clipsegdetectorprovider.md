# CLIPSegDetectorProvider

## 节点类型

`CLIPSegDetectorProvider`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `text:STRING`（1 次）

## 输出

- `BBOX_DETECTOR:BBOX_DETECTOR`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 7, 0.4, 4]`（2 次）
- `["face", 7, 0.4, 4]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
