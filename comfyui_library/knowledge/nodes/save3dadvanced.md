# Save3DAdvanced

## 节点类型

`Save3DAdvanced`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `model_3d:FILE_3D_GLB,FILE_3D_GLTF,FILE_3D_FBX,FILE_3D_OBJ,FILE_3D_STL,FILE_3D_USDZ,FILE_3D`（8 次）
- `model_3d_info:LOAD3D_MODEL_INFO`（8 次）
- `camera_info:LOAD3D_CAMERA`（8 次）

## 输出

- `model_3d:FILE_3D`（8 次）
- `model_3d_info:LOAD3D_MODEL_INFO`（8 次）
- `camera_info:LOAD3D_CAMERA`（8 次）
- `width:INT`（8 次）
- `height:INT`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["3d/ComfyUI", "", 1024, 1024]`（3 次）
- `["3d/Tripo_p2", "", 1024, 1024]`（2 次）
- `["3d/meshy_image2model", "", 1024, 1024]`（1 次）
- `["3d/Tripo3.1_i2m", "", 1024, 1024]`（1 次）
- `["3d/Tripo_P2", "", 1024, 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
