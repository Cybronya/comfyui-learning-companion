---
key: 视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json
name: wan 2.1 文生视频 （综合拆分）_2001587510151114753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json
hash: 9b6c878ea4a04dee
coverage: 0.913043
learned_at: 2026-10-11 02:57:39
nodes: [Anything Everywhere, WanVideoDecode, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, WanVideoApplyNAG, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoVACEModelSelect, FantasyTalkingModelLoader, MultiTalkModelLoader, FantasyPortraitModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, WanVideoTextEncodeCached, CR Prompt Text]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（23 个）：
- `Anything Everywhere`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoVACEModelSelect`
- `FantasyTalkingModelLoader`
- `MultiTalkModelLoader`
- `FantasyPortraitModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVACEModelSelect`、`FantasyTalkingModelLoader`、`MultiTalkModelLoader`、`FantasyPortraitModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti、VHS_VideoCombine、WanVideoBlockSwap

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
