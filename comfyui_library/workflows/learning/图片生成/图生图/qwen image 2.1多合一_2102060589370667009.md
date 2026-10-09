---
key: 图片生成/图生图/qwen image 2.1多合一_2102060589370667009.json
name: qwen image 2.1多合一_2102060589370667009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1多合一_2102060589370667009.json
hash: c74aab90aee5cd34
coverage: 0.558824
learned_at: 2026-10-09 22:27:07
nodes: [ResolutionSelector, LoadImage, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SeedVR2VideoUpscaler, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, TextInput_, EmptyLatentImage, QwenImage21Cache, TextEncodeQwenImage21, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, TextGenerateLTX2Prompt, SetNode, SetNode, GetNode, GetNode, TextGenerateLTX2Prompt, easy seed, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, LoraLoaderModelOnly, UNETLoader, CLIPLoader, CLIPLoader, Anything Everywhere3, easy showAnything, LoadImage, TextInput_, KSampler, SaveImage, SaveImageAdvanced, VAEDecode, SaveImageAdvanced]
patterns: []
missing: [忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 754172843471618, "steps": 25, "width": 1024}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/qwen image 2.1多合一_2102060589370667009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102060589370667009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `ResolutionSelector`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextInput_`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `TextGenerateLTX2Prompt`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `easy seed`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `easy showAnything`
- `LoadImage`
- `TextInput_`
- `KSampler` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImageAdvanced`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `754172843471618`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **56%**（38/68）

**有卡**：`ResolutionSelector`、`LoadImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`TextInput_`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImageAdvanced`

**缺卡**（6）：`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
