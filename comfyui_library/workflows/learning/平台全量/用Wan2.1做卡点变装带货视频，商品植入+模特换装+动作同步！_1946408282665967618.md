---
key: 平台全量/用Wan2.1做卡点变装带货视频，商品植入+模特换装+动作同步！_1946408282665967618.json
name: 用Wan2.1做卡点变装带货视频，商品植入+模特换装+动作同步！_1946408282665967618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/用Wan2.1做卡点变装带货视频，商品植入+模特换装+动作同步！_1946408282665967618.json
hash: ceb3c3ecf9637a2e
coverage: 0.975309
learned_at: 2026-11-14 02:22:20
nodes: [CLIPLoader, VAELoader, KSampler, TrimVideoLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, GetImageRangeFromBatch, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, WanVideoVACEStartToEndFrame, WanVaceToVideo, VAEDecode, KSampler, AIO_Preprocessor, TrimVideoLatent, CLIPLoader, VAELoader, KSampler, TrimVideoLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, CLIPTextEncode, GetImageRangeFromBatch, UNETLoader, MaskRepeatBatch, RepeatImageBatch, preview_mask, WanVaceToVideo, Mix Color By Mask, MaskToImage, LoadImage, LayerMask: LoadSegmentAnythingModels, LoadImage, PreviewImage, GrowMaskWithBlur, MaskToImage, GrowMaskWithBlur, Mix Color By Mask, MaskRepeatBatch, RepeatImageBatch, CLIPTextEncode, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, CLIPTextEncode, WanVideoVACEStartToEndFrame, LoadImage, WanVaceToVideo, TrimVideoLatent, KSampler, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVaceToVideo, LoadImage, CLIPTextEncode, SaveImage, LayerMask: SegmentAnythingUltra V3, PreviewImage, SaveImage, CLIPTextEncode, VHS_VideoCombine, VHS_LoadVideo, CLIPTextEncode, VHS_LoadVideo, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/用Wan2.1做卡点变装带货视频，商品植入+模特换装+动作同步！_1946408282665967618.json

> 来源文件 `comfyui_library/workflows/平台全量/用Wan2.1做卡点变装带货视频，商品植入+模特换装+动作同步！_1946408282665967618.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `TrimVideoLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `GetImageRangeFromBatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `WanVaceToVideo`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `AIO_Preprocessor`
- `TrimVideoLatent`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `TrimVideoLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageRangeFromBatch`
- `UNETLoader` ★核心
- `MaskRepeatBatch`
- `RepeatImageBatch`
- `preview_mask`
- `WanVaceToVideo`
- `Mix Color By Mask`
- `MaskToImage`
- `LoadImage`
- `LayerMask: LoadSegmentAnythingModels`
- `LoadImage`
- `PreviewImage`
- `GrowMaskWithBlur`
- `MaskToImage`
- `GrowMaskWithBlur`
- `Mix Color By Mask`
- `MaskRepeatBatch`
- `RepeatImageBatch`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `LoadImage`
- `WanVaceToVideo`
- `TrimVideoLatent`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVaceToVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LayerMask: SegmentAnythingUltra V3`
- `PreviewImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `666`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **98%**（79/81）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`TrimVideoLatent`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`GetImageRangeFromBatch`、`WanVideoVACEStartToEndFrame`、`WanVaceToVideo`、`AIO_Preprocessor`、`MaskRepeatBatch`、`RepeatImageBatch`、`preview_mask`、`Mix Color By Mask`、`MaskToImage`、`LoadImage`、`LayerMask: LoadSegmentAnythingModels`、`GrowMaskWithBlur`、`VHS_VideoCombine`、`SaveImage`、`LayerMask: SegmentAnythingUltra V3`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
