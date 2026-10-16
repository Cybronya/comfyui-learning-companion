---
key: 视频生成/图生视频/WAN2.1图生视频开源之光_1912762337353265153.json
name: WAN2.1图生视频开源之光_1912762337353265153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1912762337353265153.json
hash: e13467bd57cf400c
coverage: 0.931034
learned_at: 2026-10-15 22:29:32
nodes: [Int, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoBlockSwap, Int, easy ifElse, easy ifElse, ImageListToImageBatch, WanVideoDecode, Logic Boolean, Number to Float, Image Aspect Ratio, ImageFromBatch+, ImageUpscaleWithModel, UpscaleModelLoader, WanVideoImageClipEncode, FILM VFI, ImageScale, WanVideoSampler, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTeaCache, LoadWanVideoClipTextEncoder, LoadImage, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1图生视频开源之光_1912762337353265153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912762337353265153.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（29 个）：
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoBlockSwap`
- `Int`
- `easy ifElse`
- `easy ifElse`
- `ImageListToImageBatch`
- `WanVideoDecode`
- `Logic Boolean`
- `Number to Float`
- `Image Aspect Ratio`
- `ImageFromBatch+`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `WanVideoImageClipEncode`
- `FILM VFI`
- `ImageScale`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadImage`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`Int`、`VHS_VideoCombine`、`WanVideoEnhanceAVideo`、`WanVideoBlockSwap`、`ImageListToImageBatch`、`WanVideoDecode`、`Logic Boolean`、`Number to Float`、`Image Aspect Ratio`、`ImageFromBatch+`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`WanVideoImageClipEncode`、`FILM VFI`、`ImageScale`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`LoadWanVideoClipTextEncoder`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
