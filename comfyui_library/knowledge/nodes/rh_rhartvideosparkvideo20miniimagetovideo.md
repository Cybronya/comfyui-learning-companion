# RH_RhartVideoSparkvideo20MiniImageToVideo

## 节点类型

`RH_RhartVideoSparkvideo20MiniImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `first_frame:IMAGE`（2 次）
- `last_frame:IMAGE`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `resolution:COMBO`（2 次）
- `duration:COMBO`（2 次）
- `prompt:STRING`（2 次）
- `generateAudio:BOOLEAN`（2 次）
- `ratio:COMBO`（2 次）
- `realPersonMode:BOOLEAN`（2 次）
- `conversionSlots:COMBO`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["720p", "5", "", true, "adaptive", true, "all", false, 1861313902, "randomize", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
