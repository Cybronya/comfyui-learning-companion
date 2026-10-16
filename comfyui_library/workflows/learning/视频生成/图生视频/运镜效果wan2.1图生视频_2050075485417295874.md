---
key: 视频生成/图生视频/运镜效果wan2.1图生视频_2050075485417295874.json
name: 运镜效果wan2.1图生视频_2050075485417295874.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2050075485417295874.json
hash: 98e90f53bd1e5f7f
coverage: 0.55
learned_at: 2026-10-15 22:37:17
nodes: [Anything Everywhere, Anything Everywhere, WanVideoDecode, Note, Note, Note, ImageCASharpening+, Anything Everywhere, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoTeaCache, Note, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, JWInteger, Note, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CLIPVisionLoader, Anything Everywhere, RHHiddenNodes, ShowText|pysssss, WanVideoTextEncode, SetNode, SetNode, SetNode, LoadImage, ImageResize+, PreviewImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/运镜效果wan2.1图生视频_2050075485417295874.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050075485417295874.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoDecode`
- `Note`
- `Note`
- `Note`
- `ImageCASharpening+`
- `Anything Everywhere`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `Note`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `JWInteger`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ImageResize+`
- `PreviewImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **55%**（22/40）

**有卡**：`WanVideoDecode`、`ImageCASharpening+`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoTeaCache`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`JWInteger`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CLIPVisionLoader`、`RHHiddenNodes`、`WanVideoTextEncode`、`LoadImage`、`ImageResize+`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
