# RH_MinimaxH3MaxTurboTextToVideo

## 节点类型

`RH_MinimaxH3MaxTurboTextToVideo`

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
- `aspectRatio:COMBO`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["巨大的银色飞船低空掠过未来城市，摩天楼表面流动着蓝色能量光带，镜头从街道仰拍迅速抬升到空中，飞船穿过云层飞向橙色日出，云层边缘泛着金色辉光。", "768p", "8", "3:4", false, 683116478, "random`（1 次）
- `["车内变装视频：Create an 8-second vertical 9:16 fashion vlog video inside a pink luxury car driver seat, same young woman thro`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
