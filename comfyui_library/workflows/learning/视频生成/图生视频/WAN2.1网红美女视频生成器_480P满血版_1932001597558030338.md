---
key: 视频生成/图生视频/WAN2.1网红美女视频生成器_480P满血版_1932001597558030338.json
name: WAN2.1网红美女视频生成器_480P满血版_1932001597558030338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1932001597558030338.json
hash: 857cf014ab08fd2d
coverage: 0.925926
learned_at: 2026-10-15 22:30:10
nodes: [UpscaleModelLoader, ImageResizeKJ, ImageUpscaleWithModel, ImageScale, RIFE VFI, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoDecode, PlaySound|pysssss, VHS_VideoCombine, WanVideoTeaCache, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoImageClipEncode, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadImage, RH_Translator, CR Text Concatenate, easy showAnything, WanVideoTextEncode, WanVideoModelLoader, easy showAnything, RH_Captioner, VHS_VideoCombine, PlaySound|pysssss, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1网红美女视频生成器_480P满血版_1932001597558030338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1932001597558030338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（27 个）：
- `UpscaleModelLoader`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `ImageScale`
- `RIFE VFI`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageClipEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadImage`
- `RH_Translator`
- `CR Text Concatenate`
- `easy showAnything`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `easy showAnything`
- `RH_Captioner`
- `VHS_VideoCombine`
- `PlaySound|pysssss`
- `CR Text`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`UpscaleModelLoader`、`ImageResizeKJ`、`ImageUpscaleWithModel`、`ImageScale`、`RIFE VFI`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoImageClipEncode`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadImage`、`RH_Translator`、`CR Text Concatenate`、`WanVideoTextEncode`、`WanVideoModelLoader`、`RH_Captioner`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
