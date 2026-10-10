---
key: 视频生成/文生视频/Remix 1.0新模型文生视频_1977188003040907266.json
name: Remix 1.0新模型文生视频_1977188003040907266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Remix 1.0新模型文生视频_1977188003040907266.json
hash: 4b5354313dfb420c
coverage: 1
learned_at: 2026-10-10 23:05:10
nodes: [WanVideoSampler, WanVideoSampler, WanVideoSetRadialAttention, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoDecode, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoEmptyEmbeds, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/文生视频/Remix 1.0新模型文生视频_1977188003040907266.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Remix 1.0新模型文生视频_1977188003040907266.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（20 个）：
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetRadialAttention`
- `WanVideoSetRadialAttention`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoEmptyEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`WanVideoSampler`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、INTConstant、VHS_VideoCombine、WanVideoBlockSwap
