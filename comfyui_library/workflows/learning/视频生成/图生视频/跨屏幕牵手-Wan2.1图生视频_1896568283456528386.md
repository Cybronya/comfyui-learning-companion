---
key: 视频生成/图生视频/跨屏幕牵手-Wan2.1图生视频_1896568283456528386.json
name: 跨屏幕牵手-Wan2.1图生视频_1896568283456528386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/跨屏幕牵手-Wan2.1图生视频_1896568283456528386.json
hash: c28905db9367e342
coverage: 0.956522
learned_at: 2026-10-15 22:29:18
nodes: [WanVideoBlockSwap, WanVideoImageClipEncode, Primitive integer [Crystools], Primitive integer [Crystools], CM_IntToFloat, Primitive integer [Crystools], Note _O, Fast Groups Bypasser (rgthree), WanVideoTextEncode, Primitive integer [Crystools], WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoDecode, VHS_VideoCombine, WanVideoTorchCompileSettings, LoadImage, Primitive string [Crystools], WanVideoEnhanceAVideo, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoTeaCache]
patterns: []
missing: []
---

# 视频生成/图生视频/跨屏幕牵手-Wan2.1图生视频_1896568283456528386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1896568283456528386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（23 个）：
- `WanVideoBlockSwap`
- `WanVideoImageClipEncode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CM_IntToFloat`
- `Primitive integer [Crystools]`
- `Note _O`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `Primitive string [Crystools]`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`WanVideoBlockSwap`、`WanVideoImageClipEncode`、`Primitive integer [Crystools]`、`CM_IntToFloat`、`Note _O`、`WanVideoTextEncode`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`LoadImage`、`Primitive string [Crystools]`、`WanVideoEnhanceAVideo`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTeaCache`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
