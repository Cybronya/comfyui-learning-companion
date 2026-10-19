# GrokCreateVideo

## 节点类型

`GrokCreateVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `size:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `image_urls:STRING`（1 次）

## 输出

- `任务ID:STRING`（1 次）
- `状态:STRING`（1 次）
- `增强提示词:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "3:2", "1080P", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
