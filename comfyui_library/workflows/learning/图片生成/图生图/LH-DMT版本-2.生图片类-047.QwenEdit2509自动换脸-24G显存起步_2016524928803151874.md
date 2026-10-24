---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-047.QwenEdit2509自动换脸-24G显存起步_2016524928803151874.json
name: LH-DMT版本-2.生图片类-047.QwenEdit2509自动换脸-24G显存起步_2016524928803151874
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-047.QwenEdit2509自动换脸-24G显存起步_2016524928803151874.json
hash: 0ee455f719a1ce80
coverage: 0.641026
learned_at: 2026-10-23 11:08:41
nodes: [PreviewImage, AutoCropFaces, LayerMask: PersonMaskUltra V2, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, CLIPLoader, Reroute, Reroute, InpaintModelConditioning, Reroute, VAELoader, VAEEncode, ConditioningZeroOut, KSampler, QwenImageDiffsynthControlnet, ImageStitch, ImageStitch, PreviewImage, Image Comparer (rgthree), CheckpointLoaderSimple, Reroute, Reroute, Reroute, LayerMask: MaskGrow, Note, Note, VAEDecode, SaveImage, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, UnetLoaderGGUF, LoraLoaderModelOnly, LoadImage, LoadImage, ModelPatchLoader, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v10.4.safetensors", "denoise": 0.6, "sampler_name": "euler", "scheduler": "simple", "seed": 8848, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-047.QwenEdit2509自动换脸-24G显存起步_2016524928803151874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-047.QwenEdit2509自动换脸-24G显存起步_2016524928803151874.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `PreviewImage`
- `AutoCropFaces`
- `LayerMask: PersonMaskUltra V2`
- `MaskPreview+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `InpaintModelConditioning`
- `Reroute`
- `VAELoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `QwenImageDiffsynthControlnet`
- `ImageStitch`
- `ImageStitch`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerMask: MaskGrow`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `ModelPatchLoader`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `8848`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v10.4.safetensors`

## 知识

覆盖率 **64%**（25/39）

**有卡**：`AutoCropFaces`、`LayerMask: PersonMaskUltra V2`、`MaskPreview+`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`InpaintModelConditioning`、`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`KSampler`、`QwenImageDiffsynthControlnet`、`ImageStitch`、`CheckpointLoaderSimple`、`LayerMask: MaskGrow`、`VAEDecode`、`SaveImage`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`LoadImage`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
