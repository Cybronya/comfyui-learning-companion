---
key: 图片生成/图生图/景深 - 图生图 - 控制 - F.1_1900753740746629122.json
name: 景深 - 图生图 - 控制 - F.1_1900753740746629122
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/景深 - 图生图 - 控制 - F.1_1900753740746629122.json
hash: 51a33c0952c5abef
coverage: 0.90625
learned_at: 2026-10-23 13:05:01
nodes: [Joy_caption_two_load, InspyrenetRembg, InvertMask, ImageCompositeMasked, VAEEncode, easy cleanGpuUsed, KSampler, ControlNetApplyAdvanced, CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Joy_caption_two, DWPreprocessor, UNETLoader, LoadImage, ConstrainImage|pysssss, Image Filter Adjustments, PreviewImage, PreviewImage, ImageNoiseAugmentation, FloatSlider, VAEDecode, easy cleanGpuUsed, VAELoader, PreviewImage, ControlNetLoader, SetShakkerLabsUnionControlNetType, easy cleanGpuUsed, SaveImage, RepeatLatentBatch, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 0.85, "sampler_name": "deis", "scheduler": "beta", "seed": 419428415876655, "steps": 35}
---

# 图片生成/图生图/景深 - 图生图 - 控制 - F.1_1900753740746629122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/景深 - 图生图 - 控制 - F.1_1900753740746629122.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `Joy_caption_two_load`
- `InspyrenetRembg`
- `InvertMask`
- `ImageCompositeMasked`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncodeFlux` ★核心
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Joy_caption_two`
- `DWPreprocessor`
- `UNETLoader` ★核心
- `LoadImage`
- `ConstrainImage|pysssss`
- `Image Filter Adjustments`
- `PreviewImage`
- `PreviewImage`
- `ImageNoiseAugmentation`
- `FloatSlider`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAELoader`
- `PreviewImage`
- `ControlNetLoader`
- `SetShakkerLabsUnionControlNetType`
- `easy cleanGpuUsed`
- `SaveImage`
- `RepeatLatentBatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `419428415876655`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `0.85`
- `controlnet_strength` = `0.7000000000000001`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`Joy_caption_two_load`、`InspyrenetRembg`、`InvertMask`、`ImageCompositeMasked`、`VAEEncode`、`easy cleanGpuUsed`、`KSampler`、`ControlNetApplyAdvanced`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`DualCLIPLoader`、`Joy_caption_two`、`DWPreprocessor`、`UNETLoader`、`LoadImage`、`ConstrainImage|pysssss`、`Image Filter Adjustments`、`ImageNoiseAugmentation`、`FloatSlider`、`VAEDecode`、`VAELoader`、`ControlNetLoader`、`SetShakkerLabsUnionControlNetType`、`SaveImage`、`RepeatLatentBatch`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced
