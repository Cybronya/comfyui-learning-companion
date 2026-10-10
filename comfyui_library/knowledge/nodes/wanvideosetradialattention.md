# WanVideoSetRadialAttention

## 节点类型

`WanVideoSetRadialAttention`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（13 次）
- `dense_attention_mode:COMBO`（13 次）
- `dense_blocks:INT`（13 次）
- `dense_vace_blocks:INT`（13 次）
- `dense_timesteps:INT`（13 次）
- `decay_factor:FLOAT`（13 次）
- `block_size:COMBO`（13 次）

## 输出

- `model:WANVIDEOMODEL`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sparse_sage_attention", 1, 1, 1, 0.2, 128]`（13 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
