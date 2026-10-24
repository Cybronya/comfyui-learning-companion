---
key: 图片生成/图生图/Qwen-image-Edit-2511 图像多角度控制生成 V1.0_2010632419312934913.json
name: Qwen-image-Edit-2511 图像多角度控制生成 V1.0_2010632419312934913
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-Edit-2511 图像多角度控制生成 V1.0_2010632419312934913.json
hash: 50727655bfb01c70
coverage: 0.896552
learned_at: 2026-10-23 11:18:03
nodes: [KSampler, VAEDecode, CFGNorm, ModelSamplingAuraFlow, Note, SaveImage, Note Plus (mtb), Note Plus (mtb), Note, FluxKontextMultiReferenceLatentMethod, easy promptList, LoadImage, VNCCS_VisualPositionControl, VNCCS_VisualPositionControl, VNCCS_VisualPositionControl, VNCCS_VisualPositionControl, VNCCS_VisualPositionControl, UNETLoader, CLIPLoader, VAELoader, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus, VAEEncode, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, Power Lora Loader (rgthree), easy showAnything, Label (rgthree), Label (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image-Edit-2511 图像多角度控制生成 V1.0_2010632419312934913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-Edit-2511 图像多角度控制生成 V1.0_2010632419312934913.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `Note`
- `SaveImage`
- `Note Plus (mtb)`
- `Note Plus (mtb)`
- `Note`
- `FluxKontextMultiReferenceLatentMethod`
- `easy promptList`
- `LoadImage`
- `VNCCS_VisualPositionControl`
- `VNCCS_VisualPositionControl`
- `VNCCS_VisualPositionControl`
- `VNCCS_VisualPositionControl`
- `VNCCS_VisualPositionControl`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `Power Lora Loader (rgthree)`
- `easy showAnything`
- `Label (rgthree)`
- `Label (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1002`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`KSampler`、`VAEDecode`、`CFGNorm`、`ModelSamplingAuraFlow`、`SaveImage`、`Note Plus (mtb)`、`FluxKontextMultiReferenceLatentMethod`、`easy promptList`、`LoadImage`、`VNCCS_VisualPositionControl`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ImageScaleToTotalPixels`、`Power Lora Loader (rgthree)`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、LoadImage、CFGNorm、FluxKontextMultiReferenceLatentMethod

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
