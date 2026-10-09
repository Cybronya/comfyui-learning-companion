# RH_YouchuanTextToImageV82Fast

## 节点类型

`RH_YouchuanTextToImageV82Fast`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `sref:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `hd:BOOLEAN`（1 次）
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

- `["", false, "", 0, "4", 100, 0, 1529774663, "randomize", true, 1, 100, 6, false, false, 0, "", "3:4", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
