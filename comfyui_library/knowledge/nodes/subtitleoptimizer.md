# SubtitleOptimizer

## 节点类型

`SubtitleOptimizer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `字幕数据:SUBTITLE_DATA`（1 次）
- `优化模式:COMBO`（1 次）
- `最小词数阈值:INT`（1 次）
- `最大词数限制:INT`（1 次）
- `时间间隔:INT`（1 次）
- `合并策略:COMBO`（1 次）
- `每段最大字符数:INT`（1 次）
- `分段阈值:INT`（1 次）

## 输出

- `优化后字幕:SUBTITLE_DATA`（1 次）
- `优化报告:STRING`（1 次）
- `完整时间戳文本:STRING`（1 次）
- `简洁时间戳文本:STRING`（1 次）
- `SRT格式文本:STRING`（1 次）
- `JSON格式文本:STRING`（1 次）
- `CSV格式文本:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["智能模式 ✨", 4, 10, 300, "标准合并", 40, 35]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
