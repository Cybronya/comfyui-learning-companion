# RH_YouchuanTextToImageV82

## 节点类型

`RH_YouchuanTextToImageV82`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `sref:IMAGE`（6 次）
- `api_config:RH_OPENAPI_CONFIG`（6 次）
- `prompt:STRING`（6 次）
- `hd:BOOLEAN`（6 次）
- `chaos:INT`（6 次）
- `quality:COMBO`（6 次）
- `stylize:INT`（6 次）
- `raw:BOOLEAN`（6 次）
- `iw:INT`（6 次）

## 输出

- `image:IMAGE`（6 次）
- `url:STRING`（6 次）
- `response:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", true, 2, "4", 2, false, 1, 100, 6, "4:3", false, 1143549711, "randomize"]`（1 次）
- `["", true, 2, "4", 2, false, 1, 100, 6, "4:3", false, 1385852855, "randomize"]`（1 次）
- `["", true, 2, "4", 2, false, 1, 100, 6, "4:3", false, 1843178539, "randomize"]`（1 次）
- `["", true, 0, "4", 0, false, 1, 100, 6, "16:9", false, 1978538386, "randomize"]`（1 次）
- `["", true, 0, "4", 0, false, 1, 100, 6, "16:9", false, 1145716667, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
