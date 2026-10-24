---
key: 图片生成/图生图/FireRed Edit  1.1最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2029890668960681985.json
name: FireRed Edit  1.1最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2029890668960681985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Edit  1.1最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2029890668960681985.json
hash: 5155e5eaf0d001e4
coverage: 0.703704
learned_at: 2026-10-23 10:55:24
nodes: [SDPoseOODLoader, SDPoseOODProcessor, PreviewImage, easy ifElse, MaskToImage, SetNode, PreviewImage, PreviewImage, Mask Fill Holes, PreviewImage, DrawMaskOnImage, MaskPreview+, ClothesSegment, easy isMaskEmpty, GetNode, CR Prompt Text, Florence2Run, PreviewImage, PreviewImage, ToBinaryMask, BlockifyMask, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, GetImageSize+, EmptyLatentImage, SeedVR2LoadDiTModel, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SeedVR2VideoUpscaler, PreviewImage, SaveImage, LayerUtility: ImageBlend, Florence2ModelLoader, YOLOModelLoader, PreviewImage, Note, SaveImage, SeedVR2LoadVAEModel, Note, SaveImage, Fast Groups Muter (rgthree), LoadImage, RMBG, PreviewImage, MaskPreview+, Sa2VANodeTpl, LoadImage, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 820502896282807, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed Edit  1.1最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2029890668960681985.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Edit  1.1最强人物替换（适合二创）---不偏色，无偏移，平替全能图片V1_2029890668960681985.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `PreviewImage`
- `easy ifElse`
- `MaskToImage`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `Mask Fill Holes`
- `PreviewImage`
- `DrawMaskOnImage`
- `MaskPreview+`
- `ClothesSegment`
- `easy isMaskEmpty`
- `GetNode`
- `CR Prompt Text`
- `Florence2Run`
- `PreviewImage`
- `PreviewImage`
- `ToBinaryMask`
- `BlockifyMask`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `SeedVR2LoadDiTModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SaveImage`
- `LayerUtility: ImageBlend`
- `Florence2ModelLoader`
- `YOLOModelLoader`
- `PreviewImage`
- `Note`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `Note`
- `SaveImage`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `RMBG`
- `PreviewImage`
- `MaskPreview+`
- `Sa2VANodeTpl`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `820502896282807`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **70%**（38/54）

**有卡**：`SDPoseOODLoader`、`SDPoseOODProcessor`、`MaskToImage`、`Mask Fill Holes`、`DrawMaskOnImage`、`MaskPreview+`、`ClothesSegment`、`easy isMaskEmpty`、`CR Prompt Text`、`Florence2Run`、`ToBinaryMask`、`BlockifyMask`、`TextEncodeQwenImageEditPlus`、`GetImageSize+`、`EmptyLatentImage`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SaveImage`、`LayerUtility: ImageBlend`、`Florence2ModelLoader`、`YOLOModelLoader`、`SeedVR2LoadVAEModel`、`LoadImage`、`RMBG`、`Sa2VANodeTpl`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
