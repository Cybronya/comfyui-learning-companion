---
key: 视频生成/文生视频/wan2.2-T2v-颜料变身小手办特效工作流_1969368974502862849.json
name: wan2.2-T2v-颜料变身小手办特效工作流_1969368974502862849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-T2v-颜料变身小手办特效工作流_1969368974502862849.json
hash: 46edcd79de59e207
coverage: 0.757576
learned_at: 2026-10-15 22:43:46
nodes: [WanVideoTinyVAELoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, GetNode, WanVideoDecode, VHS_VideoCombine, WanVideoSigmaToStep, WanVideoSampler, WanVideoScheduler, WanVideoSampler, PrimitiveNode, WanVideoScheduler, WanVideoDecode, SetNode, PrimitiveNode, MarkdownNote, Note, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoEmptyEmbeds, Switch any [Crystools], WanVideoEmptyEmbeds, ConcatText_Zho, Note, Text]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2-T2v-颜料变身小手办特效工作流_1969368974502862849.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969368974502862849.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（33 个）：
- `WanVideoTinyVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSigmaToStep`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoDecode`
- `SetNode`
- `PrimitiveNode`
- `MarkdownNote`
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoEmptyEmbeds`
- `Switch any [Crystools]`
- `WanVideoEmptyEmbeds`
- `ConcatText_Zho`
- `Note`
- `Text`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`WanVideoTinyVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSigmaToStep`、`WanVideoSampler`、`WanVideoScheduler`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`Switch any [Crystools]`、`ConcatText_Zho`、`Text`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoTinyVAELoader、WanVideoLoraSelectMulti、Text、VHS_VideoCombine
