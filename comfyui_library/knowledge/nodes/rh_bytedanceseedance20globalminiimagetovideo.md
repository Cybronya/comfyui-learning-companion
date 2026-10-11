# RH_BytedanceSeedance20GlobalMiniImageToVideo

## 节点类型

`RH_BytedanceSeedance20GlobalMiniImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `first_frame:IMAGE`（4 次）
- `last_frame:IMAGE`（4 次）
- `api_config:RH_OPENAPI_CONFIG`（4 次）
- `resolution:COMBO`（4 次）
- `duration:COMBO`（4 次）
- `prompt:STRING`（4 次）
- `generateAudio:BOOLEAN`（4 次）
- `ratio:COMBO`（4 次）
- `realPersonMode:BOOLEAN`（4 次）
- `conversionSlots:COMBO`（4 次）

## 输出

- `video:VIDEO`（4 次）
- `url:STRING`（4 次）
- `response:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["720p", "10", "国风氛围感短视频，首帧固定红墙斑驳古旧木门，满枝垂落白色樱花，午后暖阳光影在墙面与木门投下花枝细碎树影，花瓣随风缓缓零星飘落，镜头从红墙樱花场景缓慢向右轻柔平移推进，画面自然转场过渡，场景无缝渐变切换至室内暖`（1 次）
- `["720p", "5", "", true, "adaptive", true, "all", false, 1441627206, "randomize", false]`（1 次）
- `["720p", "5", "", true, "adaptive", true, "all", false, 577103054, "randomize", false]`（1 次）
- `["720p", "5", "", true, "adaptive", true, "all", false, 1857331540, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
