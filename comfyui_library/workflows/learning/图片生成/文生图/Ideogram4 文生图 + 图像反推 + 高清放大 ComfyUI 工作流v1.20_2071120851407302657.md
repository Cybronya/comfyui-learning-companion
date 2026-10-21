---
key: 图片生成/文生图/Ideogram4 文生图 + 图像反推 + 高清放大 ComfyUI 工作流v1.20_2071120851407302657.json
name: Ideogram4 文生图 + 图像反推 + 高清放大 ComfyUI 工作流v1.20_2071120851407302657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ideogram4 文生图 + 图像反推 + 高清放大 ComfyUI 工作流v1.20_2071120851407302657.json
hash: 91dbc3469bc292fb
coverage: 0.809524
learned_at: 2026-10-19 23:41:03
nodes: [ModelSamplingAuraFlow, VAELoader, CLIPLoader, ImageScaleBy, SeedVR2LoadVAEModel, Image Comparer (rgthree), SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, BasicScheduler, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, PreviewImage, SaveImage, PreviewImage, ResolutionSelector, EmptyLatentImage, RandomNoise, KSamplerSelect, easy cleanGpuUsed, ModelSamplingAuraFlow, DualModelGuider, CFGOverride, CLIPTextEncode, UNETLoader, Qwen3_VQA, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, LoadImage, JoinStrings, easy cleanGpuUsed, easy showAnything, ShowText|pysssss, easy textSwitch, Text Multiline, Fast Groups Bypasser (rgthree), Text Multiline, Note, Int, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1280, "width": 720}
---

# 图片生成/文生图/Ideogram4 文生图 + 图像反推 + 高清放大 ComfyUI 工作流v1.20_2071120851407302657.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ideogram4 文生图 + 图像反推 + 高清放大 ComfyUI 工作流v1.20_2071120851407302657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `ImageScaleBy`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingAuraFlow`
- `DualModelGuider`
- `CFGOverride`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Qwen3_VQA`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `JoinStrings`
- `easy cleanGpuUsed`
- `easy showAnything`
- `ShowText|pysssss`
- `easy textSwitch`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`
- `Note`
- `Int`
- `孤海注释`

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SamplerCustomAdvanced`、`VAEDecode`、`CLIPTextEncode`、`BasicScheduler`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`、`RandomNoise`、`KSamplerSelect`、`easy cleanGpuUsed`、`DualModelGuider`、`CFGOverride`、`UNETLoader`、`Qwen3_VQA`、`LoraLoaderModelOnly`、`LoadImage`、`JoinStrings`、`easy textSwitch`、`Text Multiline`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
