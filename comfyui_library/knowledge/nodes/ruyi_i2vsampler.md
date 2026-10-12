# Ruyi_I2VSampler

## 节点类型

`Ruyi_I2VSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ruyi_model:RUYI_MODEL`（1 次）
- `start_img:IMAGE`（1 次）
- `end_img:IMAGE`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[56, 768, 914356998007630, "randomize", 25, 7, "DDIM", "2", "static", "normal_mode", "5"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
