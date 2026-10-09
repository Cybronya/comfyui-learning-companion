---
key: 视频生成/文生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108105415606226946.json
name: Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108105415606226946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108105415606226946.json
hash: 590cafa22ab879b7
coverage: 0.418605
learned_at: 2026-10-10 00:07:21
nodes: [VAELoader, VAELoader, VAEDecode, VAEDecodeAudio, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, MiniMaxH3SigmaShift, ModelAttentionBackend, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SetNode, SetNode, SetNode, LoraLoaderModelOnly, SetNode, GetNode, GetNode, ConditioningZeroOut, KSamplerSelect, LTXVSeparateAVLatent, SetNode, GetNode, GetNode, SetNode, ModelPreviewOverrideKJ, LoraLoaderModelOnly, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, VHS_LoadVideo, SetNode, LoadAudio, LoadAudio, LoadAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, PrimitiveFloat, QwenH3PromptLocal, MarkdownNote, ResolutionSelector, ExtendIntermediateSigmas, BasicScheduler, LoadImage, LoadImage, SelfLiftH3Sampler, GetNode, GetNode, RIFE VFI, easy textSwitch, MiniMaxH3AudioConditioningT8, 忽略多组孤海, 忽略多组孤海, MuyeTextEditOutput, VHS_VideoCombine]
patterns: []
missing: [RIFE VFI, easy textSwitch, 忽略多组孤海, 忽略多组孤海]
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108105415606226946.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3 selflift 速度质量完美平衡，内置自动提示词skill、光流补帧_2108105415606226946.json`

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

覆盖率 **42%**（36/86）

**有卡**：`VAELoader`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`ModelPreviewOverrideKJ`、`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`ComfyMathExpression`、`QwenH3PromptLocal`、`ResolutionSelector`、`ExtendIntermediateSigmas`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxH3AudioConditioningT8`、`MuyeTextEditOutput`

**缺卡**（4）：`RIFE VFI`、`easy textSwitch`、`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
