# RunningHub DreamID-Omni Sampler

## 节点类型

`RunningHub DreamID-Omni Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:RunningHub_DreamID_Omni_Pipeline`（2 次）
- `ref_image:IMAGE`（2 次）
- `ref_image2:IMAGE`（2 次）
- `ref_audio:AUDIO`（2 次）
- `ref_audio2:AUDIO`（2 次）
- `prompt:STRING`（2 次）
- `sample_steps:INT`（2 次）
- `seed:INT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["<img1>：画面中，一位留着黑色长发的女性被标识为 <sub1>。\n\n总体环境/场景：\n深夜，一家充满烟火气息的开放式厨房咖啡厅。灶台火苗跳动，热气腾腾；随着身后工作人员的走动，暖色调的吊灯在微微晃动。镜头采用的是人物上半身的近`（1 次）
- `["<img1>：画面中，一位留着黑色长发的女性被标识为 <sub1>。\n<img2>：画面中，一位留着黑色长发的女性被标识为 <sub2>。\n\n总体环境/场景：\n深夜，一家充满烟火气息的开放式厨房咖啡厅。灶台火苗跳动，热气腾腾；随`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
