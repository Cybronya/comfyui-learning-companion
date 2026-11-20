# workflow>shader_sea

## 节点类型

`workflow>shader_sea`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images.image0:IMAGE`（1 次）
- `ints.u_int0:INT`（1 次）
- `bools.u_bool0:BOOLEAN`（1 次）
- `curves.u_curve0:CURVE`（1 次）
- `value:FLOAT`（1 次）
- `fragment_shader:STRING`（1 次）
- `size_mode:COMFY_DYNAMICCOMBO_V3`（1 次）

## 输出

- `IMAGE0:IMAGE`（1 次）
- `IMAGE1:IMAGE`（1 次）
- `IMAGE2:IMAGE`（1 次）
- `IMAGE3:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "#version 300 es\nprecision highp float;\n\nuniform vec2 u_resolution;\nuniform float u_float0;    // TIME输入端口，外部Flo`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
