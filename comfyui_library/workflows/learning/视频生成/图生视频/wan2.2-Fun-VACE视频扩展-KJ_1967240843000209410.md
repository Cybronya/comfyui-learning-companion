---
key: 视频生成/图生视频/wan2.2-Fun-VACE视频扩展-KJ_1967240843000209410.json
name: wan2.2-Fun-VACE视频扩展-KJ_1967240843000209410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967240843000209410.json
hash: 9664f874c2bdbd9f
coverage: 0.729167
learned_at: 2026-10-15 22:31:41
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, WanVideoSampler, WanVideoBlockSwap, SetNode, SetNode, Reroute, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, WanVideoVAELoader, ImageConcatMulti, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, INTConstant, WanVideoSampler, GetNode, GetNode, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: TextJoin, ImagePadForOutpaint, VHS_VideoCombine, ImageAndMaskPreview, GetNode, WanVideoVACEEncode, RH_Captioner, LayerUtility: ImageScaleByAspectRatio V2, GetImageRangeFromBatch, GetImageRangeFromBatch, VHS_VideoInfo, VHS_DuplicateMasks, Note, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Fun-VACE视频扩展-KJ_1967240843000209410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967240843000209410.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `Reroute`
- `PrimitiveNode`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `WanVideoVAELoader`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: TextJoin`
- `ImagePadForOutpaint`
- `VHS_VideoCombine`
- `ImageAndMaskPreview`
- `GetNode`
- `WanVideoVACEEncode`
- `RH_Captioner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `VHS_VideoInfo`
- `VHS_DuplicateMasks`
- `Note`
- `VHS_LoadVideo`

## 知识

覆盖率 **73%**（35/48）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoScheduler`、`WanVideoVAELoader`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoLoraSelectMulti`、`INTConstant`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`LayerUtility: TextJoin`、`ImagePadForOutpaint`、`ImageAndMaskPreview`、`WanVideoVACEEncode`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`VHS_VideoInfo`、`VHS_DuplicateMasks`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti、ImageAndMaskPreview
