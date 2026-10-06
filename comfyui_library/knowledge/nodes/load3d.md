# Load3D

## 节点类型

`Load3D`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model_file:COMBO`（3 次）
- `image:LOAD_3D`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `mesh_path:STRING`（3 次）
- `normal:IMAGE`（3 次）
- `camera_info:LOAD3D_CAMERA`（3 次）
- `recording_video:VIDEO`（3 次）
- `model_3d:FILE_3D`（3 次）
- `model_3d_info:LOAD3D_MODEL_INFO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", null, "uploadExtraResources", "clear", "", 1024]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
