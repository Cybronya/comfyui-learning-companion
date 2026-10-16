---
key: 视频生成/图生视频/首中尾帧万相wan2.1+VACE+FlashVSR高清丝滑变身图生视频_1981344492861169666.json
name: 首中尾帧万相wan2.1+VACE+FlashVSR高清丝滑变身图生视频_1981344492861169666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981344492861169666.json
hash: 644c59774d101bcb
coverage: 0.97561
learned_at: 2026-10-15 22:32:37
nodes: [Int, Int, WanVideoDecode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoEnhanceAVideo, WanVideoSLG, Int, Int, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, WanVideoExperimentalArgs, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoApplyNAG, ImageBatchMulti, MaskBatchMulti, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, FlashVSRNode, WanVideoMagCache, WanVideoVACEEncode, WanVideoTextEncodeSingle, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, GetImageRangeFromBatch, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, WanVideoTextEncodeSingle, RHHiddenNodes, WanVideoModelLoader, WanVideoExtraModelSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/首中尾帧万相wan2.1+VACE+FlashVSR高清丝滑变身图生视频_1981344492861169666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981344492861169666.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `Int`
- `Int`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `Int`
- `Int`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoApplyNAG`
- `ImageBatchMulti`
- `MaskBatchMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `FlashVSRNode`
- `WanVideoMagCache`
- `WanVideoVACEEncode`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEStartToEndFrame`
- `GetImageRangeFromBatch`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `WanVideoTextEncodeSingle`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`

## 知识

覆盖率 **98%**（40/41）

**有卡**：`Int`、`WanVideoDecode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`LoadImage`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoApplyNAG`、`ImageBatchMulti`、`MaskBatchMulti`、`GetImageSizeAndCount`、`WanVideoSampler`、`FlashVSRNode`、`WanVideoMagCache`、`WanVideoVACEEncode`、`WanVideoTextEncodeSingle`、`WanVideoVACEStartToEndFrame`、`GetImageRangeFromBatch`、`ImageResizeKJ`、`RHHiddenNodes`、`WanVideoModelLoader`、`WanVideoExtraModelSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、GetImageSizeAndCount
