---
key: 图片生成/图生图/nunchaku-qwen-image-edit-双图_1966064348844167170.json
name: nunchaku-qwen-image-edit-双图_1966064348844167170
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-qwen-image-edit-双图_1966064348844167170.json
hash: 5cd7059b7a6a31e9
coverage: 0.956522
learned_at: 2026-10-23 11:41:21
nodes: [Preview from image [Crystools], VAEEncode, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, Anything Everywhere3, easy clearCacheAll, CFGNorm, ModelSamplingAuraFlow, easy clearCacheAll, VAEDecode, KSampler, SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, NunchakuQwenImageDiTLoader, CLIPLoader, VAELoader, ImageStitch, LayerUtility: ImageScaleByAspectRatio V2, RMBG, LoadImage, RBGImageStitchPlus, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 898989119515, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/nunchaku-qwen-image-edit-双图_1966064348844167170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-qwen-image-edit-双图_1966064348844167170.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Preview from image [Crystools]`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `Anything Everywhere3`
- `easy clearCacheAll`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `NunchakuQwenImageDiTLoader`
- `CLIPLoader`
- `VAELoader`
- `ImageStitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `LoadImage`
- `RBGImageStitchPlus`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `898989119515`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`Preview from image [Crystools]`、`VAEEncode`、`TextEncodeQwenImageEdit`、`easy clearCacheAll`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`VAELoader`、`ImageStitch`、`RMBG`、`RBGImageStitchPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
