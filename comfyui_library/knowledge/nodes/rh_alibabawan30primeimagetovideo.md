# RH_AlibabaWan30PrimeImageToVideo

## 节点类型

`RH_AlibabaWan30PrimeImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `first_frame:IMAGE`（3 次）
- `last_frame:IMAGE`（3 次）
- `api_config:RH_OPENAPI_CONFIG`（3 次）
- `resolution:COMBO`（3 次）
- `aspectRatio:COMBO`（3 次）
- `duration:COMBO`（3 次）
- `prompt:STRING`（3 次）
- `audio:BOOLEAN`（3 次）
- `seed:INT`（3 次）
- `skip_error:BOOLEAN`（3 次）

## 输出

- `video:VIDEO`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["480P", "adaptive", "2", "", true, 1307795056, "randomize", false]`（1 次）
- `["480P", "adaptive", "5", "", true, 2086731414, "randomize", false]`（1 次）
- `["720P", "adaptive", "5", "", true, 993528517, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
