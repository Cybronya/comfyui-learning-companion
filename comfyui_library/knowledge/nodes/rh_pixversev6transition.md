# RH_PixverseV6Transition

## 节点类型

`RH_PixverseV6Transition`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `first_image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `resolution:COMBO`（1 次）
- `duration:INT`（1 次）
- `generateAudioSwitch:BOOLEAN`（1 次）
- `generateMultiClipSwitch:BOOLEAN`（1 次）
- `negativePrompt:STRING`（1 次）
- `aspectRatio:COMBO`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "720p", 5, false, false, "", "1:1", true, "anime", 287733292, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
