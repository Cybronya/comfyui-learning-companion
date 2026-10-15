---
key: 视频生成/文生视频/MinimaxH3-双bf16满血版-4步加速lora 1.0+sage_2088155343741345793.json
name: MinimaxH3-双bf16满血版-4步加速lora 1.0+sage_2088155343741345793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MinimaxH3-双bf16满血版-4步加速lora 1.0+sage_2088155343741345793.json
hash: 12468c42c087bb59
coverage: 0.904762
learned_at: 2026-10-15 22:46:43
nodes: [LoadImage, PrimitiveFloat, VHS_VideoCombine, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, CLIPLoader, VAELoader, BasicGuider, KSamplerSelect, ComfyMathExpression, CR Prompt Text, MarkdownNote, UNETLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, ResolutionSelector, BasicScheduler, VAELoader, MiniMaxH3AudioConditioningT8]
patterns: []
missing: []
---

# 视频生成/文生视频/MinimaxH3-双bf16满血版-4步加速lora 1.0+sage_2088155343741345793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MinimaxH3-双bf16满血版-4步加速lora 1.0+sage_2088155343741345793.json`

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

覆盖率 **90%**（19/21）

**有卡**：`LoadImage`、`VHS_VideoCombine`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`CLIPLoader`、`VAELoader`、`BasicGuider`、`KSamplerSelect`、`ComfyMathExpression`、`CR Prompt Text`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ResolutionSelector`、`BasicScheduler`、`MiniMaxH3AudioConditioningT8`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
