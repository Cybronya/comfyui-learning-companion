---
key: 视频生成/图生视频/极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json
name: 极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json
hash: 2a43baeef793efe2
coverage: 0.955556
learned_at: 2026-10-15 22:31:47
nodes: [WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoDecode, ImageFromBatch+, MaskToImage, ImageCompositeMasked, WanVideoSetBlockSwap, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoInfo, INTConstant, Reroute, Reroute, INTConstant, SimpleMath+, CreateCFGScheduleFloatList, VHS_VideoCombine, SolidMask, VHS_LoadVideo, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, WanVideoVACEModelSelect, WanVideoVACEModelSelect, VHS_VideoCombine, LoadImage, ImpactInt, ImpactInt, ImageResizeKJv2, easy imageRemBg, WanVideoVACEEncode, ImageResizeKJv2, LayerMask: SAM2VideoUltra, LayerMask: SegmentAnythingUltra V2, GrowMaskWithBlur, WanVideoVAELoader, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetLoRAs, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968955207906385921.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `ImageFromBatch+`
- `MaskToImage`
- `ImageCompositeMasked`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoInfo`
- `INTConstant`
- `Reroute`
- `Reroute`
- `INTConstant`
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `SolidMask`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `VHS_VideoCombine`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `WanVideoVACEEncode`
- `ImageResizeKJv2`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `GrowMaskWithBlur`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **96%**（43/45）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoDecode`、`ImageFromBatch+`、`MaskToImage`、`ImageCompositeMasked`、`INTConstant`、`LoadWanVideoT5TextEncoder`、`VHS_VideoInfo`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`SolidMask`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoVACEModelSelect`、`LoadImage`、`ImpactInt`、`ImageResizeKJv2`、`easy imageRemBg`、`WanVideoVACEEncode`、`LayerMask: SAM2VideoUltra`、`LayerMask: SegmentAnythingUltra V2`、`GrowMaskWithBlur`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
