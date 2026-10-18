---
key: 视频生成/图生视频/wan2.1通义万相图生视频蹦蹦跳跳工作流_1899811031231639553.json
name: wan2.1通义万相图生视频蹦蹦跳跳工作流_1899811031231639553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1通义万相图生视频蹦蹦跳跳工作流_1899811031231639553.json
hash: 2bc74de96d57f850
coverage: 1
learned_at: 2026-10-15 22:29:22
nodes: [WanVideoDecode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoTorchCompileSettings, GetImageSizeAndCount, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoSampler, LoadWanVideoT5TextEncoder, Int, SimpleMath+, LoadImage, WanVideoImageClipEncode, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1通义万相图生视频蹦蹦跳跳工作流_1899811031231639553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1899811031231639553.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（17 个）：
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `GetImageSizeAndCount`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `Int`
- `SimpleMath+`
- `LoadImage`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoEnhanceAVideo`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`Int`、`SimpleMath+`、`LoadImage`、`WanVideoImageClipEncode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
