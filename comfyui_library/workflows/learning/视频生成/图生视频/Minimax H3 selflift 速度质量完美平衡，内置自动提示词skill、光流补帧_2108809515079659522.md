---
key: 视频生成/图生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108809515079659522.json
name: Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108809515079659522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108809515079659522.json
hash: 28a3c389d35662f4
coverage: 0.465116
learned_at: 2026-10-17 22:49:58
nodes: [VAELoader, VAELoader, VAEDecode, VAEDecodeAudio, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, MiniMaxH3SigmaShift, ModelAttentionBackend, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SetNode, SetNode, SetNode, LoraLoaderModelOnly, SetNode, GetNode, GetNode, ConditioningZeroOut, KSamplerSelect, LTXVSeparateAVLatent, SetNode, GetNode, GetNode, SetNode, ModelPreviewOverrideKJ, LoraLoaderModelOnly, SetNode, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, VHS_LoadVideo, SetNode, LoadAudio, LoadAudio, LoadAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, QwenH3PromptLocal, MarkdownNote, ExtendIntermediateSigmas, BasicScheduler, SelfLiftH3Sampler, GetNode, GetNode, RIFE VFI, MiniMaxH3AudioConditioningT8, 忽略多组孤海, 忽略多组孤海, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, PrimitiveFloat, ResolutionSelector, MuyeTextEditOutput, easy textSwitch]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108809515079659522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108809515079659522.json`

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
- `QwenH3PromptLocal`
- `MarkdownNote`
- `ExtendIntermediateSigmas`
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `GetNode`
- `GetNode`
- `RIFE VFI`
- `MiniMaxH3AudioConditioningT8`
- `忽略多组孤海`
- `忽略多组孤海`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `ResolutionSelector`
- `MuyeTextEditOutput`
- `easy textSwitch`

## 知识

覆盖率 **47%**（40/86）

**有卡**：`VAELoader`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`ModelPreviewOverrideKJ`、`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`ComfyMathExpression`、`QwenH3PromptLocal`、`ExtendIntermediateSigmas`、`BasicScheduler`、`SelfLiftH3Sampler`、`RIFE VFI`、`MiniMaxH3AudioConditioningT8`、`忽略多组孤海`、`ResolutionSelector`、`MuyeTextEditOutput`、`easy textSwitch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
