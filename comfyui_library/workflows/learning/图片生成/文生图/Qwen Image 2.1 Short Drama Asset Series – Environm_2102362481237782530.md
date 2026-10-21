---
key: 图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json
name: Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json
hash: 66cbe0d6994ae2bd
coverage: 0.705882
learned_at: 2026-10-20 01:50:51
nodes: [easy setNode, VAEDecode, EmptyLatentImage, Seed (rgthree), KSampler, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, GetNode, CLIPLoader, CLIPLoader, CLIPLoader, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, CR Prompt Text, LayerUtility: TextJoin, CR Prompt Text, SaveImage, ResolutionSelector, TextEncodeQwenImage21, TextGenerateLTX2Prompt, easy showAnything, Fast Groups Bypasser (rgthree), MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 93130720365265, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `easy setNode`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SaveImage`
- `CR Prompt Text`
- `LayerUtility: TextJoin`
- `CR Prompt Text`
- `SaveImage`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `93130720365265`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`easy setNode`、`VAEDecode`、`EmptyLatentImage`、`Seed (rgthree)`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`CLIPLoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SaveImage`、`CR Prompt Text`、`LayerUtility: TextJoin`、`ResolutionSelector`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
