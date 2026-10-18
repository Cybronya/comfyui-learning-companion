---
key: 视频生成/文生视频/Wan2.1+Lightx2v文生视频极速版_1936093650231152641.json
name: Wan2.1+Lightx2v文生视频极速版_1936093650231152641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1+Lightx2v文生视频极速版_1936093650231152641.json
hash: 9e360bb20a8a31e6
coverage: 1
learned_at: 2026-10-15 22:43:29
nodes: [ImpactInt, ImpactInt, Text Multiline, WanVideoTextEncode, ImpactInt, ImpactInt, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoTorchCompileSettings, SimpleMath+, WanVideoLoraSelect, WanVideoSampler, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoBlockSwap, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1+Lightx2v文生视频极速版_1936093650231152641.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1936093650231152641.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（18 个）：
- `ImpactInt`
- `ImpactInt`
- `Text Multiline`
- `WanVideoTextEncode`
- `ImpactInt`
- `ImpactInt`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`ImpactInt`、`Text Multiline`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、ImpactInt、VHS_VideoCombine
