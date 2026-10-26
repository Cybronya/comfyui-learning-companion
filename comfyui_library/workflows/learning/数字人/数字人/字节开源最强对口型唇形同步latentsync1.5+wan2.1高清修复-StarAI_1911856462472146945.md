---
key: 数字人/数字人/字节开源最强对口型唇形同步latentsync1.5+wan2.1高清修复-StarAI_1911856462472146945.json
name: 字节开源最强对口型唇形同步latentsync1.5+wan2.1高清修复-StarAI_1911856462472146945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/字节开源最强对口型唇形同步latentsync1.5+wan2.1高清修复-StarAI_1911856462472146945.json
hash: 524012e765614e60
coverage: 0.693333
learned_at: 2026-10-26 02:01:34
nodes: [MaskPreview+, DF_Int_to_Float, SimpleMath+, easy float, GetNode, CLIPLoader, VAELoader, LoraLoaderModelOnly, WanVideoTeaCacheKJ, SkipLayerGuidanceWanVideo, UNETLoader, DownloadAndLoadFlorence2Model, ImageFromBatch+, Florence2Run, GroundingDinoModelLoader (segment anything), GrowMask, ImageAndMaskPreview, MaskBoundingBox+, ImageScaleBy, Note, SimpleMath+, Audio Cut (mtb), VideoLengthAdjuster, VHS_VideoCombine, GroundingDinoSAMSegment (segment anything), MaskToSEGS, GroundingDinoSAMSegment (segment anything), SAMLoader, SegsToCombinedMask, VHS_VideoCombine, ModelSamplingSD3, DifferentialDiffusion, InstructPixToPixConditioning, KSampler, CLIPTextEncode, CLIPTextEncode, Note Plus (mtb), LayerUtility: PurgeVRAM V2, VAEDecode, ShowText|pysssss, ImageBlur, LayerUtility: PurgeVRAM V2, ImageResizeKJ, VHS_VideoCombine, GrowMaskWithBlur, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageCompositeMasked, LayerUtility: PurgeVRAM V2, VHS_LoadVideo, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LatentSyncNode, VHS_VideoCombine, ImageCrop, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM V2, SetNode, SetNode, SetNode, SetNode, SetNode, easy int, easy int, LoadAudio]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "gradient_estimation", "scheduler": "normal", "seed": 484124163270679, "steps": 20}
---

# 数字人/数字人/字节开源最强对口型唇形同步latentsync1.5+wan2.1高清修复-StarAI_1911856462472146945.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/字节开源最强对口型唇形同步latentsync1.5+wan2.1高清修复-StarAI_1911856462472146945.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（75 个）：
- `MaskPreview+`
- `DF_Int_to_Float`
- `SimpleMath+`
- `easy float`
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `WanVideoTeaCacheKJ`
- `SkipLayerGuidanceWanVideo`
- `UNETLoader` ★核心
- `DownloadAndLoadFlorence2Model`
- `ImageFromBatch+`
- `Florence2Run`
- `GroundingDinoModelLoader (segment anything)`
- `GrowMask`
- `ImageAndMaskPreview`
- `MaskBoundingBox+`
- `ImageScaleBy`
- `Note`
- `SimpleMath+`
- `Audio Cut (mtb)`
- `VideoLengthAdjuster`
- `VHS_VideoCombine`
- `GroundingDinoSAMSegment (segment anything)`
- `MaskToSEGS`
- `GroundingDinoSAMSegment (segment anything)`
- `SAMLoader`
- `SegsToCombinedMask`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `DifferentialDiffusion`
- `InstructPixToPixConditioning`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `ImageBlur`
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageCompositeMasked`
- `LayerUtility: PurgeVRAM V2`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LatentSyncNode`
- `VHS_VideoCombine`
- `ImageCrop`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `easy int`
- `LoadAudio`

## 关键参数

- `seed` = `484124163270679`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `gradient_estimation`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **69%**（52/75）

**有卡**：`MaskPreview+`、`DF_Int_to_Float`、`SimpleMath+`、`easy float`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`WanVideoTeaCacheKJ`、`SkipLayerGuidanceWanVideo`、`UNETLoader`、`DownloadAndLoadFlorence2Model`、`ImageFromBatch+`、`Florence2Run`、`GroundingDinoModelLoader (segment anything)`、`GrowMask`、`ImageAndMaskPreview`、`MaskBoundingBox+`、`ImageScaleBy`、`Audio Cut (mtb)`、`VideoLengthAdjuster`、`VHS_VideoCombine`、`GroundingDinoSAMSegment (segment anything)`、`MaskToSEGS`、`SAMLoader`、`SegsToCombinedMask`、`ModelSamplingSD3`、`DifferentialDiffusion`、`InstructPixToPixConditioning`、`KSampler`、`CLIPTextEncode`、`Note Plus (mtb)`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`ImageBlur`、`ImageResizeKJ`、`GrowMaskWithBlur`、`ImageCompositeMasked`、`VHS_LoadVideo`、`LatentSyncNode`、`ImageCrop`、`easy int`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SkipLayerGuidanceWanVideo
