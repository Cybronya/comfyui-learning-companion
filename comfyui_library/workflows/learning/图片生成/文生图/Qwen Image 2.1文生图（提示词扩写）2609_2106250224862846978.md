---
key: 图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json
name: Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json
hash: 422d493a61e3d305
coverage: 0.47619
learned_at: 2026-10-06 21:49:15
nodes: [Anything Everywhere3, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, llama_cpp_instruct_adv, PreviewAny, llama_cpp_model_loader, TextEncodeQwenImage21, SaveImage, VAEDecode, SetNode, SeedVR2VideoUpscaler, GetNode, SaveImage, SeedVR2LoadVAEModel, ResolutionSelector, CR Text, SeedVR2LoadDiTModel, Fast Groups Bypasser (rgthree), KSampler]
patterns: []
missing: [CR Text, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, llama_cpp_model_loader, PreviewAny, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9528, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `llama_cpp_model_loader`
- `TextEncodeQwenImage21`
- `SaveImage`
- `VAEDecode` ★核心
- `SetNode`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `ResolutionSelector`
- `CR Text`
- `SeedVR2LoadDiTModel`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `9528`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（10/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImage`、`VAEDecode`、`ResolutionSelector`、`KSampler`

**缺卡**（8）：`CR Text`、`Fast Groups Bypasser (rgthree)`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`PreviewAny`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
