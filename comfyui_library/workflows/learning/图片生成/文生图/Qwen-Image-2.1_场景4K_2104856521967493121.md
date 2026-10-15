---
key: 图片生成/文生图/Qwen-Image-2.1_场景4K_2104856521967493121.json
name: Qwen-Image-2.1_场景4K_2104856521967493121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1_场景4K_2104856521967493121.json
hash: 23ffb8cb5b7e7568
coverage: 0.904762
learned_at: 2026-10-15 22:27:12
nodes: [CR Text, CR Text Concatenate, easy seed, QZ_ResolutionPreset, SimpleMathDual+, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SimpleMathDual+, SeedVR2VideoUpscaler, ImageScale, SaveImage, Note, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 2048}
---

# 图片生成/文生图/Qwen-Image-2.1_场景4K_2104856521967493121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1_场景4K_2104856521967493121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CR Text`
- `CR Text Concatenate`
- `easy seed`
- `QZ_ResolutionPreset`
- `SimpleMathDual+`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SimpleMathDual+`
- `SeedVR2VideoUpscaler`
- `ImageScale`
- `SaveImage`
- `Note`
- `CR Text`

## 关键参数

- `width` = `2048`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CR Text`、`CR Text Concatenate`、`easy seed`、`QZ_ResolutionPreset`、`SimpleMathDual+`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScale`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、SeedVR2LoadDiTModel
