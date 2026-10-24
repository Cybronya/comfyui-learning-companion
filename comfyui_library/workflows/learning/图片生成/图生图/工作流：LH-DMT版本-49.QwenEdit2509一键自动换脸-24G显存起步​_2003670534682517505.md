---
key: 图片生成/图生图/工作流：LH-DMT版本-49.QwenEdit2509一键自动换脸-24G显存起步​_2003670534682517505.json
name: 工作流：LH-DMT版本-49.QwenEdit2509一键自动换脸-24G显存起步​_2003670534682517505
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/工作流：LH-DMT版本-49.QwenEdit2509一键自动换脸-24G显存起步​_2003670534682517505.json
hash: f662f7f15288af05
coverage: 0.641026
learned_at: 2026-10-23 12:50:38
nodes: [PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, AutoCropFaces, LayerMask: PersonMaskUltra V2, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, UnetLoaderGGUF, TextEncodeQwenImageEditPlus, CLIPLoader, Reroute, Reroute, InpaintModelConditioning, Reroute, VAELoader, VAEEncode, ConditioningZeroOut, LoraLoaderModelOnly, KSampler, QwenImageDiffsynthControlnet, ImageStitch, ImageStitch, PreviewImage, Image Comparer (rgthree), LayerMask: MaskGrow, Note, Note, VAEDecode, SaveImage, LoadImage, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, CheckpointLoaderSimple, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-SFW-v11.safetensors", "denoise": 0.6, "sampler_name": "euler", "scheduler": "simple", "seed": 8848, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/工作流：LH-DMT版本-49.QwenEdit2509一键自动换脸-24G显存起步​_2003670534682517505.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/工作流：LH-DMT版本-49.QwenEdit2509一键自动换脸-24G显存起步​_2003670534682517505.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AutoCropFaces`
- `LayerMask: PersonMaskUltra V2`
- `MaskPreview+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UnetLoaderGGUF` ★核心
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `InpaintModelConditioning`
- `Reroute`
- `VAELoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `QwenImageDiffsynthControlnet`
- `ImageStitch`
- `ImageStitch`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerMask: MaskGrow`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `8848`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6`
- `checkpoint` = `Qwen-Rapid-AIO-SFW-v11.safetensors`

## 知识

覆盖率 **64%**（25/39）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`AutoCropFaces`、`LayerMask: PersonMaskUltra V2`、`MaskPreview+`、`UnetLoaderGGUF`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`InpaintModelConditioning`、`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`KSampler`、`QwenImageDiffsynthControlnet`、`ImageStitch`、`LayerMask: MaskGrow`、`VAEDecode`、`SaveImage`、`LoadImage`、`ModelPatchLoader`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
