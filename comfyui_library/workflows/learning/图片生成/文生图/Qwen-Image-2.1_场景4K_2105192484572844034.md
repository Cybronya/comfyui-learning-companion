---
key: 图片生成/文生图/Qwen-Image-2.1_场景4K_2105192484572844034.json
name: Qwen-Image-2.1_场景4K_2105192484572844034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1_场景4K_2105192484572844034.json
hash: 0c0fda8cf67e1487
coverage: 0.619048
learned_at: 2026-10-07 02:25:19
nodes: [CR Text, CR Text Concatenate, easy seed, QZ_ResolutionPreset, SimpleMathDual+, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SimpleMathDual+, SeedVR2VideoUpscaler, ImageScale, SaveImage, Note, CR Text]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate, SimpleMathDual+, SimpleMathDual+, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 2048}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen-Image-2.1_场景4K_2105192484572844034.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1_场景4K_2105192484572844034.json`

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

覆盖率 **62%**（13/21）

**有卡**：`QZ_ResolutionPreset`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScale`、`SaveImage`

**缺卡**（6）：`CR Text`、`CR Text`、`CR Text Concatenate`、`SimpleMathDual+`、`SimpleMathDual+`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、SeedVR2LoadDiTModel

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
