---
key: 图片生成/反推提示词/Qwen-image2.1 文生图+VOSR2放大_2105647237308174337.json
name: Qwen-image2.1 文生图+VOSR2放大_2105647237308174337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen-image2.1 文生图+VOSR2放大_2105647237308174337.json
hash: e04f2f6ad75f4537
coverage: 0.434783
learned_at: 2026-10-06 21:37:19
nodes: [CLIPLoader, VAELoader, UNETLoader, Anything Everywhere3, llama_cpp_model_loader, CR Text, TextEncodeQwenImage21, ResolutionSelector, VOSR2ModelLoader, SplitImageWithAlpha, VOSR2Upscale, MarkdownNote, Fast Groups Bypasser (rgthree), EmptyLatentImage, SaveImage, SaveImage, KSampler, VAEDecode, PreviewAny, llama_cpp_instruct_adv, Image Comparer (rgthree), MarkdownNote, 孤海注释]
patterns: []
missing: [CR Text, Fast Groups Bypasser (rgthree), SplitImageWithAlpha, VOSR2ModelLoader, VOSR2Upscale, llama_cpp_instruct_adv, llama_cpp_model_loader, PreviewAny]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 9528, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `VOSR2ModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `VOSR2Upscale` 相关主题 Upscale 在知识库中无对应知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/反推提示词/Qwen-image2.1 文生图+VOSR2放大_2105647237308174337.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen-image2.1 文生图+VOSR2放大_2105647237308174337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Anything Everywhere3`
- `llama_cpp_model_loader`
- `CR Text`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `VOSR2ModelLoader`
- `SplitImageWithAlpha`
- `VOSR2Upscale`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `孤海注释`

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

覆盖率 **43%**（10/23）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`VAEDecode`

**缺卡**（8）：`CR Text`、`Fast Groups Bypasser (rgthree)`、`SplitImageWithAlpha`、`VOSR2ModelLoader`、`VOSR2Upscale`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`PreviewAny`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识
- 次要节点 `VOSR2ModelLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `VOSR2Upscale` 相关主题 Upscale 在知识库中无对应知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
