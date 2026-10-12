# ToraEncodeTrajectory

## 节点类型

`ToraEncodeTrajectory`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `tora_model:TORAMODEL`（1 次）
- `vae:VAE`（1 次）
- `coordinates:STRING`（1 次）
- `num_frames:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `tora_trajectory:TORAFEATURES`（1 次）
- `video_flow_images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 720, 480, 49, 1, 0, 1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
