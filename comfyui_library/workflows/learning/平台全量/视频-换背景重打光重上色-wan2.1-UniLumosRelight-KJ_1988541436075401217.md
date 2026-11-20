---
key: 平台全量/视频-换背景重打光重上色-wan2.1-UniLumosRelight-KJ_1988541436075401217.json
name: 视频-换背景重打光重上色-wan2.1-UniLumosRelight-KJ_1988541436075401217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-换背景重打光重上色-wan2.1-UniLumosRelight-KJ_1988541436075401217.json
hash: 34df23198fcd92ac
coverage: 0.942857
learned_at: 2026-11-14 02:34:20
nodes: [WanVideoTextEncode, easy seed, easy int, ImageResizeKJv2, InvertMask, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, SetNode, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, WanVideoEncode, VHS_VideoCombine, DrawMaskOnImage, WanVideoEncode, DrawGaussianNoiseOnImage, easy imageRemBg, GetImageSizeAndCount, WanVideoUniLumosEmbeds, VHS_VideoCombine, easy int, easy int, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoInfo, Reroute, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoSampler, WanVideoModelLoader, VHS_LoadVideo, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/视频-换背景重打光重上色-wan2.1-UniLumosRelight-KJ_1988541436075401217.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-换背景重打光重上色-wan2.1-UniLumosRelight-KJ_1988541436075401217.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoTextEncode`
- `easy seed`
- `easy int`
- `ImageResizeKJv2`
- `InvertMask`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `WanVideoEncode`
- `DrawGaussianNoiseOnImage`
- `easy imageRemBg`
- `GetImageSizeAndCount`
- `WanVideoUniLumosEmbeds`
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `VHS_LoadVideo`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`WanVideoTextEncode`、`easy seed`、`easy int`、`ImageResizeKJv2`、`InvertMask`、`GetImageSizeAndCount`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoEncode`、`DrawMaskOnImage`、`DrawGaussianNoiseOnImage`、`easy imageRemBg`、`WanVideoUniLumosEmbeds`、`VHS_VideoInfo`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoModelLoader`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader
