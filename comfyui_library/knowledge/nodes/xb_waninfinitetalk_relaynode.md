# XB_WanInfiniteTalk_RelayNode

## 节点类型

`XB_WanInfiniteTalk_RelayNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `wan_infinitetalk_bus:WAN_INFINITETALK_BUS`（18 次）
- `prev_video:IMAGE`（18 次）
- `prev_audio:AUDIO`（18 次）
- `audio:AUDIO`（18 次）
- `positive_prompt:STRING`（18 次）
- `segment_length:INT`（18 次）

## 输出

- `📦 WAN_INFINITETALK_BUS (传给下段):WAN_INFINITETALK_BUS`（18 次）
- `🎞️ 累加视频流:IMAGE`（18 次）
- `🔊 累加音频流:AUDIO`（18 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 81]`（18 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
