---
key: 平台全量/KJ版-wan2.2-Fun-VACE视频生视频 视频扩展 效果很棒_1968470687239286786.json
name: KJ版-wan2.2-Fun-VACE视频生视频 视频扩展 效果很棒_1968470687239286786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/KJ版-wan2.2-Fun-VACE视频生视频 视频扩展 效果很棒_1968470687239286786.json
hash: 92ca63036d425757
coverage: 0.660714
learned_at: 2026-11-14 00:33:16
nodes: [WanVideoVACEModelSelect, WanVideoSetBlockSwap, WanVideoModelLoader, SetNode, INTConstant, INTConstant, SetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, PrimitiveFloat, SetNode, Note, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, GetNode, GetNode, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSampler, GetNode, Reroute, Reroute, easy cleanGpuUsed, WanVideoSampler, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoDecode, GetNode, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVACEModelSelect, WanVideoVACEEncode, GetNode, VHS_DuplicateMasks, GetImageSize, GetImageRangeFromBatch, PreviewImage, PreviewImage, GetNode, ImageConcatMulti, LayerUtility: TextJoin, ImageAndMaskPreview, SetNode, PrimitiveInt, GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, RH_Captioner, RH_Translator, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/KJ版-wan2.2-Fun-VACE视频生视频 视频扩展 效果很棒_1968470687239286786.json

> 来源文件 `comfyui_library/workflows/平台全量/KJ版-wan2.2-Fun-VACE视频生视频 视频扩展 效果很棒_1968470687239286786.json`

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
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `RH_Captioner`
- `RH_Translator`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **66%**（37/56）

**有卡**：`WanVideoVACEModelSelect`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`INTConstant`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`WanVideoVACEEncode`、`VHS_DuplicateMasks`、`GetImageSize`、`GetImageRangeFromBatch`、`ImageConcatMulti`、`LayerUtility: TextJoin`、`ImageAndMaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImagePadForOutpaint`、`RH_Captioner`、`RH_Translator`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
