---
key: 图片生成/图生图/minimalist极简主义风格_Kontext-dev_1943852515488071682.json
name: minimalist极简主义风格_Kontext-dev_1943852515488071682
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/minimalist极简主义风格_Kontext-dev_1943852515488071682.json
hash: de7af85779fb8eb0
coverage: 0.875
learned_at: 2026-10-23 11:41:01
nodes: [VAEDecode, KSampler, VAELoader, DualCLIPLoader, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, SaveImage, UNETLoader, ReferenceLatent, ShowText|pysssss, SaveImage, VAEEncode, EmptySD3LatentImage, GetImageSizeAndCount, ImageStitch, FluxKontextImageScale, ImageConcatMulti, PreviewImage, Text Multiline, LoraLoaderModelOnly, LoadImage, ImageScaleDownToSize, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 988290283750979, "steps": 20}
---

# 图片生成/图生图/minimalist极简主义风格_Kontext-dev_1943852515488071682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/minimalist极简主义风格_Kontext-dev_1943852515488071682.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `SaveImage`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `ShowText|pysssss`
- `SaveImage`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `GetImageSizeAndCount`
- `ImageStitch`
- `FluxKontextImageScale`
- `ImageConcatMulti`
- `PreviewImage`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImageScaleDownToSize`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `988290283750979`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAEDecode`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`SaveImage`、`UNETLoader`、`ReferenceLatent`、`VAEEncode`、`EmptySD3LatentImage`、`GetImageSizeAndCount`、`ImageStitch`、`FluxKontextImageScale`、`ImageConcatMulti`、`Text Multiline`、`LoraLoaderModelOnly`、`LoadImage`、`ImageScaleDownToSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
