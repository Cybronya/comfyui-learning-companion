---
key: 视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json
name: Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json
hash: 6191b622173982d2
coverage: 0.708333
learned_at: 2026-10-11 21:30:19
nodes: [RandomNoise, MiniMaxH3AVDecodeT8, BasicGuider, SamplerCustomAdvanced, MiniMaxH3DualClockSamplerT8, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, VAELoader, VAELoader, CLIPLoader, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, 孤海注释, CR Prompt Text, PrimitiveFloat, ResolutionSelector, UNETLoader, MiniMaxH3AudioConditioningT8, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, VHS_VideoCombine]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（24 个）：
- `RandomNoise`
- `MiniMaxH3AVDecodeT8`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `孤海注释`
- `CR Prompt Text`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MiniMaxH3AudioConditioningT8`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`RandomNoise`、`MiniMaxH3AVDecodeT8`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3DualClockSamplerT8`、`ComfyMathExpression`、`VAELoader`、`CLIPLoader`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ResolutionSelector`、`UNETLoader`、`MiniMaxH3AudioConditioningT8`、`LoraLoaderBypassModelOnly`、`LoraLoaderModelOnly`、`VHS_VideoCombine`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
