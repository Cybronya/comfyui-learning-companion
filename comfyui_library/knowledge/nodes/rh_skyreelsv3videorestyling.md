# RH_SkyreelsV3VideoRestyling

## 节点类型

`RH_SkyreelsV3VideoRestyling`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video:VIDEO`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `styleName:COMBO`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["simpsons", false, 905986517431149, "randomize"]`（1 次）
- `["simpsons", false, 0, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
