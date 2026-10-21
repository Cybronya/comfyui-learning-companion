---
key: 图片生成/文生图/角色设定集丨Qwen Image 2.1丨多视图·表情·姿态_2112093133474459649.json
name: 角色设定集丨Qwen Image 2.1丨多视图·表情·姿态_2112093133474459649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/角色设定集丨Qwen Image 2.1丨多视图·表情·姿态_2112093133474459649.json
hash: 36272ababe920e96
coverage: 0.741935
learned_at: 2026-10-21 03:02:50
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, JjkText, JjkText, JjkText, PrimitiveFloat, PrimitiveBoolean, PrimitiveInt, ResolutionSelector, QwenImage21Cache, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, KSampler, KSampler, KSampler, VAEDecode, VAEDecode, VAEDecode, ImageStitch, SaveImage, SaveImage, SaveImage, ImageStitch, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1344, "sampler_name": "euler", "scheduler": "beta", "seed": 333400813783706, "steps": 25, "width": 2368}
---

# 图片生成/文生图/角色设定集丨Qwen Image 2.1丨多视图·表情·姿态_2112093133474459649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/角色设定集丨Qwen Image 2.1丨多视图·表情·姿态_2112093133474459649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `JjkText`
- `JjkText`
- `JjkText`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `ResolutionSelector`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `SaveImage`

## 关键参数

- `width` = `2368`
- `height` = `1344`
- `batch_size` = `1`
- `seed` = `333400813783706`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **74%**（23/31）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`PrimitiveBoolean`、`ResolutionSelector`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`ImageStitch`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
