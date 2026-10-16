---
key: 视频生成/文生视频/WAN2.1视频生成_720P_1932577426033549314.json
name: WAN2.1视频生成_720P_1932577426033549314.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1932577426033549314.json
hash: 6b29d99021d67601
coverage: 0.857143
learned_at: 2026-10-15 22:43:26
nodes: [LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoBlockSwap, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoDecode, ImageScale, VHS_VideoCombine, easy showAnything, RH_Translator, Reroute, RH_Captioner, CR Text Concatenate, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModel, VHS_VideoCombine, easy showAnything, RH_Translator, easy showAnything, WanVideoSampler, WanVideoTextEncode, WanVideoImageClipEncode, WanVideoTeaCache, WanVideoModelLoader, ImageResizeKJ, CR Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.1视频生成_720P_1932577426033549314.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1932577426033549314.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（28 个）：
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `ImageScale`
- `VHS_VideoCombine`
- `easy showAnything`
- `RH_Translator`
- `Reroute`
- `RH_Captioner`
- `CR Text Concatenate`
- `RIFE VFI`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `easy showAnything`
- `RH_Translator`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoImageClipEncode`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `ImageResizeKJ`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`ImageScale`、`VHS_VideoCombine`、`RH_Translator`、`RH_Captioner`、`CR Text Concatenate`、`RIFE VFI`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoImageClipEncode`、`WanVideoTeaCache`、`WanVideoModelLoader`、`ImageResizeKJ`、`CR Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
