---
key: 视频生成/图生视频/【高速跟随运镜】wan2.1图生视频（全自动）_1930913690252718081.json
name: 【高速跟随运镜】wan2.1图生视频（全自动）_1930913690252718081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【高速跟随运镜】wan2.1图生视频（全自动）_1930913690252718081.json
hash: 2a3201b7ca78d4b0
coverage: 0.55
learned_at: 2026-10-15 22:30:08
nodes: [Anything Everywhere, Anything Everywhere, WanVideoDecode, Note, Note, Note, ImageCASharpening+, Anything Everywhere, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, PreviewImage, VHS_VideoCombine, Note, JWInteger, Anything Everywhere, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoLoraSelect, LoadImage, WanVideoModelLoader, ImageResize+, ShowText|pysssss, WanVideoTextEncode, RHHiddenNodes, WanVideoTeaCache, Note, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs]
patterns: []
missing: []
---

# 视频生成/图生视频/【高速跟随运镜】wan2.1图生视频（全自动）_1930913690252718081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930913690252718081.json`

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
- `Note`
- `JWInteger`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoModelLoader`
- `ImageResize+`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `WanVideoTeaCache`
- `Note`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`

## 知识

覆盖率 **55%**（22/40）

**有卡**：`WanVideoDecode`、`ImageCASharpening+`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`JWInteger`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoModelLoader`、`ImageResize+`、`WanVideoTextEncode`、`RHHiddenNodes`、`WanVideoTeaCache`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
