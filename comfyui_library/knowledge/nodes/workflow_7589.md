# workflow>自定义节点

## 节点类型

`workflow>自定义节点`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `模型:MODEL`（2 次）
- `正面条件:CONDITIONING`（2 次）
- `负面条件:CONDITIONING`（2 次）
- `Latent:LATENT`（2 次）
- `steps:INT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `noise_seed:INT`（2 次）
- `cfg:FLOAT`（2 次）
- `sampler_name:COMBO`（2 次）

## 输出

- `输出:LATENT`（2 次）
- `降噪输出:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 1024, 1024, 935493137599916, "randomize", 1, "euler"]`（1 次）
- `[4, 1024, 1024, 576223453712126, "randomize", 1, "sa_solver"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
