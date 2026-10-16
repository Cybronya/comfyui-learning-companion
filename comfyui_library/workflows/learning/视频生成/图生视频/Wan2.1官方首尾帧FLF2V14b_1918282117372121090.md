---
key: 视频生成/图生视频/Wan2.1官方首尾帧FLF2V14b_1918282117372121090.json
name: Wan2.1官方首尾帧FLF2V14b_1918282117372121090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1918282117372121090.json
hash: 0f949c2dd9ab6574
coverage: 0.875
learned_at: 2026-10-15 22:29:40
nodes: [SetNode, GetNode, GetNode, EmptyImage, AddLabel, AddLabel, ImageConcatMulti, SetNode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, ImageConcatMulti, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_LoadVideo, WanVideoBlockSwap, VHS_VideoCombine, WanVideoSampler, VHS_VideoCombine, GetImageSizeAndCount, WanVideoDecode, WanVideoTextEncode, LoadWanVideoClipTextEncoder, ImageResize+, ImageResize+, WanVideoTeaCache, WanVideoSLG, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadImage, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1官方首尾帧FLF2V14b_1918282117372121090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1918282117372121090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（32 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `ImageConcatMulti`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `ImageResize+`
- `ImageResize+`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`EmptyImage`、`AddLabel`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`、`ImageResize+`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
