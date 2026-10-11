# RHBerniniFullTextToVideo

## 节点类型

`RHBerniniFullTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）
- `negative_prompt:STRING`（2 次）
- `num_frames:INT`（2 次）
- `fps:INT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `steps:INT`（2 次）
- `seed:INT`（2 次）
- `quality_preset:COMBO`（2 次）
- `acceleration:COMBO`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Day time, side lighting, medium shot, center composition. A large, fluffy white polar bear sits upright on a snowbank,`（1 次）
- `["Day time, side lighting, medium shot, center composition. A large, fluffy white polar bear sits upright on a snowbank,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
