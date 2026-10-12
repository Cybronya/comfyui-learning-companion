# Context Switch (rgthree)

## 节点类型

`Context Switch (rgthree)`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ctx_01:RGTHREE_CONTEXT`（2 次）
- `ctx_02:RGTHREE_CONTEXT`（2 次）
- `ctx_03:RGTHREE_CONTEXT`（2 次）
- `ctx_04:RGTHREE_CONTEXT`（2 次）
- `ctx_05:RGTHREE_CONTEXT`（2 次）

## 输出

- `CONTEXT:RGTHREE_CONTEXT`（2 次）
- `MODEL:MODEL`（2 次）
- `CLIP:CLIP`（2 次）
- `VAE:VAE`（2 次）
- `POSITIVE:CONDITIONING`（2 次）
- `NEGATIVE:CONDITIONING`（2 次）
- `LATENT:LATENT`（2 次）
- `IMAGE:IMAGE`（2 次）
- `SEED:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
