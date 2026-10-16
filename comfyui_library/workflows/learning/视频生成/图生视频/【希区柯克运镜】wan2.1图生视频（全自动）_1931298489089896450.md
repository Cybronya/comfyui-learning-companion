---
key: 视频生成/图生视频/【希区柯克运镜】wan2.1图生视频（全自动）_1931298489089896450.json
name: 【希区柯克运镜】wan2.1图生视频（全自动）_1931298489089896450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1931298489089896450.json
hash: 2e485a71b5ec7e50
coverage: 0.55
learned_at: 2026-10-15 22:30:09
nodes: [Anything Everywhere, Anything Everywhere, WanVideoDecode, Note, Note, Note, ImageCASharpening+, Anything Everywhere, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, PreviewImage, VHS_VideoCombine, Anything Everywhere, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoModelLoader, ImageResize+, WanVideoTeaCache, WanVideoLoraSelect, RHHiddenNodes, LoadImage, Note, Note, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, ShowText|pysssss, WanVideoTextEncode, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/【希区柯克运镜】wan2.1图生视频（全自动）_1931298489089896450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1931298489089896450.json`

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
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
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
- `WanVideoModelLoader`
- `ImageResize+`
- `WanVideoTeaCache`
- `WanVideoLoraSelect`
- `RHHiddenNodes`
- `LoadImage`
- `Note`
- `Note`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `JWInteger`

## 知识

覆盖率 **55%**（22/40）

**有卡**：`WanVideoDecode`、`ImageCASharpening+`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoModelLoader`、`ImageResize+`、`WanVideoTeaCache`、`WanVideoLoraSelect`、`RHHiddenNodes`、`LoadImage`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
