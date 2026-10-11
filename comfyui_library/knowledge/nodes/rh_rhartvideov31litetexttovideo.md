# RH_RhartVideoV31LiteTextToVideo

## 节点类型

`RH_RhartVideoV31LiteTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `aspectRatio:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["暖黄柔光洒满客厅，一只橘白英短好奇走向三层实木转盘猫玩具。它用肉垫拨弄轨道里的木球与薄荷球，球滚动碰撞发出清脆声响；随即跃上猫抓柱，抓挠紧密不掉屑的麻绳，又咬住吊球悬空摆动；最后被羽毛逗猫棒吸引，猛地跃起扑向羽毛，铃铛轻响。画面干净柔和`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
