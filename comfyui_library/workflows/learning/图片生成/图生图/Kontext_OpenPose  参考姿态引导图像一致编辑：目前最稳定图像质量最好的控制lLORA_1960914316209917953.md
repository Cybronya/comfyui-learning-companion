---
key: 图片生成/图生图/Kontext_OpenPose  参考姿态引导图像一致编辑：目前最稳定图像质量最好的控制lLORA_1960914316209917953.json
name: Kontext_OpenPose  参考姿态引导图像一致编辑：目前最稳定图像质量最好的控制lLORA_1960914316209917953
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext_OpenPose  参考姿态引导图像一致编辑：目前最稳定图像质量最好的控制lLORA_1960914316209917953.json
hash: 5f41e01c80f521db
coverage: 0.92
learned_at: 2026-10-23 11:06:50
nodes: [VAELoader, GetImageSizeAndCount, GetImageSizeAndCount, UNETLoader, ImageScaleDownToSize, ImageScaleDownToSize, FluxGuidance, ConditioningZeroOut, VAEDecode, DualCLIPLoader, ImageStitch, AIO_Preprocessor, ReferenceLatent, VAEEncode, CLIPTextEncode, LoraLoaderModelOnly, ImageCrop, LoadImage, LoadImage, Text Multiline, KSampler, SaveImage, ImageConcatMulti, PreviewImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1076161270252148, "steps": 20}
---

# 图片生成/图生图/Kontext_OpenPose  参考姿态引导图像一致编辑：目前最稳定图像质量最好的控制lLORA_1960914316209917953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext_OpenPose  参考姿态引导图像一致编辑：目前最稳定图像质量最好的控制lLORA_1960914316209917953.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `VAELoader`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `UNETLoader` ★核心
- `ImageScaleDownToSize`
- `ImageScaleDownToSize`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `ImageStitch`
- `AIO_Preprocessor`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageCrop`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `KSampler` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `PreviewImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1076161270252148`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`VAELoader`、`GetImageSizeAndCount`、`UNETLoader`、`ImageScaleDownToSize`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`DualCLIPLoader`、`ImageStitch`、`AIO_Preprocessor`、`ReferenceLatent`、`VAEEncode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ImageCrop`、`LoadImage`、`Text Multiline`、`KSampler`、`SaveImage`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
