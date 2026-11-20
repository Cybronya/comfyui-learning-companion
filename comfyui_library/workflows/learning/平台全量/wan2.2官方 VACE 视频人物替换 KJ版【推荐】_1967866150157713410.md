---
key: 平台全量/wan2.2官方 VACE 视频人物替换 KJ版【推荐】_1967866150157713410.json
name: wan2.2官方 VACE 视频人物替换 KJ版【推荐】_1967866150157713410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2官方 VACE 视频人物替换 KJ版【推荐】_1967866150157713410.json
hash: d2c9123d51f53b77
coverage: 0.978723
learned_at: 2026-11-14 01:19:46
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, ImpactInt, ImpactInt, ImpactInt, SimpleMath+, ImageResizeKJv2, WanVideoTextEncode, VHS_VideoInfo, ImageResizeKJv2, INTConstant, CreateCFGScheduleFloatList, ImageFromBatch+, LayerMask: SegmentAnythingUltra V2, LayerMask: SAM2VideoUltra, SolidMask, GrowMaskWithBlur, ImageCompositeMasked, MaskToImage, VHS_VideoCombine, WanVideoVACEEncode, easy imageRemBg, INTConstant, GetImageSizeAndCount, WanVideoSampler, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, CR Text, MarkdownNote, Note Plus (mtb), LoadImage, VHS_LoadVideo, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader]
patterns: []
missing: []
---

# 平台全量/wan2.2官方 VACE 视频人物替换 KJ版【推荐】_1967866150157713410.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2官方 VACE 视频人物替换 KJ版【推荐】_1967866150157713410.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `SimpleMath+`
- `ImageResizeKJv2`
- `WanVideoTextEncode`
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `ImageFromBatch+`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerMask: SAM2VideoUltra`
- `SolidMask`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `MaskToImage`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `easy imageRemBg`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`ImpactInt`、`SimpleMath+`、`ImageResizeKJv2`、`WanVideoTextEncode`、`VHS_VideoInfo`、`INTConstant`、`CreateCFGScheduleFloatList`、`ImageFromBatch+`、`LayerMask: SegmentAnythingUltra V2`、`LayerMask: SAM2VideoUltra`、`SolidMask`、`GrowMaskWithBlur`、`ImageCompositeMasked`、`MaskToImage`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`easy imageRemBg`、`GetImageSizeAndCount`、`ImageConcatMulti`、`CR Text`、`Note Plus (mtb)`、`LoadImage`、`VHS_LoadVideo`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
