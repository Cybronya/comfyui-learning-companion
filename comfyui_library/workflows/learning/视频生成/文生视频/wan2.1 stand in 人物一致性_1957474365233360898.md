---
key: 视频生成/文生视频/wan2.1 stand in 人物一致性_1957474365233360898.json
name: wan2.1 stand in 人物一致性_1957474365233360898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1 stand in 人物一致性_1957474365233360898.json
hash: ce69ef69f9f420e4
coverage: 0.6
learned_at: 2026-10-10 23:09:30
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, FaceProcessorLoader, ApplyFaceProcessor, PreviewImage, GetNode, GetNode, WanVideoDecode, WanVideoEncode, WanVideoAddStandInLatent, SetNode, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoEmptyEmbeds, WanVideoSampler, VHS_VideoCombine, LoadImage, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1 stand in 人物一致性_1957474365233360898.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.1 stand in 人物一致性_1957474365233360898.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（25 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `FaceProcessorLoader`
- `ApplyFaceProcessor`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoAddStandInLatent`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **60%**（15/25）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoDecode`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoAddStandInLatent、WanVideoEncode、WanVideoLoraSelectMulti
