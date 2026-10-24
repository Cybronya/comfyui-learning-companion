---
key: 图片生成/图生图/景深 - 图生图 - F.1_1900235357496012801.json
name: 景深 - 图生图 - F.1_1900235357496012801
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/景深 - 图生图 - F.1_1900235357496012801.json
hash: e897e3bed9683c6d
coverage: 0.870968
learned_at: 2026-10-23 13:05:01
nodes: [UltralyticsDetectorProvider, SAMLoader, FaceDetailer, ImageNoiseAugmentation, CLIPTextEncode, ImageColorMatch+, SaveImage, PreviewImage, Image Comparer (rgthree), Image Filter Adjustments, SaveImage, VAELoader, Joy_caption_two_load, CLIPTextEncodeFlux, DualCLIPLoader, Joy_caption_two, ConstrainImage|pysssss, LoadImage, PreviewImage, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, InspyrenetRembg, InvertMask, ImageCompositeMasked, PreviewImage, VAEEncode, RepeatLatentBatch, VAEDecode, KSampler, FloatSlider]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.85, "sampler_name": "deis", "scheduler": "beta", "seed": 702656852989553, "steps": 35}
---

# 图片生成/图生图/景深 - 图生图 - F.1_1900235357496012801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/景深 - 图生图 - F.1_1900235357496012801.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `FaceDetailer`
- `ImageNoiseAugmentation`
- `CLIPTextEncode` ★核心
- `ImageColorMatch+`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `SaveImage`
- `VAELoader`
- `Joy_caption_two_load`
- `CLIPTextEncodeFlux` ★核心
- `DualCLIPLoader`
- `Joy_caption_two`
- `ConstrainImage|pysssss`
- `LoadImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `InspyrenetRembg`
- `InvertMask`
- `ImageCompositeMasked`
- `PreviewImage`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `FloatSlider`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `702656852989553`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `0.85`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`UltralyticsDetectorProvider`、`SAMLoader`、`FaceDetailer`、`ImageNoiseAugmentation`、`CLIPTextEncode`、`ImageColorMatch+`、`SaveImage`、`Image Filter Adjustments`、`VAELoader`、`Joy_caption_two_load`、`CLIPTextEncodeFlux`、`DualCLIPLoader`、`Joy_caption_two`、`ConstrainImage|pysssss`、`LoadImage`、`ConditioningZeroOut`、`UNETLoader`、`LoraLoaderModelOnly`、`InspyrenetRembg`、`InvertMask`、`ImageCompositeMasked`、`VAEEncode`、`RepeatLatentBatch`、`VAEDecode`、`KSampler`、`FloatSlider`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
