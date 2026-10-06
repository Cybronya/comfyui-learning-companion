# VideoDepthAnythingProcess

## 节点类型

`VideoDepthAnythingProcess`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `vda_model:VDAMODEL`（5 次）
- `images:IMAGE`（5 次）
- `input_size:INT`（5 次）
- `max_res:INT`（5 次）
- `precision:COMBO`（5 次）
- `colormap:COMBO`（5 次）

## 输出

- `image:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[518, 1280, "fp16", "gray"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
