---
key: 图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json
name: Qwen-image2.1多视图_角色三视图_2103002508884008961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json
hash: 012b13f600014844
coverage: 0.62069
learned_at: 2026-10-10 20:59:05
nodes: [VAEDecode, LayerUtility: ImageReelComposit, PreviewImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, LayerUtility: ImageReel, UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, TextEncodeQwenImage21, KSampler, VAEDecode, TextEncodeQwenImage21, llama_cpp_model_loader, CR Text, llama_cpp_instruct_adv, PreviewAny, EmptyLatentImage, ResolutionSelector, ResolutionSelector, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: [CR Text, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9528, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json`

## 结构

**节点**（29 个）：
- `VAEDecode`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `LayerUtility: ImageReel`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `KSampler`
- `VAEDecode`
- `TextEncodeQwenImage21`
- `llama_cpp_model_loader`
- `CR Text`
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `EmptyLatentImage`
- `ResolutionSelector`
- `ResolutionSelector`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

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

覆盖率 **62%**（18/29）

**有卡**：`VAEDecode`、`LayerUtility: ImageReelComposit`、`PreviewImage`、`EmptyLatentImage`、`Fast Groups Bypasser (rgthree)`、`KSampler`、`SaveImage`、`LayerUtility: ImageReel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Anything Everywhere3`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`CR Text`

**缺卡**（3）：`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
