# RunningHub OmniConsistency Sampler

## 节点类型

`RunningHub OmniConsistency Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `style_lora:OCPipeline`（5 次）
- `spatial_images:IMAGE`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）
- `prompt:STRING`（5 次）

## 输出

- `image:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Vector style, a girl is sitting on the bed", 896, 1024, 3.5, 154384674523591, "randomize", 25]`（1 次）
- `["3D Chibi style, Three individuals standing together in the office.", 1024, 1024, 3.5, 822296471155374, "randomize", 25`（1 次）
- `["Vector style, a girl is sitting on the bed", 896, 1024, 3.5, 550067530098604, "randomize", 15]`（1 次）
- `["Vector style, a girl is sitting on the bed", 896, 1024, 3.5, 436207294190798, "randomize", 15]`（1 次）
- `["Vector style, a girl is sitting on the bed", 896, 1024, 3.5, 13808895436500, "randomize", 25]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
