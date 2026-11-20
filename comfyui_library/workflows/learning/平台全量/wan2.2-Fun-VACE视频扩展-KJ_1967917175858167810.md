---
key: 平台全量/wan2.2-Fun-VACE视频扩展-KJ_1967917175858167810.json
name: wan2.2-Fun-VACE视频扩展-KJ_1967917175858167810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-Fun-VACE视频扩展-KJ_1967917175858167810.json
hash: 49029259a2446cc0
coverage: 0.660714
learned_at: 2026-11-14 01:19:29
nodes: [WanVideoVACEModelSelect, WanVideoSetBlockSwap, WanVideoModelLoader, SetNode, INTConstant, INTConstant, SetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, PrimitiveFloat, SetNode, Note, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, VHS_VideoCombine, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSampler, GetNode, Reroute, Reroute, easy cleanGpuUsed, WanVideoSampler, WanVideoSetLoRAs, easy cleanGpuUsed, VHS_VideoCombine, WanVideoDecode, GetNode, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVACEModelSelect, WanVideoVACEEncode, GetNode, VHS_DuplicateMasks, GetImageSize, GetImageRangeFromBatch, PreviewImage, PreviewImage, GetNode, ImageConcatMulti, LayerUtility: TextJoin, ImageAndMaskPreview, SetNode, PrimitiveInt, VHS_LoadVideo, GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, RH_Captioner, RH_Translator]
patterns: []
missing: []
---

# 平台全量/wan2.2-Fun-VACE视频扩展-KJ_1967917175858167810.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-Fun-VACE视频扩展-KJ_1967917175858167810.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（56 个）：
- `WanVideoVACEModelSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `PrimitiveFloat`
- `SetNode`
- `Note`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `GetNode`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `GetNode`
- `VHS_DuplicateMasks`
- `GetImageSize`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `ImageConcatMulti`
- `LayerUtility: TextJoin`
- `ImageAndMaskPreview`
- `SetNode`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `RH_Captioner`
- `RH_Translator`

## 知识

覆盖率 **66%**（37/56）

**有卡**：`WanVideoVACEModelSelect`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`INTConstant`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`WanVideoVACEEncode`、`VHS_DuplicateMasks`、`GetImageSize`、`GetImageRangeFromBatch`、`ImageConcatMulti`、`LayerUtility: TextJoin`、`ImageAndMaskPreview`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImagePadForOutpaint`、`RH_Captioner`、`RH_Translator`

**用到的条目**：CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
