---
key: 图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2108914820471939073.json
name: Qwenimage2.1漫转真+换头+写真_2108914820471939073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2108914820471939073.json
hash: ec7992195e5a0596
coverage: 0.755556
learned_at: 2026-10-23 11:21:47
nodes: [VAEDecode, KSampler, Image Comparer (rgthree), TextEncodeQwenImage21, SaveImage, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), TextEncodeQwenImage21, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, TextEncodeQwenImage21, KSampler, VAEDecode, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, MarkdownNote, MarkdownNote, MarkdownNote, Fast Groups Bypasser (rgthree), Anything Everywhere3, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, SaveImage, LoadImage, ProcessString, easy promptLine, RHLLMChatNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2108914820471939073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2108914820471939073.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `SaveImage`
- `LoadImage`
- `ProcessString`
- `easy promptLine`
- `RHLLMChatNode`

## 关键参数

- `seed` = `42`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`VAEDecode`、`KSampler`、`TextEncodeQwenImage21`、`SaveImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ResolutionSelector`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`ProcessString`、`easy promptLine`、`RHLLMChatNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
