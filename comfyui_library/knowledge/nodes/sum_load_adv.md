# sum_load_adv

## 节点类型

`sum_load_adv`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `over_model:MODEL`（4 次）
- `over_clip:CLIP`（4 次）
- `lora_stack:LORASTACK`（4 次）

## 输出

- `context:RUN_CONTEXT`（4 次）
- `model:MODEL`（4 次）
- `preset_save:PDATA`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["clip2-flux/clip2-kontext.toml", "Flux_Kontext_dev_fp8.safetensors", "None", "fp8_e4m3fn", "flux", "clip_l.safetensors"`（1 次）
- `["clip2-flux/clip2-kontext.toml", "None", "flux1-kontext-dev.safetensors", "fp8_e4m3fn", "flux", "clip_l.safetensors", "`（1 次）
- `["clip2-flux/clip2-kontext.toml", "None", "flux1-dev-kontext_fp8_scaled.safetensors", "fp8_e4m3fn", "flux", "clip_l.safe`（1 次）
- `["clip2-flux/clip2-kontext.toml", "None", "flux1-kontext-dev-Q8_0.gguf", "fp8_e4m3fn", "flux", "clip_l.safetensors", "t5`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
