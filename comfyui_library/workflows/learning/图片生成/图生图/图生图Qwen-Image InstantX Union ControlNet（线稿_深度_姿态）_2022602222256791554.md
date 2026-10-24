---
key: 图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_2022602222256791554.json
name: 图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_2022602222256791554
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_2022602222256791554.json
hash: 4ef674ec3c2cb75c
coverage: 0.811966
learned_at: 2026-10-23 12:43:11
nodes: [CLIPLoader, VAELoader, ModelSamplingAuraFlow, ControlNetApplyAdvanced, ControlNetLoader, CLIPLoader, VAELoader, ModelSamplingAuraFlow, VAEEncode, ControlNetLoader, CLIPLoader, VAELoader, ModelSamplingAuraFlow, LoraLoaderModelOnly, ControlNetLoader, LoraLoaderModelOnly, DepthAnything_V2, PreviewImage, Canny, PreviewImage, SaveImage, SaveImage, SaveImage, DWPreprocessor, MarkdownNote, VAEDecode, MarkdownNote, VAEDecode, MarkdownNote, Note, VAEDecode, VAEEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, LoadImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, Note, KSampler, KSampler, KSampler, VAEEncode, DownloadAndLoadDepthAnythingV2Model, ControlNetApplyAdvanced, ControlNetApplyAdvanced, PreviewImage, CLIPTextEncode, CLIPLoader, UNETLoader, Note, VAEDecode, ModelSamplingAuraFlow, LoraLoaderModelOnly, Note, SaveImage, Note, Note, VAEEncode, UNETLoader, UNETLoader, LoadImage, UNETLoader, UNETLoader, UNETLoader, UNETLoader, VAELoader, CLIPLoader, UNETLoader, Note, VAEDecode, Note, SaveImage, Note, Note, CLIPTextEncode, ModelSamplingAuraFlow, VAELoader, KSampler, ControlNetInpaintingAliMamaApply, LoraLoaderModelOnly, PDImageResizeV2, VAEEncode, KSampler, ControlNetLoader, Note, CLIPLoader, UNETLoader, Note, VAEDecode, Note, SaveImage, Note, Note, CLIPTextEncode, ModelSamplingAuraFlow, VAELoader, KSampler, ControlNetInpaintingAliMamaApply, LoraLoaderModelOnly, VAEEncode, ControlNetLoader, Note, PDImageResizeV2, ImagePadForOutpaint, LoadImage, CLIPTextEncode, LoadImage, CLIPTextEncode, CLIPTextEncode, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 353953510325720, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_2022602222256791554.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_2022602222256791554.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（117 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `ControlNetLoader`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `DepthAnything_V2`
- `PreviewImage`
- `Canny`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `DWPreprocessor`
- `MarkdownNote`
- `VAEDecode` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `MarkdownNote`
- `Note`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `DownloadAndLoadDepthAnythingV2Model`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `SaveImage`
- `Note`
- `Note`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `VAEDecode` ★核心
- `Note`
- `SaveImage`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `KSampler` ★核心
- `ControlNetInpaintingAliMamaApply`
- `LoraLoaderModelOnly` ★核心
- `PDImageResizeV2`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ControlNetLoader`
- `Note`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `VAEDecode` ★核心
- `Note`
- `SaveImage`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `KSampler` ★核心
- `ControlNetInpaintingAliMamaApply`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `ControlNetLoader`
- `Note`
- `PDImageResizeV2`
- `ImagePadForOutpaint`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `353953510325720`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（95/117）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`VAEEncode`、`LoraLoaderModelOnly`、`DepthAnything_V2`、`Canny`、`SaveImage`、`DWPreprocessor`、`VAEDecode`、`ImageScaleToTotalPixels`、`LoadImage`、`CLIPTextEncode`、`KSampler`、`DownloadAndLoadDepthAnythingV2Model`、`UNETLoader`、`ControlNetInpaintingAliMamaApply`、`PDImageResizeV2`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 6 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
