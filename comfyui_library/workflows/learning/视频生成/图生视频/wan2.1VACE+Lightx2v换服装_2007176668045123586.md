---
key: 视频生成/图生视频/wan2.1VACE+Lightx2v换服装_2007176668045123586.json
name: wan2.1VACE+Lightx2v换服装_2007176668045123586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007176668045123586.json
hash: 95c52bf51a1f33e2
coverage: 0.630952
learned_at: 2026-10-15 22:34:03
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), WanVideoTorchCompileSettings, SetNode, Label (rgthree), WanVideoBlockSwap, ImageResize+, GetNode, RMBG, GetNode, InvertMask, ImageFromBatch, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEModelSelect, WanVideoExperimentalArgs, WanVideoSLG, WanVideoEnhanceAVideo, GetNode, ClothesSegment, WanVideoModelLoader, WanVideoLoraSelect, SetNode, GetNode, SetNode, SetNode, GetNode, ImageResizeKJ, SetNode, VHS_VideoInfo, SetNode, SetNode, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), SetNode, GrowMask, easy cleanGpuUsed, SetNode, SetNode, Mute / Bypass Repeater (rgthree), WanVideoTeaCache, SetNode, Any Switch (rgthree), SetNode, FaceSegment, Reroute, GetImageSizeAndCount, GetNode, GetNode, GetNode, WanVideoDecode, WanVideoSampler, Mute / Bypass Relay (rgthree), WanVideoVACEEncode, GetNode, GetImageSize+, ResizeMask, INPAINT_MaskedFill, GetNode, GetNode, PreviewImage, VHS_VideoCombine, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), MarkdownNote, VHS_VideoCombine, LoadImage, easy int, PrimitiveStringMultiline, VHS_LoadVideo, WanVideoTextEncode, easy seed]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1VACE+Lightx2v换服装_2007176668045123586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007176668045123586.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（84 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `Label (rgthree)`
- `WanVideoBlockSwap`
- `ImageResize+`
- `GetNode`
- `RMBG`
- `GetNode`
- `InvertMask`
- `ImageFromBatch`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `GetNode`
- `ClothesSegment`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJ`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `SetNode`
- `GrowMask`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `Mute / Bypass Repeater (rgthree)`
- `WanVideoTeaCache`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `FaceSegment`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `Mute / Bypass Relay (rgthree)`
- `WanVideoVACEEncode`
- `GetNode`
- `GetImageSize+`
- `ResizeMask`
- `INPAINT_MaskedFill`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: BiRefNetUltraV2`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LoadImage`
- `easy int`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `WanVideoTextEncode`
- `easy seed`

## 知识

覆盖率 **63%**（53/84）

**有卡**：`Label (rgthree)`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`ImageResize+`、`RMBG`、`InvertMask`、`ImageFromBatch`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`ClothesSegment`、`WanVideoModelLoader`、`ImageResizeKJ`、`VHS_VideoInfo`、`GrowMask`、`easy cleanGpuUsed`、`Mute / Bypass Repeater (rgthree)`、`WanVideoTeaCache`、`FaceSegment`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`Mute / Bypass Relay (rgthree)`、`WanVideoVACEEncode`、`GetImageSize+`、`ResizeMask`、`INPAINT_MaskedFill`、`VHS_VideoCombine`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`LoadImage`、`easy int`、`VHS_LoadVideo`、`WanVideoTextEncode`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
