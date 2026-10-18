---
key: 视频生成/图生视频/Wan2.1 VACE14B 图生视频 电商产品服装展示_1926239959831769089.json
name: Wan2.1 VACE14B 图生视频 电商产品服装展示_1926239959831769089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 VACE14B 图生视频 电商产品服装展示_1926239959831769089.json
hash: 6d26e108d8f692c4
coverage: 0.785714
learned_at: 2026-10-15 22:29:52
nodes: [WanVideoSetBlockSwap, SetNode, WanVideoBlockSwap, WanVideoVACEModelSelect, GetNode, WanVideoModelLoader, WanVideoLoraSelect, Anything Everywhere, LoadWanVideoT5TextEncoder, Anything Everywhere, WanVideoVAELoader, Anything Everywhere, WanVideoVACEStartToEndFrame, PreviewImage, WanVideoVACEEncode, JWInteger, WanVideoTeaCache, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSampler, WanVideoDecode, ImageCASharpening+, LoadImage, ImageResize+, WanVideoTextEncode, VHS_VideoCombine, Note _O]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 VACE14B 图生视频 电商产品服装展示_1926239959831769089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1926239959831769089.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（28 个）：
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `WanVideoVACEEncode`
- `JWInteger`
- `WanVideoTeaCache`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageCASharpening+`
- `LoadImage`
- `ImageResize+`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `Note _O`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`JWInteger`、`WanVideoTeaCache`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoDecode`、`ImageCASharpening+`、`LoadImage`、`ImageResize+`、`WanVideoTextEncode`、`VHS_VideoCombine`、`Note _O`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
