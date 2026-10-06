# InstructPixToPixConditioning

## 节点类型

`InstructPixToPixConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `pixels:IMAGE`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
