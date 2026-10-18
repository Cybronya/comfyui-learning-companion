---
key: 视频生成/图生视频/极致首中尾帧万相wan2.1+FusionX+VACE图生视频_1934272711260856322.json
name: 极致首中尾帧万相wan2.1+FusionX+VACE图生视频_1934272711260856322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/极致首中尾帧万相wan2.1+FusionX+VACE图生视频_1934272711260856322.json
hash: 1be0c960d13d551f
coverage: 0.975
learned_at: 2026-10-15 22:30:17
nodes: [LoadImage, LoadImage, LoadImage, Int, Int, ImageResizeKJ, ImageResizeKJ, GetImageRangeFromBatch, MaskBatchMulti, ImageBatchMulti, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoDecode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, VHS_VideoCombine, PMRF, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoVAELoader, ImageResizeKJ, GetImageSizeAndCount, WanVideoEnhanceAVideo, WanVideoSLG, VHS_VideoCombine, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVACEStartToEndFrame, LoadWanVideoT5TextEncoder, Int, Int, WanVideoSampler, WanVideoExperimentalArgs, WanVideoTextEncodeSingle, PrimitiveStringMultiline, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoMagCache]
patterns: []
missing: []
---

# 视频生成/图生视频/极致首中尾帧万相wan2.1+FusionX+VACE图生视频_1934272711260856322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934272711260856322.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Int`
- `Int`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `GetImageRangeFromBatch`
- `MaskBatchMulti`
- `ImageBatchMulti`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PMRF`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVACEStartToEndFrame`
- `LoadWanVideoT5TextEncoder`
- `Int`
- `Int`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoTextEncodeSingle`
- `PrimitiveStringMultiline`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoMagCache`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`LoadImage`、`Int`、`ImageResizeKJ`、`GetImageRangeFromBatch`、`MaskBatchMulti`、`ImageBatchMulti`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`WanVideoLoraSelect`、`WanVideoDecode`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`PMRF`、`LayerUtility: PurgeVRAM V2`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoMagCache`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、WanVideoLoraSelect
