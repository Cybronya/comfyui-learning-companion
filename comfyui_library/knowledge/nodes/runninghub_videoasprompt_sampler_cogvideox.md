# RunningHub VideoAsPrompt Sampler(CogVideoX)

## 节点类型

`RunningHub VideoAsPrompt Sampler(CogVideoX)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `pipeline:RH_VideoAsPrompt_Pipeline`（3 次）
- `image:IMAGE`（3 次）
- `ref_video:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `prompt_mot_ref:STRING`（3 次）
- `height:INT`（3 次）
- `width:INT`（3 次）
- `num_frames:INT`（3 次）
- `num_inference_steps:INT`（3 次）
- `seed:INT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["one man transforms into a robot", "one man holding a gun transforms into a robot", 480, 720, 49, 50, 379340579543210, `（1 次）
- `["A chestnut-colored horse stands on a grassy hill against a backdrop of distant, snow-dusted mountains. The horse begin`（1 次）
- `["角色站起来跳舞", "From a low-angle perspective, a cream-colored sheep looks directly into the camera. The view widens as the `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
