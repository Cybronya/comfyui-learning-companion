# RH_Hitem3dV2MultiImageTo3d

## 节点类型

`RH_Hitem3dV2MultiImageTo3d`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `front_image:IMAGE`（2 次）
- `back_image:IMAGE`（2 次）
- `left_image:IMAGE`（2 次）
- `right_image:IMAGE`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `requestType:COMBO`（2 次）
- `resolution:COMBO`（2 次）
- `face:INT`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `model_url:STRING`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mesh", "1536", 1000000, false, 325732862654808, "randomize"]`（1 次）
- `["mesh", "1536", 1000000, false, 1036114997661134, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
