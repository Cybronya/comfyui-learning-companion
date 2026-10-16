---
key: 视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1912679086651834369.json
name: WAN2.1 万相图生视频，效果强悍！_1912679086651834369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1912679086651834369.json
hash: 77f6cc293f8647c2
coverage: 0.842105
learned_at: 2026-10-15 22:29:32
nodes: [WanVideoSampler, WanVideoImageClipEncode, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoBlockSwap, Note, Note, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, CR Upscale Image, WanVideoDecode, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoContextOptions, WanVideoDecode, WanVideoTeaCache, WanVideoImageClipEncode, LoadImage, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, ImageResizeKJ, Note, LoadImage, WanVideoModelLoader, WanVideoTextEncode, Note, Note, WanVideoModelLoader, WanVideoVAELoader, VHS_VideoCombine, Fast Groups Muter (rgthree), LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoTextEncode, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, easy cleanGpuUsed, WanVideoBlockSwap, CR Upscale Image, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, WanVideoDecode, Note, Note, WanVideoImageClipEncode, Note, VHS_VideoCombine, WanVideoModelLoader, ImageResizeAdvanced, WanVideoTextEncode, LoadImage, CR Upscale Image]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1 万相图生视频，效果强悍！_1912679086651834369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912679086651834369.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（57 个）：
- `WanVideoSampler` ★核心
- `WanVideoImageClipEncode`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `CR Upscale Image`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoTeaCache`
- `WanVideoImageClipEncode`
- `LoadImage`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `ImageResizeKJ`
- `Note`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `CR Upscale Image`
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `WanVideoDecode`
- `Note`
- `Note`
- `WanVideoImageClipEncode`
- `Note`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `ImageResizeAdvanced`
- `WanVideoTextEncode`
- `LoadImage`
- `CR Upscale Image`

## 知识

覆盖率 **84%**（48/57）

**有卡**：`WanVideoSampler`、`WanVideoImageClipEncode`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`RIFE VFI`、`CR Upscale Image`、`WanVideoDecode`、`WanVideoEnhanceAVideo`、`WanVideoContextOptions`、`WanVideoTeaCache`、`LoadImage`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`ImageResizeAdvanced`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
