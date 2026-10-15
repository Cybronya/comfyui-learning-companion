---
key: 图片生成/文生图/InstantX_Qwen-Image-ControlNet-Union（,线稿_深度_姿态）_1961145405088186369.json
name: InstantX_Qwen-Image-ControlNet-Union（,线稿_深度_姿态）_1961145405088186369
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/InstantX_Qwen-Image-ControlNet-Union（,线稿_深度_姿态）_1961145405088186369.json
hash: 14c13f28824237c1
coverage: 0.708333
learned_at: 2026-10-10 20:58:41
nodes: [MarkdownNote, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, VAEDecode, Note, Note, MarkdownNote, ImageScaleToTotalPixels, MarkdownNote, MarkdownNote, Canny, ControlNetApplyAdvanced, VAEEncode, CLIPTextEncode, PreviewImage, LoraLoaderModelOnly, KSampler, CLIPTextEncode, LoadImage, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, ControlNetLoader, SaveImage, MarkdownNote, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, VAEDecode, Note, Note, MarkdownNote, MarkdownNote, MarkdownNote, ControlNetApplyAdvanced, VAEEncode, CLIPTextEncode, PreviewImage, LoraLoaderModelOnly, KSampler, CLIPTextEncode, LoadImage, ControlNetLoader, SaveImage, MarkdownNote, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, VAEDecode, Note, Note, MarkdownNote, MarkdownNote, MarkdownNote, Canny, ControlNetApplyAdvanced, VAEEncode, CLIPTextEncode, PreviewImage, LoraLoaderModelOnly, KSampler, CLIPTextEncode, LoadImage, SaveImage, ImageScaleToTotalPixels, Canny, ImageScaleToTotalPixels, DWPreprocessor, ControlNetLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 514475539865847, "steps": 20}
---

# 图片生成/文生图/InstantX_Qwen-Image-ControlNet-Union（,线稿_深度_姿态）_1961145405088186369.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/InstantX_Qwen-Image-ControlNet-Union（,线稿_深度_姿态）_1961145405088186369.json`

## 结构

**节点**（72 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `VAEDecode`
- `Note`
- `Note`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `MarkdownNote`
- `Canny`
- `ControlNetApplyAdvanced`
- `VAEEncode`
- `CLIPTextEncode`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `KSampler`
- `CLIPTextEncode`
- `LoadImage`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `ControlNetLoader`
- `SaveImage`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `VAEDecode`
- `Note`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ControlNetApplyAdvanced`
- `VAEEncode`
- `CLIPTextEncode`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `KSampler`
- `CLIPTextEncode`
- `LoadImage`
- `ControlNetLoader`
- `SaveImage`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `VAEDecode`
- `Note`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Canny`
- `ControlNetApplyAdvanced`
- `VAEEncode`
- `CLIPTextEncode`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `KSampler`
- `CLIPTextEncode`
- `LoadImage`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `Canny`
- `ImageScaleToTotalPixels`
- `DWPreprocessor`
- `ControlNetLoader`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `2.5`
- `controlnet_strength` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `514475539865847`
- `steps` = `20`

## 知识

覆盖率 **71%**（51/72）

**有卡**：`MarkdownNote`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`Note`、`ImageScaleToTotalPixels`、`Canny`、`ControlNetApplyAdvanced`、`VAEEncode`、`CLIPTextEncode`、`PreviewImage`、`LoraLoaderModelOnly`、`KSampler`、`LoadImage`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`ControlNetLoader`、`SaveImage`
