---
key: 视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json
name: wan 2.1 文生视频 （综合拆分）_2001587510151114753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json
hash: 9b6c878ea4a04dee
coverage: 0.956522
learned_at: 2026-10-15 22:47:34
nodes: [Anything Everywhere, WanVideoDecode, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, WanVideoApplyNAG, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoVACEModelSelect, FantasyTalkingModelLoader, MultiTalkModelLoader, FantasyPortraitModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, WanVideoTextEncodeCached, CR Prompt Text]
patterns: []
missing: []
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

覆盖率 **96%**（22/23）

**有卡**：`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVACEModelSelect`、`FantasyTalkingModelLoader`、`MultiTalkModelLoader`、`FantasyPortraitModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti、CR Prompt Text、VHS_VideoCombine
