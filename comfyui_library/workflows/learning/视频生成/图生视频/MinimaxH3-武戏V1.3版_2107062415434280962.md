---
key: 视频生成/图生视频/MinimaxH3-武戏V1.3版_2107062415434280962.json
name: MinimaxH3-武戏V1.3版_2107062415434280962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3-武戏V1.3版_2107062415434280962.json
hash: 4d50c42e6ae34d38
coverage: 0.710526
learned_at: 2026-10-17 22:18:46
nodes: [SetNode, SetNode, SetNode, SetNode, KSamplerSelect, easy clearCacheAll, GetNode, GetNode, FeiHouEasyH3RHOutput, GetNode, VAEDecode, VAEDecodeAudio, H3SigmaRefiner, BasicScheduler, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPreviewOverrideKJ, SetNode, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, FeiHouEasyH3RH, ConditioningZeroOut, FeiHouEasyH3RHLoader, LoraLoaderBypassModelOnly, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SemanticBridgeApplyT8, GetNode, FeiHouEasyH3RHLoader, VHS_VideoCombine, SelfLiftAvatarH3Sampler, RunningHub Deepcleaner, MarkdownNote, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/MinimaxH3-武戏V1.3版_2107062415434280962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3-武戏V1.3版_2107062415434280962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（38 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `easy clearCacheAll`
- `GetNode`
- `GetNode`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `H3SigmaRefiner`
- `BasicScheduler`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `SetNode`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `FeiHouEasyH3RH`
- `ConditioningZeroOut`
- `FeiHouEasyH3RHLoader`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SemanticBridgeApplyT8`
- `GetNode`
- `FeiHouEasyH3RHLoader`
- `VHS_VideoCombine`
- `SelfLiftAvatarH3Sampler` ★核心
- `RunningHub Deepcleaner`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **71%**（27/38）

**有卡**：`KSamplerSelect`、`easy clearCacheAll`、`FeiHouEasyH3RHOutput`、`VAEDecode`、`VAEDecodeAudio`、`H3SigmaRefiner`、`BasicScheduler`、`LoraLoaderModelOnly`、`ModelPreviewOverrideKJ`、`ModelAttentionBackend`、`FeiHouEasyH3RH`、`ConditioningZeroOut`、`FeiHouEasyH3RHLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3SemanticBridgeApplyT8`、`VHS_VideoCombine`、`SelfLiftAvatarH3Sampler`、`RunningHub Deepcleaner`、`Label (rgthree)`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、KSamplerSelect、SelfLiftAvatarH3Sampler、VAEDecodeAudio、LoraLoaderBypassModelOnly、ModelPreviewOverrideKJ
