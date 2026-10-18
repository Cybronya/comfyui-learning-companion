---
key: 音频生成/音频生成/高精度对口型-latentsync1.5_1904485553994174465.json
name: 高精度对口型-latentsync1.5_1904485553994174465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/高精度对口型-latentsync1.5_1904485553994174465.json
hash: ed02f5ca23e6064e
coverage: 0.627119
learned_at: 2026-10-18 01:24:12
nodes: [VideoLengthAdjuster, MaskToSEGS, SegsToCombinedMask, GroundingDinoModelLoader (segment anything), GrowMask, ImageAndMaskPreview, SetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, MaskPreview+, MaskBoundingBox+, SetNode, ImageScaleBy, GetNode, SetNode, SetNode, SetNode, GetNode, WanVideoTeaCacheKJ, SkipLayerGuidanceWanVideo, GetNode, ModelSamplingSD3, DifferentialDiffusion, KSampler, GetNode, CLIPTextEncode, ImageBlur, InstructPixToPixConditioning, CLIPTextEncode, VHS_VideoCombine, LatentSyncNode, VHS_VideoCombine, SetNode, VAEDecode, ImageCompositeMasked, ImageResizeKJ, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, UNETLoader, CLIPLoader, VAELoader, LoadAudio, LoraLoaderModelOnly, VHS_VideoCombine, SAMLoader, GroundingDinoSAMSegment (segment anything), ImageCrop, GroundingDinoSAMSegment (segment anything), SetNode, GetNode, GrowMaskWithBlur, Reroute, Reroute]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "gradient_estimation", "scheduler": "normal", "seed": 484124163270679, "steps": 30}
---

# 音频生成/音频生成/高精度对口型-latentsync1.5_1904485553994174465.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/高精度对口型-latentsync1.5_1904485553994174465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `VideoLengthAdjuster`
- `MaskToSEGS`
- `SegsToCombinedMask`
- `GroundingDinoModelLoader (segment anything)`
- `GrowMask`
- `ImageAndMaskPreview`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `MaskPreview+`
- `MaskBoundingBox+`
- `SetNode`
- `ImageScaleBy`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoTeaCacheKJ`
- `SkipLayerGuidanceWanVideo`
- `GetNode`
- `ModelSamplingSD3`
- `DifferentialDiffusion`
- `KSampler` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageBlur`
- `InstructPixToPixConditioning`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LatentSyncNode`
- `VHS_VideoCombine`
- `SetNode`
- `VAEDecode` ★核心
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `SAMLoader`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageCrop`
- `GroundingDinoSAMSegment (segment anything)`
- `SetNode`
- `GetNode`
- `GrowMaskWithBlur`
- `Reroute`
- `Reroute`

## 关键参数

- `seed` = `484124163270679`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `gradient_estimation`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **63%**（37/59）

**有卡**：`VideoLengthAdjuster`、`MaskToSEGS`、`SegsToCombinedMask`、`GroundingDinoModelLoader (segment anything)`、`GrowMask`、`ImageAndMaskPreview`、`VHS_VideoCombine`、`MaskPreview+`、`MaskBoundingBox+`、`ImageScaleBy`、`WanVideoTeaCacheKJ`、`SkipLayerGuidanceWanVideo`、`ModelSamplingSD3`、`DifferentialDiffusion`、`KSampler`、`CLIPTextEncode`、`ImageBlur`、`InstructPixToPixConditioning`、`LatentSyncNode`、`VAEDecode`、`ImageCompositeMasked`、`ImageResizeKJ`、`VHS_LoadVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadAudio`、`LoraLoaderModelOnly`、`SAMLoader`、`GroundingDinoSAMSegment (segment anything)`、`ImageCrop`、`GrowMaskWithBlur`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SkipLayerGuidanceWanVideo
