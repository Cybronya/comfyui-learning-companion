---
key: 图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json
name: Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json
hash: aac8c8afb61a2ecb
coverage: 0.924528
learned_at: 2026-10-23 11:27:55
nodes: [CLIPLoader, VAELoader, KSampler, TrimVideoLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, AIO_Preprocessor, AIO_Preprocessor, SaveImage, PreviewImage, SaveImage, PreviewImage, AIO_Preprocessor, SaveImage, PreviewImage, VAEDecode, CLIPLoader, UNETLoader, VAELoader, TrimVideoLatent, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, WanVaceToVideo, KSampler, CLIPTextEncode, LoadImage, CLIPTextEncode, GetImageRangeFromBatch, WanVaceToVideo, UNETLoader, MaskRepeatBatch, GetImageRangeFromBatch, RepeatImageBatch, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, MaskToImage, PreviewImage, GrowMaskWithBlur, RepeatImageBatch, LoadImage, LoadImage, SaveImage, LoadImage, CLIPTextEncode, LoadImage, CLIPTextEncode, SaveImage, LoraLoaderModelOnly, preview_mask, Mix Color By Mask, Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1高阶玩法，电商模特姿势任意摆&衣服随心换_1946080152214532098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `TrimVideoLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `TrimVideoLatent`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `WanVaceToVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `GetImageRangeFromBatch`
- `WanVaceToVideo`
- `UNETLoader` ★核心
- `MaskRepeatBatch`
- `GetImageRangeFromBatch`
- `RepeatImageBatch`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `MaskToImage`
- `PreviewImage`
- `GrowMaskWithBlur`
- `RepeatImageBatch`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `preview_mask`
- `Mix Color By Mask`
- `Label (rgthree)`

## 关键参数

- `seed` = `666`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（49/53）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`TrimVideoLatent`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`AIO_Preprocessor`、`SaveImage`、`VAEDecode`、`UNETLoader`、`WanVaceToVideo`、`CLIPTextEncode`、`LoadImage`、`GetImageRangeFromBatch`、`MaskRepeatBatch`、`RepeatImageBatch`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`MaskToImage`、`GrowMaskWithBlur`、`preview_mask`、`Mix Color By Mask`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
