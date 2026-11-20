---
key: 平台全量/wan2.2视频换背景_1957367973776388098.json
name: wan2.2视频换背景_1957367973776388098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2视频换背景_1957367973776388098.json
hash: 0444424df1013ac3
coverage: 0.728571
learned_at: 2026-11-14 01:19:53
nodes: [WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, INTConstant, VHS_VideoInfo, WanVideoVACEModelSelect, PrimitiveNode, ImageFromBatch, RH_Translator, LayerUtility: PurgeVRAM V2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, LayerMask: SAM2VideoUltra, GrowMask, INPAINT_MaskedFill, MaskToImage, GetNode, VHS_VideoCombine, VHS_VideoCombine, Note, WanVideoVAELoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, Note, Note, RH_Translator, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModelBatched, GetNode, VHS_VideoCombine, WanVideoSetLoRAs, SetNode, WanVideoSetLoRAs, SetNode, GetNode, Note, MathExpression|pysssss, Note, Int, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM V2, WanVideoDecode, ImageFromBatch+, GetNode, GetNode, GetNode, WanVideoLoraSelect, VHS_VideoCombine, Fast Groups Muter (rgthree), VHS_LoadVideo, MarkdownNote, GetImageSizeAndCount, Note, Int]
patterns: []
missing: []
---

# 平台全量/wan2.2视频换背景_1957367973776388098.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2视频换背景_1957367973776388098.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（70 个）：
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `VHS_VideoInfo`
- `WanVideoVACEModelSelect`
- `PrimitiveNode`
- `ImageFromBatch`
- `RH_Translator`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2VideoUltra`
- `GrowMask`
- `INPAINT_MaskedFill`
- `MaskToImage`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `RH_Translator`
- `RIFE VFI`
- `UpscaleModelLoader`
- `ImageUpscaleWithModelBatched`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `Note`
- `MathExpression|pysssss`
- `Note`
- `Int`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `VHS_LoadVideo`
- `MarkdownNote`
- `GetImageSizeAndCount`
- `Note`
- `Int`

## 知识

覆盖率 **73%**（51/70）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`INTConstant`、`VHS_VideoInfo`、`WanVideoVACEModelSelect`、`ImageFromBatch`、`RH_Translator`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`LayerMask: SAM2Ultra`、`LayerMask: SAM2VideoUltra`、`GrowMask`、`INPAINT_MaskedFill`、`MaskToImage`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`RIFE VFI`、`UpscaleModelLoader`、`ImageUpscaleWithModelBatched`、`WanVideoSetLoRAs`、`MathExpression|pysssss`、`Int`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`VHS_LoadVideo`

**用到的条目**：CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
