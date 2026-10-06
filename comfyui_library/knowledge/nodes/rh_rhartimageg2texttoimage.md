# RH_RhartImageG2TextToImage

## 节点类型

`RH_RhartImageG2TextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（3 次）
- `prompt:STRING`（3 次）
- `aspectRatio:COMBO`（3 次）
- `skip_error:BOOLEAN`（3 次）
- `seed:INT`（3 次）
- `resolution:COMBO`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "3:4", false, 954431881, "randomize", "2k"]`（1 次）
- `["", "16:9", false, 1553286340, "randomize", "4k"]`（1 次）
- `["", "16:9", true, 2012032379, "randomize", "1k"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
