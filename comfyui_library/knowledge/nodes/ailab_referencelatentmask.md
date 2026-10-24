# AILab_ReferenceLatentMask

## 节点类型

`AILab_ReferenceLatentMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）
- `mask:MASK`（3 次）
- `expand:INT`（3 次）
- `blur:FLOAT`（3 次）
- `mask_only:BOOLEAN`（3 次）

## 输出

- `CONDITIONING:CONDITIONING`（3 次）
- `LATENT:LATENT`（3 次）
- `MASK:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 2, 10]`（2 次）
- `[5, 5, 10]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
