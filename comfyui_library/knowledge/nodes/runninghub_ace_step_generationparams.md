# RunningHub ACE-Step GenerationParams

## 节点类型

`RunningHub ACE-Step GenerationParams`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `caption:STRING`（3 次）
- `lyrics:STRING`（3 次）
- `bpm:INT`（3 次）
- `duration:FLOAT`（3 次）
- `keyscale:STRING`（3 次）
- `timesignature:STRING`（3 次）

## 输出

- `generation params:ACEStepGenerationParams`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 95, 240, "F# minor", "4"]`（2 次）
- `["genre=urban-electronic ballad / sad pop\ntempo=70 → 86 bpm（尾副歌爆发）\nkey=Am → C major（升调照亮人海）\nmood=lonely-crowded / neo`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
