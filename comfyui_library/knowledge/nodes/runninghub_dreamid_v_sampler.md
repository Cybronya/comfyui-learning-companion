# RunningHub_DreamID-V_Sampler

## 节点类型

`RunningHub_DreamID-V_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 20 个 workflow 中。

## 输入

- `pipeline:RH_DreamID-V_Pipeline`（20 次）
- `video:VIDEO`（20 次）
- `ref_image:IMAGE`（20 次）
- `size:COMBO`（20 次）
- `frame_num:INT`（20 次）
- `sample_steps:INT`（20 次）
- `fps:INT`（20 次）
- `seed:INT`（20 次）
- `custom_width:INT`（20 次）
- `custom_height:INT`（20 次）

## 输出

- `frames:IMAGE`（20 次）
- `video:VIDEO`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["832*480", 193, 20, 24, 464241251896148, "randomize", 0.5, 832, 480]`（1 次）
- `["832*480", 193, 20, 24, 150739250517681, "randomize", 0.5000000000000001, 480, 480]`（1 次）
- `["480*832", 193, 20, 24, 5053496044172, "randomize", 832, 480]`（1 次）
- `["832*480", 81, 20, 24, 766989478508320, "randomize", 832, 480]`（1 次）
- `["custom", 81, 20, 24, 951073901274759, "randomize", 480, 832]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
