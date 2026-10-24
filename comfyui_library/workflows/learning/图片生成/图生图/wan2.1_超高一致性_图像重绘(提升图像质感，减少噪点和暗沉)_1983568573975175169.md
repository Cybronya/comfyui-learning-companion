---
key: 图片生成/图生图/wan2.1_超高一致性_图像重绘(提升图像质感，减少噪点和暗沉)_1983568573975175169.json
name: wan2.1_超高一致性_图像重绘(提升图像质感，减少噪点和暗沉)_1983568573975175169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.1_超高一致性_图像重绘(提升图像质感，减少噪点和暗沉)_1983568573975175169.json
hash: e9c0e3e22b75d959
coverage: 0.818182
learned_at: 2026-10-23 11:45:49
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageScaleToMaxDimension, ImageScaleToMaxDimension, PreviewImage, PreviewImage, Note, LynxEncodeFaceIP, WanVideoTextEncode, BiRefNetRMBG, AutoCropFaces, Reroute, WanVideoAddLynxEmbeds, Reroute, WanVideoBlockSwap, WanVideoVACEEncode, GetImageSize, WanVideoTextEncode, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, Image Comparer (rgthree), WanVideoSampler, LoadLynxResampler, LoadImage, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, AutoCropFaces, WanVideoDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/wan2.1_超高一致性_图像重绘(提升图像质感，减少噪点和暗沉)_1983568573975175169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.1_超高一致性_图像重绘(提升图像质感，减少噪点和暗沉)_1983568573975175169.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `LynxEncodeFaceIP`
- `WanVideoTextEncode`
- `BiRefNetRMBG`
- `AutoCropFaces`
- `Reroute`
- `WanVideoAddLynxEmbeds`
- `Reroute`
- `WanVideoBlockSwap`
- `WanVideoVACEEncode`
- `GetImageSize`
- `WanVideoTextEncode`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `Image Comparer (rgthree)`
- `WanVideoSampler` ★核心
- `LoadLynxResampler` ★核心
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `AutoCropFaces`
- `WanVideoDecode`
- `SaveImage`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageScaleToMaxDimension`、`LynxEncodeFaceIP`、`WanVideoTextEncode`、`BiRefNetRMBG`、`AutoCropFaces`、`WanVideoAddLynxEmbeds`、`WanVideoBlockSwap`、`WanVideoVACEEncode`、`GetImageSize`、`WanVideoExtraModelSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSampler`、`LoadLynxResampler`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`SaveImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
