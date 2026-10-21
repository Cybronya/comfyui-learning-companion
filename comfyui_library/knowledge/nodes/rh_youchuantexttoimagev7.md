# RH_YouchuanTextToImageV7

## 节点类型

`RH_YouchuanTextToImageV7`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `sref:IMAGE`（2 次）
- `oref:IMAGE`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `negativePrompt:STRING`（2 次）
- `chaos:INT`（2 次）
- `quality:COMBO`（2 次）
- `stylize:INT`（2 次）
- `weird:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 0, "1", 0, 0, false, 1, 100, 4, 100, false, "16:9", false, 352187541, "randomize"]`（1 次）
- `["", "", 0, "1", 0, 0, false, 1, 100, 4, 100, false, "16:9", false, 1061917100, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
