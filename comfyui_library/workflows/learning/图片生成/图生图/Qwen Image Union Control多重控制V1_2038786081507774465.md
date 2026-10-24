---
key: 图片生成/图生图/Qwen Image Union Control多重控制V1_2038786081507774465.json
name: Qwen Image Union Control多重控制V1_2038786081507774465
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image Union Control多重控制V1_2038786081507774465.json
hash: 997a791aed13534c
coverage: 0.843137
learned_at: 2026-10-23 11:13:26
nodes: [ReferenceLatent, ReferenceLatent, VAELoader, CLIPLoader, UNETLoader, MarkdownNote, KSampler, MarkdownNote, ModelSamplingAuraFlow, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, SaveImage, Canny, LoraLoaderModelOnly, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, VAELoader, CLIPLoader, UNETLoader, MarkdownNote, KSampler, MarkdownNote, ModelSamplingAuraFlow, VAEDecode, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, PreviewImage, SaveImage, LoraLoaderModelOnly, ImageScaleToTotalPixels, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, ReferenceLatent, ReferenceLatent, VAELoader, CLIPLoader, UNETLoader, KSampler, MarkdownNote, ModelSamplingAuraFlow, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, ImageScaleToTotalPixels, VAEEncode, VAEDecode, SaveImage, MiDaS-NormalMapPreprocessor, MarkdownNote, LoadImage, LoraLoaderModelOnly, ReferenceLatent, ReferenceLatent, VAELoader, CLIPLoader, UNETLoader, KSampler, MarkdownNote, ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPTextEncode, VAEEncode, VAEDecode, SaveImage, PreviewImage, MarkdownNote, LoadImage, LoraLoaderModelOnly, ImageScaleToTotalPixels, OpenposePreprocessor, ReferenceLatent, ReferenceLatent, VAELoader, CLIPLoader, UNETLoader, KSampler, MarkdownNote, ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, SaveImage, MarkdownNote, LoadImage, LoraLoaderModelOnly, ImageScaleToTotalPixels, OpenposePreprocessor, CLIPTextEncode, MarkdownNote, PreviewImage, CLIPTextEncode, PreviewImage, CLIPTextEncode, VAEEncode, PreviewImage, ImageScaleToTotalPixels, VAEDecode, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 279673668075344, "steps": 20}
---

# 图片生成/图生图/Qwen Image Union Control多重控制V1_2038786081507774465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image Union Control多重控制V1_2038786081507774465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Canny`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MiDaS-NormalMapPreprocessor`
- `MarkdownNote`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `MarkdownNote`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `OpenposePreprocessor`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `OpenposePreprocessor`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `279673668075344`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（86/102）

**有卡**：`ReferenceLatent`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`KSampler`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SaveImage`、`Canny`、`VAEEncode`、`VAEDecode`、`LoadImage`、`ImageScaleToTotalPixels`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`MiDaS-NormalMapPreprocessor`、`OpenposePreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
