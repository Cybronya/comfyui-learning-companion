# RH_BytedanceSeedance25GlobalTokenTextToVideo

## 节点类型

`RH_BytedanceSeedance25GlobalTokenTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `resolution:COMBO`（2 次）
- `duration:COMBO`（2 次）
- `generateAudio:BOOLEAN`（2 次）
- `ratio:COMBO`（2 次）
- `webSearch:BOOLEAN`（2 次）
- `returnLastFrame:BOOLEAN`（2 次）
- `bitrateMode:COMBO`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "720p", "6", true, "16:9", false, false, "standard", -1, "randomize", "mp4", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
