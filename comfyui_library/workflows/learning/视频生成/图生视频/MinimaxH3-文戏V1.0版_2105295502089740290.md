---
key: 视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json
name: MinimaxH3-文戏V1.0版_2105295502089740290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json
hash: 39c9bf4497a265b5
coverage: 0.571429
learned_at: 2026-10-10 22:53:50
nodes: [SetNode, SetNode, SetNode, SetNode, KSamplerSelect, easy clearCacheAll, ConditioningZeroOut, GetNode, GetNode, H3SigmaRefiner, BasicScheduler, FeiHouEasyH3RHLoader, SetNode, LoraLoaderModelOnly, FeiHouEasyH3RHLoader, FeiHouEasyH3RHOutput, GetNode, MiniMaxH3SemanticBridgeApplyT8, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, ModelPreviewOverrideKJ, MarkdownNote, MiniMaxH3SemanticBridgeConfigT8, GetNode, VAEDecodeAudio, GetNode, SelfLiftAvatarH3Sampler, VAEDecode, VHS_VideoCombine, FeiHouEasyH3RH, RunningHub Deepcleaner, VRAM_Debug, Label (rgthree), Label (rgthree)]
patterns: []
missing: [Label (rgthree), Label (rgthree), RunningHub Deepcleaner, easy clearCacheAll]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（35 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `easy clearCacheAll`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `H3SigmaRefiner`
- `BasicScheduler`
- `FeiHouEasyH3RHLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `FeiHouEasyH3RHLoader`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `MiniMaxH3SemanticBridgeApplyT8`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `MarkdownNote`
- `MiniMaxH3SemanticBridgeConfigT8`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `SelfLiftAvatarH3Sampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `FeiHouEasyH3RH`
- `RunningHub Deepcleaner`
- `VRAM_Debug`
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **57%**（20/35）

**有卡**：`KSamplerSelect`、`ConditioningZeroOut`、`H3SigmaRefiner`、`BasicScheduler`、`FeiHouEasyH3RHLoader`、`LoraLoaderModelOnly`、`FeiHouEasyH3RHOutput`、`MiniMaxH3SemanticBridgeApplyT8`、`ModelAttentionBackend`、`ModelPreviewOverrideKJ`、`MiniMaxH3SemanticBridgeConfigT8`、`VAEDecodeAudio`、`SelfLiftAvatarH3Sampler`、`VAEDecode`、`VHS_VideoCombine`、`FeiHouEasyH3RH`、`VRAM_Debug`

**缺卡**（4）：`Label (rgthree)`、`Label (rgthree)`、`RunningHub Deepcleaner`、`easy clearCacheAll`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、KSamplerSelect、SelfLiftAvatarH3Sampler、VAEDecodeAudio、ModelPreviewOverrideKJ、FeiHouEasyH3RHOutput

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub Deepcleaner` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
