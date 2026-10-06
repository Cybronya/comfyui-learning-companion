# WanVideoBlockSwap

## 节点类型

`WanVideoBlockSwap`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `blocks_to_swap:INT`（1 次）
- `offload_img_emb:BOOLEAN`（1 次）
- `offload_txt_emb:BOOLEAN`（1 次）
- `use_non_blocking:BOOLEAN`（1 次）
- `vace_blocks_to_swap:INT`（1 次）
- `prefetch_blocks:INT`（1 次）
- `block_swap_debug:BOOLEAN`（1 次）

## 输出

- `block_swap_args:BLOCKSWAPARGS`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, false, false]`（1 次）
- `[10, false, false]`（1 次）
- `[40, false, false, true, 0, 0, false]`（1 次）
- `[15]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
