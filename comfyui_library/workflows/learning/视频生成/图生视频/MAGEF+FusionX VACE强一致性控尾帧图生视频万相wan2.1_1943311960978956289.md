---
key: 视频生成/图生视频/MAGEF+FusionX VACE强一致性控尾帧图生视频万相wan2.1_1943311960978956289.json
name: MAGEF+FusionX VACE强一致性控尾帧图生视频万相wan2.1_1943311960978956289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MAGEF+FusionX VACE强一致性控尾帧图生视频万相wan2.1_1943311960978956289.json
hash: c66453ebf3120dad
coverage: 0.96875
learned_at: 2026-10-15 22:30:38
nodes: [GetImageSizeAndCount, WanVideoVACEEncode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoDecode, LayerUtility: PurgeVRAM V2, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, GIMMVFI_interpolate, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, LoadImage, WanVideoModelLoader, VHS_VideoCombine, WanVideoLoraSelect, WanVideoMagCache, WanVideoExperimentalArgs, WanVideoSampler, PrimitiveStringMultiline, WanVideoVACEModelSelect, WanVideoTextEncodeSingle, ImageResizeKJ, GetImageRangeFromBatch, WanVideoApplyNAG, WanVideoVACEStartToEndFrame, WanVideoTextEncodeSingle, SimpleMath+, Int, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/MAGEF+FusionX VACE强一致性控尾帧图生视频万相wan2.1_1943311960978956289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1943311960978956289.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `PrimitiveStringMultiline`
- `WanVideoVACEModelSelect`
- `WanVideoTextEncodeSingle`
- `ImageResizeKJ`
- `GetImageRangeFromBatch`
- `WanVideoApplyNAG`
- `WanVideoVACEStartToEndFrame`
- `WanVideoTextEncodeSingle`
- `SimpleMath+`
- `Int`
- `Int`
- `Int`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoModelLoader`、`WanVideoMagCache`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoVACEModelSelect`、`WanVideoTextEncodeSingle`、`ImageResizeKJ`、`GetImageRangeFromBatch`、`WanVideoApplyNAG`、`WanVideoVACEStartToEndFrame`、`SimpleMath+`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、WanVideoLoraSelect
