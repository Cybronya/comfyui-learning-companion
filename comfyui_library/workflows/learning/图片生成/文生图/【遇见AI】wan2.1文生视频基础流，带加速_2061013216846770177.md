---
key: 图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json
name: 【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json
hash: 066958be071fa23c
coverage: 1
learned_at: 2026-10-19 23:03:37
nodes: [WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoEmptyEmbeds, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader]
patterns: []
missing: []
---

# 图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（16 个）：
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoEmptyEmbeds`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs、VHS_VideoCombine、WanVideoBlockSwap
