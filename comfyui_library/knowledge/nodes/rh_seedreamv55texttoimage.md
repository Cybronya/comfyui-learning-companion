# RH_SeedreamV55TextToImage

## 节点类型

`RH_SeedreamV55TextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `resolution:COMBO`（2 次）
- `outputFormat:COMBO`（2 次）
- `watermark:COMBO`（2 次）
- `background:COMBO`（2 次）
- `optimizePromptMode:COMBO`（2 次）
- `safetyIdentifier:STRING`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Avant-garde fashion photography, a female model walking in profile wearing an oversized glossy ivory bomber jacket and`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
