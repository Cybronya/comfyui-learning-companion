---
key: 视频生成/图生视频/Wan2.1高速图生视频_1951680460374134786.json
name: Wan2.1高速图生视频_1951680460374134786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1高速图生视频_1951680460374134786.json
hash: 21a111c239035d40
coverage: 0.714286
learned_at: 2026-10-15 22:30:59
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, SetNode, CR Text, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoImageToVideoEncode, WanVideoApplyNAG, WanVideoEnhanceAVideo, WanVideoSLG, LoadImage, SetNode, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, VHS_VideoCombine, JWInteger, JWInteger, WanVideoModelLoader, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1高速图生视频_1951680460374134786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951680460374134786.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（28 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `CR Text`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoImageToVideoEncode`
- `WanVideoApplyNAG`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `LoadImage`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **71%**（20/28）

**有卡**：`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`CR Text`、`WanVideoTextEncodeSingle`、`WanVideoImageToVideoEncode`、`WanVideoApplyNAG`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`LoadImage`、`WanVideoLoraSelect`、`JWInteger`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoLoraSelect
