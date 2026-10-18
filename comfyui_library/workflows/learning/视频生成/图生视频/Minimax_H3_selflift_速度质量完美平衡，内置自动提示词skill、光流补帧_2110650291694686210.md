---
key: 视频生成/图生视频/Minimax_H3_selflift_速度质量完美平衡，内置自动提示词skill、光流补帧_2110650291694686210.json
name: Minimax_H3_selflift_速度质量完美平衡，内置自动提示词skill、光流补帧_2110650291694686210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax_H3_selflift_速度质量完美平衡，内置自动提示词skill、光流补帧_2110650291694686210.json
hash: 6bdf2432642efb53
coverage: 0.465116
learned_at: 2026-10-18 00:23:43
nodes: [VAELoader, VAELoader, VAEDecode, VAEDecodeAudio, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, MiniMaxH3SigmaShift, ModelAttentionBackend, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SetNode, SetNode, SetNode, LoraLoaderModelOnly, SetNode, GetNode, GetNode, ConditioningZeroOut, KSamplerSelect, LTXVSeparateAVLatent, SetNode, GetNode, GetNode, SetNode, ModelPreviewOverrideKJ, LoraLoaderModelOnly, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, VHS_LoadVideo, SetNode, LoadAudio, LoadAudio, LoadAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, PrimitiveFloat, QwenH3PromptLocal, MarkdownNote, ResolutionSelector, ExtendIntermediateSigmas, BasicScheduler, LoadImage, LoadImage, SelfLiftH3Sampler, GetNode, GetNode, RIFE VFI, easy textSwitch, MiniMaxH3AudioConditioningT8, 忽略多组孤海, 忽略多组孤海, MuyeTextEditOutput, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax_H3_selflift_速度质量完美平衡，内置自动提示词skill、光流补帧_2110650291694686210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax_H3_selflift_速度质量完美平衡，内置自动提示词skill、光流补帧_2110650291694686210.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（86 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `QwenH3PromptLocal`
- `MarkdownNote`
- `ResolutionSelector`
- `ExtendIntermediateSigmas`
- `BasicScheduler`
- `LoadImage`
- `LoadImage`
- `SelfLiftH3Sampler` ★核心
- `GetNode`
- `GetNode`
- `RIFE VFI`
- `easy textSwitch`
- `MiniMaxH3AudioConditioningT8`
- `忽略多组孤海`
- `忽略多组孤海`
- `MuyeTextEditOutput`
- `VHS_VideoCombine`

## 知识

覆盖率 **47%**（40/86）

**有卡**：`VAELoader`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`ModelPreviewOverrideKJ`、`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`ComfyMathExpression`、`QwenH3PromptLocal`、`ResolutionSelector`、`ExtendIntermediateSigmas`、`BasicScheduler`、`SelfLiftH3Sampler`、`RIFE VFI`、`easy textSwitch`、`MiniMaxH3AudioConditioningT8`、`忽略多组孤海`、`MuyeTextEditOutput`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
