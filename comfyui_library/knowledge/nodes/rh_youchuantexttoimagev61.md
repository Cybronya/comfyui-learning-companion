# RH_YouchuanTextToImageV61

## 节点类型

`RH_YouchuanTextToImageV61`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `cref:IMAGE`（1 次）
- `sref:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `negativePrompt:STRING`（1 次）
- `chaos:INT`（1 次）
- `quality:COMBO`（1 次）
- `stylize:INT`（1 次）
- `weird:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["新国潮插画，国风青绿流体山水，流动渐变青绿色层叠山峦，流体丙烯肌理，左上斜出苍劲迎客古松，细碎金色山花点缀，纯白大量留白，左下角一位古装束发文人骑黑马，人物小巧，水墨晕染，低饱和莫兰迪青绿色调，极简干净背景，海报构图，细腻质感，高级简约`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
