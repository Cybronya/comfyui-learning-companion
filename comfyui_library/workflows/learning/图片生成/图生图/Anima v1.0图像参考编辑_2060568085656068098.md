---
key: 图片生成/图生图/Anima v1.0图像参考编辑_2060568085656068098.json
name: Anima v1.0图像参考编辑_2060568085656068098
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima v1.0图像参考编辑_2060568085656068098.json
hash: 3c03973ee700f995
coverage: 0.757576
learned_at: 2026-10-23 10:51:07
nodes: [UNETLoader, VAELoader, CLIPLoader, AILab_ICLoRAConcat, GrowMaskWithBlur, ComfySwitchNode, ComfySwitchNode, StringReplace, AnimaLLLiteApply, SetLatentNoiseMask, VAEEncode, PrimitiveBoundingBox, VAEDecode, ImageCropV2, PrimitiveBoolean, SaveImage, ComfySwitchNode, KSampler, ImageResizeKJv2, Note, Text, LoadImage, JWInteger, Note, PrimitiveStringMultiline, MaskPreview, CLIPTextEncode, PreviewImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, ComfySwitchNode, SaveImage, ImageConcanate]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4.5, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 443247086103961, "steps": 20}
---

# 图片生成/图生图/Anima v1.0图像参考编辑_2060568085656068098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima v1.0图像参考编辑_2060568085656068098.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `AILab_ICLoRAConcat`
- `GrowMaskWithBlur`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `StringReplace`
- `AnimaLLLiteApply`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `PrimitiveBoundingBox`
- `VAEDecode` ★核心
- `ImageCropV2`
- `PrimitiveBoolean`
- `SaveImage`
- `ComfySwitchNode`
- `KSampler` ★核心
- `ImageResizeKJv2`
- `Note`
- `Text`
- `LoadImage`
- `JWInteger`
- `Note`
- `PrimitiveStringMultiline`
- `MaskPreview`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ComfySwitchNode`
- `SaveImage`
- `ImageConcanate`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `443247086103961`
- `steps` = `20`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`AILab_ICLoRAConcat`、`GrowMaskWithBlur`、`StringReplace`、`AnimaLLLiteApply`、`SetLatentNoiseMask`、`VAEEncode`、`PrimitiveBoundingBox`、`VAEDecode`、`ImageCropV2`、`PrimitiveBoolean`、`SaveImage`、`KSampler`、`ImageResizeKJv2`、`Text`、`LoadImage`、`JWInteger`、`MaskPreview`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
