---
key: 图片生成/文生图/文生图-qwen_image2.1-t8pe加速版_2116696483385921537.json
name: 文生图-qwen_image2.1-t8pe加速版_2116696483385921537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-qwen_image2.1-t8pe加速版_2116696483385921537.json
hash: bc9e53c5a129d107
coverage: 0.730769
learned_at: 2026-11-02 19:16:30
nodes: [QwenImage21Cache, CLIPLoader, EmptyLatentImage, ComfySwitchNode, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, ResolutionSelector, UNETLoader, MarkdownNote, Note, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, easy showAnything, QwenPERewriteT8, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 705110640804333, "steps": 40, "width": 1024}
---

# 图片生成/文生图/文生图-qwen_image2.1-t8pe加速版_2116696483385921537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-qwen_image2.1-t8pe加速版_2116696483385921537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MarkdownNote`
- `Note`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `QwenPERewriteT8`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `705110640804333`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`ResolutionSelector`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SaveImage`、`SeedVR2LoadDiTModel`、`TextEncodeQwenImage21`、`QwenPERewriteT8`、`CR Prompt Text`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
