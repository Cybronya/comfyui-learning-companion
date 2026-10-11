---
key: 视频生成/文生视频/MinimaxH3-双bf16满血版-8步加速lora 1.0+sage_2088154982188150785.json
name: MinimaxH3-双bf16满血版-8步加速lora 1.0+sage_2088154982188150785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MinimaxH3-双bf16满血版-8步加速lora 1.0+sage_2088154982188150785.json
hash: 230056ee2dded9c9
coverage: 0.857143
learned_at: 2026-10-11 20:53:46
nodes: [LoadImage, PrimitiveFloat, VHS_VideoCombine, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, CLIPLoader, VAELoader, BasicGuider, KSamplerSelect, ComfyMathExpression, CR Prompt Text, MarkdownNote, UNETLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, ResolutionSelector, BasicScheduler, VAELoader, MiniMaxH3AudioConditioningT8]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/MinimaxH3-双bf16满血版-8步加速lora 1.0+sage_2088154982188150785.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MinimaxH3-双bf16满血版-8步加速lora 1.0+sage_2088154982188150785.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（21 个）：
- `LoadImage`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `CLIPLoader`
- `VAELoader`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `CR Prompt Text`
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `BasicScheduler`
- `VAELoader`
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`LoadImage`、`VHS_VideoCombine`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`CLIPLoader`、`VAELoader`、`BasicGuider`、`KSamplerSelect`、`ComfyMathExpression`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ResolutionSelector`、`BasicScheduler`、`MiniMaxH3AudioConditioningT8`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
