---
key: 视频生成/文生视频/Minimax H3动作增强修复双采--bf16-0.4-1.0_2096232383161917442.json
name: Minimax H3动作增强修复双采--bf16-0.4-1.0_2096232383161917442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3动作增强修复双采--bf16-0.4-1.0_2096232383161917442.json
hash: f44809d5ef8372d1
coverage: 0.903226
learned_at: 2026-10-11 21:41:49
nodes: [KSamplerSelect, CLIPLoader, ComfyMathExpression, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicGuider, CR Prompt Text, LoadImage, PrimitiveFloat, VAELoader, VAELoader, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVSeparateAVLatent, BasicScheduler, KSamplerSelect, BasicScheduler, RandomNoise, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AudioConditioningT8, MinimaxH3LatentUpscaler3D, UNETLoader, ResolutionSelector, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, BasicGuider, VHS_VideoCombine, VHS_VideoCombine, ResolutionSelector, MarkdownNote]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Minimax H3动作增强修复双采--bf16-0.4-1.0_2096232383161917442.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3动作增强修复双采--bf16-0.4-1.0_2096232383161917442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（31 个）：
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `CR Prompt Text`
- `LoadImage`
- `PrimitiveFloat`
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AudioConditioningT8`
- `MinimaxH3LatentUpscaler3D`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `BasicGuider`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `MarkdownNote`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`KSamplerSelect`、`CLIPLoader`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`BasicGuider`、`LoadImage`、`VAELoader`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`BasicScheduler`、`RandomNoise`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AudioConditioningT8`、`MinimaxH3LatentUpscaler3D`、`UNETLoader`、`ResolutionSelector`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
