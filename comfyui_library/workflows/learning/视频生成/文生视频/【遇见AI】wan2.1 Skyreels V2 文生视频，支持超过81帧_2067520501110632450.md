---
key: 视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json
name: 【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json
hash: b0783555a4e48c86
coverage: 0.947368
learned_at: 2026-10-11 20:21:33
nodes: [WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoCombine, MarkdownNote, LoadImage, LoadImage, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（19 个）：
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LoadImage`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs、VHS_VideoCombine
