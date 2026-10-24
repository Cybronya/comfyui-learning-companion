---
key: 图片生成/图生图/【动态追踪运镜】wan2.1图生视频（全自动）_2044340242756407298.json
name: 【动态追踪运镜】wan2.1图生视频（全自动）_2044340242756407298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【动态追踪运镜】wan2.1图生视频（全自动）_2044340242756407298.json
hash: aac44081cf4e100e
coverage: 0.55
learned_at: 2026-10-23 11:49:39
nodes: [Anything Everywhere, Anything Everywhere, WanVideoDecode, Note, ImageCASharpening+, Anything Everywhere, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoTeaCache, WanVideoSLG, CogVideoEnhanceAVideo, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, Anything Everywhere, Note, WanVideoSetBlockSwap, CLIPVisionLoader, Note, RHHiddenNodes, ShowText|pysssss, WanVideoTextEncode, WanVideoExperimentalArgs, Note, Note, JWInteger, SetNode, SetNode, SetNode, LoadImage, ImageResize+, PreviewImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/【动态追踪运镜】wan2.1图生视频（全自动）_2044340242756407298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【动态追踪运镜】wan2.1图生视频（全自动）_2044340242756407298.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoDecode`
- `Note`
- `ImageCASharpening+`
- `Anything Everywhere`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `Note`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `Note`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `WanVideoExperimentalArgs`
- `Note`
- `Note`
- `JWInteger`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ImageResize+`
- `PreviewImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **55%**（22/40）

**有卡**：`WanVideoDecode`、`ImageCASharpening+`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`RHHiddenNodes`、`WanVideoTextEncode`、`WanVideoExperimentalArgs`、`JWInteger`、`LoadImage`、`ImageResize+`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
