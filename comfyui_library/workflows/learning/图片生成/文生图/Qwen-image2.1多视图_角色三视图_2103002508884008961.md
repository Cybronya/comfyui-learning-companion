---
key: 图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json
name: Qwen-image2.1多视图_角色三视图_2103002508884008961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json
hash: 012b13f600014844
coverage: 0.724138
learned_at: 2026-10-15 22:27:21
nodes: [VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, LayerUtility: ImageReel, UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, TextEncodeQwenImage21, KSampler, VAEDecode, TextEncodeQwenImage21, llama_cpp_model_loader, CR Text, llama_cpp_instruct_adv, PreviewAny, EmptyLatentImage, ResolutionSelector, ResolutionSelector, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9528, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `llama_cpp_model_loader`
- `CR Text`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ResolutionSelector`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

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

覆盖率 **72%**（21/29）

**有卡**：`VAEDecode`、`LayerUtility: ImageReelComposit`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`LayerUtility: ImageReel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`CR Text`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
