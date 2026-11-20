---
key: 平台全量/wan2.1 360旋特效_1901198215566499842.json
name: wan2.1 360旋特效_1901198215566499842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 360旋特效_1901198215566499842.json
hash: b3f76ec55b526e87
coverage: 0.777778
learned_at: 2026-11-14 01:19:02
nodes: [WanVideoVAELoader, WanVideoDecode, Note, WanVideoSampler, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoTextEncode, Simple String, LoadImage, Note, WanVideoImageClipEncode, Note, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, Note, WanVideoBlockSwap]
patterns: []
missing: []
---

# 平台全量/wan2.1 360旋特效_1901198215566499842.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 360旋特效_1901198215566499842.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（18 个）：
- `WanVideoVAELoader`
- `WanVideoDecode`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoTextEncode`
- `Simple String`
- `LoadImage`
- `Note`
- `WanVideoImageClipEncode`
- `Note`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `WanVideoBlockSwap`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoTextEncode`、`Simple String`、`LoadImage`、`WanVideoImageClipEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
