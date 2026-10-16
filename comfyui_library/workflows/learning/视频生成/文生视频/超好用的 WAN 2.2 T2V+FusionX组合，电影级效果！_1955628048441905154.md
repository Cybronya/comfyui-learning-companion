---
key: 视频生成/文生视频/超好用的 WAN 2.2 T2V+FusionX组合，电影级效果！_1955628048441905154.json
name: 超好用的 WAN 2.2 T2V+FusionX组合，电影级效果！_1955628048441905154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1955628048441905154.json
hash: 93a3cc71e4333d76
coverage: 0.702703
learned_at: 2026-10-15 22:43:40
nodes: [Anything Everywhere, Anything Everywhere, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoEmptyEmbeds, Divide [DVB], mxSlider, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Anything Everywhere, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, GetNode, WanVideoDecode, GetNode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoSLG, WanVideoSampler, WanVideoExperimentalArgs, Textbox, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/超好用的 WAN 2.2 T2V+FusionX组合，电影级效果！_1955628048441905154.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1955628048441905154.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（37 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoEmptyEmbeds`
- `Divide [DVB]`
- `mxSlider`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `Anything Everywhere`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `Textbox`
- `VHS_VideoCombine`

## 知识

覆盖率 **70%**（26/37）

**有卡**：`WanVideoEmptyEmbeds`、`Divide [DVB]`、`mxSlider`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`Textbox`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSetLoRAs、WanVideoLoraSelectMulti、Textbox
