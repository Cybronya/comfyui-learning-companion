---
key: 视频生成/图生视频/WAN2.1网红美女视频生成器_720P_1932009420425723906.json
name: WAN2.1网红美女视频生成器_720P_1932009420425723906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1932009420425723906.json
hash: 8fd98f8698de049b
coverage: 0.925926
learned_at: 2026-10-15 22:30:10
nodes: [PlaySound|pysssss, LoadWanVideoT5TextEncoder, WanVideoTextEncode, easy showAnything, PlaySound|pysssss, VHS_VideoCombine, LoadImage, ImageResizeKJ, LoadWanVideoClipTextEncoder, WanVideoVAELoader, easy showAnything, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModel, ImageScale, WanVideoModelLoader, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoBlockSwap, RH_Captioner, CR Text Concatenate, CR Text, WanVideoImageClipEncode, VHS_VideoCombine, WanVideoSampler, WanVideoSLG]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1网红美女视频生成器_720P_1932009420425723906.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1932009420425723906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（27 个）：
- `PlaySound|pysssss`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `easy showAnything`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJ`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `easy showAnything`
- `RIFE VFI`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScale`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `RH_Captioner`
- `CR Text Concatenate`
- `CR Text`
- `WanVideoImageClipEncode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSLG`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`PlaySound|pysssss`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJ`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`RIFE VFI`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScale`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`RH_Captioner`、`CR Text Concatenate`、`CR Text`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoSLG`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
