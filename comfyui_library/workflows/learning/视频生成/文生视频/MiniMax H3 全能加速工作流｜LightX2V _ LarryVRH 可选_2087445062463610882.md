---
key: 视频生成/文生视频/MiniMax H3 全能加速工作流｜LightX2V _ LarryVRH 可选_2087445062463610882.json
name: MiniMax H3 全能加速工作流｜LightX2V _ LarryVRH 可选_2087445062463610882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全能加速工作流｜LightX2V _ LarryVRH 可选_2087445062463610882.json
hash: 08f14078a8342110
coverage: 0.793103
learned_at: 2026-10-15 22:45:36
nodes: [VAELoader, CLIPLoader, VAELoader, BasicGuider, MarkdownNote, RandomNoise, UNETLoader, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, SamplerCustomAdvanced, MiniMaxH3DualClockSamplerT8, ComfyMathExpression, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoadImage, LoadImage, Audio Cut (mtb), LoadAudio, MiniMaxH3AudioConditioningT8, MarkdownNote, VHS_VideoCombine, MarkdownNote, PrimitiveStringMultiline, MarkdownNote, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 全能加速工作流｜LightX2V _ LarryVRH 可选_2087445062463610882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全能加速工作流｜LightX2V _ LarryVRH 可选_2087445062463610882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（29 个）：
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `BasicGuider`
- `MarkdownNote`
- `RandomNoise`
- `UNETLoader` ★核心
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `Audio Cut (mtb)`
- `LoadAudio`
- `MiniMaxH3AudioConditioningT8`
- `MarkdownNote`
- `VHS_VideoCombine`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`VAELoader`、`CLIPLoader`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`SamplerCustomAdvanced`、`MiniMaxH3DualClockSamplerT8`、`ComfyMathExpression`、`LoraLoaderBypassModelOnly`、`Audio Cut (mtb)`、`LoadAudio`、`MiniMaxH3AudioConditioningT8`、`VHS_VideoCombine`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
