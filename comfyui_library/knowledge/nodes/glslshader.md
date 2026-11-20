# GLSLShader

## 节点类型

`GLSLShader`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images.image0:IMAGE`（6 次）
- `images.image1:IMAGE`（6 次）
- `floats.u_float0:FLOAT`（6 次）
- `floats.u_float1:FLOAT`（6 次）
- `ints.u_int0:INT`（6 次）
- `bools.u_bool0:BOOLEAN`（6 次）
- `curves.u_curve0:CURVE`（6 次）
- `fragment_shader:STRING`（6 次）
- `size_mode:COMFY_DYNAMICCOMBO_V3`（6 次）
- `floats.u_float2:FLOAT`（6 次）

## 输出

- `IMAGE0:IMAGE`（6 次）
- `IMAGE1:IMAGE`（6 次）
- `IMAGE2:IMAGE`（6 次）
- `IMAGE3:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#version 300 es\nprecision highp float;\n\nuniform vec2 u_resolution;\nuniform float u_float0; // iTime\nuniform float`（1 次）
- `["#version 300 es\nprecision highp float;\n\nuniform sampler2D u_image0; // Color贴图 images.image0\nuniform sampler2D u_i`（1 次）
- `["#version 300 es\nprecision highp float;\n\nuniform sampler2D u_image0; // Color images.image0\nuniform sampler2D u_ima`（1 次）
- `["#version 300 es\nprecision highp float;\n\nuniform vec2 u_resolution;\nuniform float u_float0;    // TIME输入端口，外部Float驱`（1 次）
- `["#version 300 es\nprecision highp float;\n\nuniform vec2 u_resolution;\nuniform float u_float0;\n\n// 三张图片输入，取图片中心点颜色作为`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
