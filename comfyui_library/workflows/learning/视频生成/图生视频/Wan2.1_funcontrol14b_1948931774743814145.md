---
key: 视频生成/图生视频/Wan2.1_funcontrol14b_1948931774743814145.json
name: Wan2.1_funcontrol14b_1948931774743814145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948931774743814145.json
hash: 1dc5174222b93e60
coverage: 0.933333
learned_at: 2026-10-15 22:30:48
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, WanVideoControlEmbeds, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, Florence2Run, Florence2ModelLoader, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTeaCache, DisplayAny, WanVideoEncode, WanVideoDecode, ImagePadForOutpaint, Anything Everywhere, LoadWanVideoClipTextEncoder, WanVideoExperimentalArgs, WanVideoSampler, WanVideoVAELoader, WanVideoTextEncode, PreviewImage, KepStringLiteral, ImageResize+, WanVideoModelLoader, VHS_VideoCombine, ImageResizeKJ, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_funcontrol14b_1948931774743814145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948931774743814145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（30 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoControlEmbeds`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `Florence2Run`
- `Florence2ModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `DisplayAny`
- `WanVideoEncode`
- `WanVideoDecode`
- `ImagePadForOutpaint`
- `Anything Everywhere`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `PreviewImage`
- `KepStringLiteral`
- `ImageResize+`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoControlEmbeds`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`Florence2Run`、`Florence2ModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTeaCache`、`DisplayAny`、`WanVideoEncode`、`WanVideoDecode`、`ImagePadForOutpaint`、`LoadWanVideoClipTextEncoder`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoTextEncode`、`KepStringLiteral`、`ImageResize+`、`WanVideoModelLoader`、`VHS_VideoCombine`、`ImageResizeKJ`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
