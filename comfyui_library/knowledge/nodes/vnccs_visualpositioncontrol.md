# VNCCS_VisualPositionControl

## 节点类型

`VNCCS_VisualPositionControl`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `camera_data:STRING`（6 次）

## 输出

- `prompt:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["{\"azimuth\":225,\"elevation\":60,\"distance\":\"medium shot\",\"include_trigger\":true}", ""]`（2 次）
- `["{\"azimuth\":0,\"elevation\":-30,\"distance\":\"wide shot\",\"include_trigger\":true}", ""]`（1 次）
- `["{\"azimuth\":45,\"elevation\":30,\"distance\":\"medium shot\",\"include_trigger\":true}", ""]`（1 次）
- `["{\"azimuth\":180,\"elevation\":60,\"distance\":\"wide shot\",\"include_trigger\":true}", ""]`（1 次）
- `["{\"azimuth\":270,\"elevation\":0,\"distance\":\"wide shot\",\"include_trigger\":true}", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
