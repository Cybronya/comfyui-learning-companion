---
key: 视频生成/图生视频/【弧线围绕运镜】wan2.1图生视频（全自动）_1931133040167157762.json
name: 【弧线围绕运镜】wan2.1图生视频（全自动）_1931133040167157762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1931133040167157762.json
hash: 77eaa8eef928b55a
coverage: 0.55
learned_at: 2026-10-15 22:30:08
nodes: [Anything Everywhere, Anything Everywhere, WanVideoDecode, Note, Note, Note, ImageCASharpening+, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, Anything Everywhere, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, PreviewImage, VHS_VideoCombine, Anything Everywhere, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, ImageResize+, WanVideoTextEncode, WanVideoTeaCache, WanVideoModelLoader, JWInteger, ShowText|pysssss, LoadImage, WanVideoLoraSelect, WanVideoBlockSwap, RHHiddenNodes, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/【弧线围绕运镜】wan2.1图生视频（全自动）_1931133040167157762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1931133040167157762.json`

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
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `ImageResize+`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `JWInteger`
- `ShowText|pysssss`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `RHHiddenNodes`
- `Note`
- `Note`

## 知识

覆盖率 **55%**（22/40）

**有卡**：`WanVideoDecode`、`ImageCASharpening+`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`ImageResize+`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoModelLoader`、`JWInteger`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
