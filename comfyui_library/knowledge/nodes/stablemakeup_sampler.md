# StableMakeup_Sampler

## 节点类型

`StableMakeup_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `id_image:IMAGE`（4 次）
- `makeup_image:IMAGE`（4 次）
- `pipe:MODEL`（4 次）
- `makeup_encoder:MODEL`（4 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 输出

- `image:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mobilenet", "300wpublic", 1.6, 30, 512, 512]`（3 次）
- `["mobilenet", "300wpublic", 1.5, 20, 768, 768]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
