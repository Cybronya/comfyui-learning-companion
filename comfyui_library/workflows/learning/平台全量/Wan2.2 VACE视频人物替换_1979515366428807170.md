---
key: 平台全量/Wan2.2 VACE视频人物替换_1979515366428807170.json
name: Wan2.2 VACE视频人物替换_1979515366428807170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 VACE视频人物替换_1979515366428807170.json
hash: cf907cd7bc67fa8e
coverage: 1
learned_at: 2026-11-14 01:05:35
nodes: [WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoVACEModelSelect, WanVideoVAELoader, SimpleMath+, INTConstant, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSampler, INTConstant, WanVideoVACEEncode, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, LayerMask: SAM2VideoUltra, LayerMask: SegmentAnythingUltra V2, VHS_VideoCombine, LoadImage, ImageFromBatch+, ImageResizeKJv2, WanVideoLoraSelectMulti, INTConstant, SolidMask, INTConstant, VHS_LoadVideo, GrowMaskWithBlur, ImageResizeKJv2, VHS_VideoCombine, MaskToImage, ImageCompositeMasked, INTConstant, CreateCFGScheduleFloatList]
patterns: []
missing: []
---

# 平台全量/Wan2.2 VACE视频人物替换_1979515366428807170.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 VACE视频人物替换_1979515366428807170.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `SimpleMath+`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoVACEEncode`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `SolidMask`
- `INTConstant`
- `VHS_LoadVideo`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `MaskToImage`
- `ImageCompositeMasked`
- `INTConstant`
- `CreateCFGScheduleFloatList`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`SimpleMath+`、`INTConstant`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoVACEEncode`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`LayerMask: SAM2VideoUltra`、`LayerMask: SegmentAnythingUltra V2`、`VHS_VideoCombine`、`LoadImage`、`ImageFromBatch+`、`ImageResizeKJv2`、`SolidMask`、`VHS_LoadVideo`、`GrowMaskWithBlur`、`MaskToImage`、`ImageCompositeMasked`、`CreateCFGScheduleFloatList`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti
