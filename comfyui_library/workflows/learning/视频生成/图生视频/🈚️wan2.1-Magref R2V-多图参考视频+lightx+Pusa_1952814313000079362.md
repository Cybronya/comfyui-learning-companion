---
key: 视频生成/图生视频/🈚️wan2.1-Magref R2V-多图参考视频+lightx+Pusa_1952814313000079362.json
name: 🈚️wan2.1-Magref R2V-多图参考视频+lightx+Pusa_1952814313000079362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952814313000079362.json
hash: 319269d710f33eca
coverage: 0.455224
learned_at: 2026-10-15 22:31:03
nodes: [WanVideoEncode, GetNode, ImageResizeKJv2, GetNode, GetNode, CLIPVisionLoader, WanVideoSLG, WanVideoExperimentalArgs, WanVideoFreeInitArgs, WanVideoEnhanceAVideo, GetNode, WanVideoTeaCache, WanVideoUni3C_ControlnetLoader, GetNode, LayerUtility: CropByMask V2, easy imageRemBg, LayerUtility: CropByMask V2, LoadImage, LoadImage, ImagePadKJ, ImagePadKJ, LoadWanVideoT5TextEncoder, WanVideoUni3C_embeds, VHS_LoadVideo, WanVideoBlockSwap, WanVideoVAELoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, easy imageRemBg, ImagePadKJ, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, WanVideoLoraSelect, WanVideoLoraSelect, SetNode, WanVideoTextEncode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, SetNode, WanVideoSampler, WanVideoContextOptions, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelect, GetNode, GetNode, GetNode, PIP_图像联结, PreviewImage, PreviewImage, PIP_图像联结, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, CR Text, GetNode, GetNode, GetNode, GetNode, FastCanvasTool, Primitive integer [Crystools], Primitive integer [Crystools], PreviewImage, PreviewImage, GetNode, GetNode, GetNode, GetNode, PreviewImage, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, PIP_图像联结, SetNode, PIP_图像联结, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), Any Switch (rgthree), GetNode, Note, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, PreviewImage, WanVideoLoraSelect, PreviewImage, GetNode, GetNode, Primitive integer [Crystools], GetImageSize, easy mathInt, Bjornulf_ShowInt, GetNode, GetNode, WanVideoDecode, GetImageRangeFromBatch, SetNode, VHS_VideoCombine, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, Note, LayerUtility: ColorImage, FastCanvas, ImpactSwitch, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️wan2.1-Magref R2V-多图参考视频+lightx+Pusa_1952814313000079362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952814313000079362.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（134 个）：
- `WanVideoEncode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoFreeInitArgs`
- `WanVideoEnhanceAVideo`
- `GetNode`
- `WanVideoTeaCache`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `LayerUtility: CropByMask V2`
- `easy imageRemBg`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `LoadImage`
- `ImagePadKJ`
- `ImagePadKJ`
- `LoadWanVideoT5TextEncoder`
- `WanVideoUni3C_embeds`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageRemBg`
- `ImagePadKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `GetNode`
- `PIP_图像联结`
- `PreviewImage`
- `PreviewImage`
- `PIP_图像联结`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FastCanvasTool`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `PIP_图像联结`
- `SetNode`
- `PIP_图像联结`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `Note`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `WanVideoLoraSelect`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `Primitive integer [Crystools]`
- `GetImageSize`
- `easy mathInt`
- `Bjornulf_ShowInt`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `SetNode`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `LayerUtility: ColorImage`
- `FastCanvas`
- `ImpactSwitch`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **46%**（61/134）

**有卡**：`WanVideoEncode`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoFreeInitArgs`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoUni3C_ControlnetLoader`、`LayerUtility: CropByMask V2`、`easy imageRemBg`、`LoadImage`、`ImagePadKJ`、`LoadWanVideoT5TextEncoder`、`WanVideoUni3C_embeds`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoModelLoader`、`PIP_图像联结`、`CR Text`、`FastCanvasTool`、`Primitive integer [Crystools]`、`GetImageSize`、`easy mathInt`、`Bjornulf_ShowInt`、`WanVideoDecode`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`LayerUtility: ColorImage`、`FastCanvas`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
