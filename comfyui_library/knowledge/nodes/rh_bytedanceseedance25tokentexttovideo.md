# RH_BytedanceSeedance25TokenTextToVideo

## 节点类型

`RH_BytedanceSeedance25TokenTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `generateAudio:BOOLEAN`（1 次）
- `ratio:COMBO`（1 次）
- `webSearch:BOOLEAN`（1 次）
- `returnLastFrame:BOOLEAN`（1 次）
- `bitrateMode:COMBO`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["**15秒电影级追逐短片：**暴雨后的未来东京街头，夜晚霓虹灯映照湿润路面。一位黑色长发的年轻成年女性，穿暗红色长风衣、黑色长裤和短靴，从一家便利店冲出，右手提着透明手提箱，快速跑向路边一辆银色未来感跑车。镜头从店内低机位开始，一镜跟随`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
