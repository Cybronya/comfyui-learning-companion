---
key: 视频生成/文生视频/wan2.1 MAGREF_FusionX 3倍加速图生视频_1938855885659627522.json
name: wan2.1 MAGREF_FusionX 3倍加速图生视频_1938855885659627522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1 MAGREF_FusionX 3倍加速图生视频_1938855885659627522.json
hash: df04d3ea046392c0
coverage: 0.75
learned_at: 2026-10-15 22:43:30
nodes: [SetNode, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, GetNode, GetNode, GetNode, GetNode, JWInteger, GetNode, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoApplyNAG, CLIPVisionLoader, ImageResizeKJv2, PreviewImage, WanVideoClipVisionEncode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, MathExpression|pysssss, WanVideoSampler, JWInteger, JWInteger, easy imageRemBg, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, CR Text, LoadImage, VHS_VideoCombine, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1 MAGREF_FusionX 3倍加速图生视频_1938855885659627522.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1938855885659627522.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `GetNode`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `MathExpression|pysssss`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `easy imageRemBg`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `CR Text`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`JWInteger`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageToVideoEncode`、`MathExpression|pysssss`、`WanVideoSampler`、`easy imageRemBg`、`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoCombine`、`CR Text`、`LoadImage`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
