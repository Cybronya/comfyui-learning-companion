---
key: 视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json
name: MinimaxH3-文戏V1.0版_2105295502089740290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json
hash: 39c9bf4497a265b5
coverage: 0.685714
learned_at: 2026-10-15 22:42:54
nodes: [SetNode, SetNode, SetNode, SetNode, KSamplerSelect, easy clearCacheAll, ConditioningZeroOut, GetNode, GetNode, H3SigmaRefiner, BasicScheduler, FeiHouEasyH3RHLoader, SetNode, LoraLoaderModelOnly, FeiHouEasyH3RHLoader, FeiHouEasyH3RHOutput, GetNode, MiniMaxH3SemanticBridgeApplyT8, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, ModelPreviewOverrideKJ, MarkdownNote, MiniMaxH3SemanticBridgeConfigT8, GetNode, VAEDecodeAudio, GetNode, SelfLiftAvatarH3Sampler, VAEDecode, VHS_VideoCombine, FeiHouEasyH3RH, RunningHub Deepcleaner, VRAM_Debug, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
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

覆盖率 **69%**（24/35）

**有卡**：`KSamplerSelect`、`easy clearCacheAll`、`ConditioningZeroOut`、`H3SigmaRefiner`、`BasicScheduler`、`FeiHouEasyH3RHLoader`、`LoraLoaderModelOnly`、`FeiHouEasyH3RHOutput`、`MiniMaxH3SemanticBridgeApplyT8`、`ModelAttentionBackend`、`ModelPreviewOverrideKJ`、`MiniMaxH3SemanticBridgeConfigT8`、`VAEDecodeAudio`、`SelfLiftAvatarH3Sampler`、`VAEDecode`、`VHS_VideoCombine`、`FeiHouEasyH3RH`、`RunningHub Deepcleaner`、`VRAM_Debug`、`Label (rgthree)`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、KSamplerSelect、SelfLiftAvatarH3Sampler、VAEDecodeAudio、ModelPreviewOverrideKJ、FeiHouEasyH3RHOutput
