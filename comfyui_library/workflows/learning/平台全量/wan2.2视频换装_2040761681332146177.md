---
key: 平台全量/wan2.2视频换装_2040761681332146177.json
name: wan2.2视频换装_2040761681332146177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2视频换装_2040761681332146177.json
hash: e0929a40553e4fa5
coverage: 0.716667
learned_at: 2026-11-14 01:19:56
nodes: [WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, INTConstant, VHS_VideoInfo, WanVideoVACEModelSelect, PrimitiveNode, LayerUtility: PurgeVRAM V2, SetNode, SetNode, Note, WanVideoVAELoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModelBatched, GetNode, VHS_VideoCombine, WanVideoSetLoRAs, SetNode, WanVideoSetLoRAs, SetNode, GetNode, Note, MathExpression|pysssss, Note, Int, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM V2, WanVideoDecode, ImageFromBatch+, GetNode, GetNode, GetNode, WanVideoLoraSelect, VHS_VideoCombine, Fast Groups Muter (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerMask: SegformerB2ClothesUltra, GrowMaskWithBlur, InpaintPreprocessor, WanVideoVACEEncode, VHS_VideoCombine, MarkdownNote, Note, GetImageSizeAndCount, RH_Translator, Int, Note, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/wan2.2视频换装_2040761681332146177.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2视频换装_2040761681332146177.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（60 个）：
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
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `Note`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: SegformerB2ClothesUltra`
- `GrowMaskWithBlur`
- `InpaintPreprocessor`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note`
- `GetImageSizeAndCount`
- `RH_Translator`
- `Int`
- `Note`
- `VHS_LoadVideo`

## 知识

覆盖率 **72%**（43/60）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`INTConstant`、`VHS_VideoInfo`、`WanVideoVACEModelSelect`、`LayerUtility: PurgeVRAM V2`、`WanVideoVAELoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`RIFE VFI`、`UpscaleModelLoader`、`ImageUpscaleWithModelBatched`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`MathExpression|pysssss`、`Int`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: SegformerB2ClothesUltra`、`GrowMaskWithBlur`、`InpaintPreprocessor`、`WanVideoVACEEncode`、`RH_Translator`、`VHS_LoadVideo`

**用到的条目**：CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
