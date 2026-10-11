# RH_SparkVideoAssetQuery

## 节点类型

`RH_SparkVideoAssetQuery`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `asset_id:STRING`（21 次）
- `api_config:RH_OPENAPI_CONFIG`（21 次）
- `skip_error:BOOLEAN`（21 次）

## 输出

- `asset_id:STRING`（21 次）
- `status:STRING`（21 次）
- `preview_url:STRING`（21 次）
- `response:STRING`（21 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false]`（21 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
