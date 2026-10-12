# workflow>anime

## 节点类型

`workflow>anime`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `前上下文:CONTEXT_OPTIONS`（1 次）
- `视图设置:VIEW_OPTS`（1 次）
- `噪波层:NOISE_LAYERS`（1 次）
- `迭代设置:ITERATION_OPTS`（1 次）
- `自定CFG:CUSTOM_CFG`（1 次）
- `Sigma调度:SIGMA_SCHEDULE`（1 次）
- `image_inject:IMAGE_INJECT`（1 次）
- `动态模型:MOTION_MODEL_ADE`（1 次）
- `动态LoRA:MOTION_LORA`（1 次）
- `缩放多值:MULTIVAL`（1 次）

## 输出

- `上下文设置:CONTEXT_OPTIONS`（1 次）
- `采样设置:SAMPLE_SETTINGS`（1 次）
- `动态模型组:M_MODELS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, 8, "pyramid", false, 0, 1, 0, "FreeNoise", "comfy [gpu]", 0, false, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
