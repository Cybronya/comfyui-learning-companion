# SONICSampler

## 节点类型

`SONICSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `model:MODEL_SONIC`（9 次）
- `data_dict:SONIC_PREDATA`（9 次）
- `seed:INT`（1 次）
- `dynamic_scale:FLOAT`（1 次）

## 输出

- `image:IMAGE`（9 次）
- `fps:FLOAT`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[237894021, "randomize", 25, 1, 25]`（1 次）
- `[1783642930, "randomize", 25, 1, 25]`（1 次）
- `[427401818, "randomize", 25, 1, 25]`（1 次）
- `[1193351165, "randomize", 25, 1, 25]`（1 次）
- `[473352584, "fixed", 25, 1, 25]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
