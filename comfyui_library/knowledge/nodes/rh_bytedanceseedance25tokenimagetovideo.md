# RH_BytedanceSeedance25TokenImageToVideo

## 节点类型

`RH_BytedanceSeedance25TokenImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `first_frame:IMAGE`（1 次）
- `last_frame:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `prompt:STRING`（1 次）
- `generateAudio:BOOLEAN`（1 次）
- `ratio:COMBO`（1 次）
- `realPersonMode:BOOLEAN`（1 次）
- `conversionSlots:COMBO`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1080p", "10", "3:4竖屏，4K极致电影感MV画质，真实人像模式。夜幕降临的高空天台上，一位拥有精致东亚面孔、留着浓密黑色长卷发的摇滚女歌手在城市霓虹灯火下演唱。\n\n【00:00 - 00:05秒（起点对应图1）】\n`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
