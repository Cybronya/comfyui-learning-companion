---
key: 图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json
name: Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json
hash: 422d493a61e3d305
coverage: 0.714286
learned_at: 2026-10-10 20:58:54
nodes: [Anything Everywhere3, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, llama_cpp_instruct_adv, PreviewAny, llama_cpp_model_loader, TextEncodeQwenImage21, SaveImage, VAEDecode, SetNode, SeedVR2VideoUpscaler, GetNode, SaveImage, SeedVR2LoadVAEModel, ResolutionSelector, CR Text, SeedVR2LoadDiTModel, Fast Groups Bypasser (rgthree), KSampler]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9528, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图（提示词扩写）2609_2106250224862846978.json`

## 结构

**节点**（21 个）：
- `Anything Everywhere3`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `llama_cpp_model_loader`
- `TextEncodeQwenImage21`
- `SaveImage`
- `VAEDecode`
- `SetNode`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `ResolutionSelector`
- `CR Text`
- `SeedVR2LoadDiTModel`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `9528`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`Anything Everywhere3`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`llama_cpp_instruct_adv`、`PreviewAny`、`llama_cpp_model_loader`、`TextEncodeQwenImage21`、`SaveImage`、`VAEDecode`、`SetNode`、`SeedVR2VideoUpscaler`、`GetNode`

**缺卡**（1）：`CR Text`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
