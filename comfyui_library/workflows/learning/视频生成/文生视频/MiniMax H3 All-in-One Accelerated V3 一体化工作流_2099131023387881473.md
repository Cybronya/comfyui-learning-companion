---
key: 视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473.json
name: MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473.json
hash: 35f5f5624704dbda
coverage: 0.85
learned_at: 2026-10-11 21:41:40
nodes: [SamplerCustomAdvanced, ResolutionSelector, KSamplerSelect, BasicScheduler, H3SigmaRefiner, ModelPreviewOverrideKJ, MarkdownNote, MiniMaxH3AVDecodeT8, VHS_VideoCombine, Label (rgthree), ModelAttentionBackend, CLIPLoader, VAELoader, VAELoader, CR Text, MiniMaxH3Unified, RandomNoise, BasicGuider, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: [CR Text, Label (rgthree)]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473.json`

## 结构

**生成流程**：Model → Latent → Sampling → Other

**节点**（20 个）：
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `H3SigmaRefiner`
- `ModelPreviewOverrideKJ`
- `MarkdownNote`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `ModelAttentionBackend`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `CR Text`
- `MiniMaxH3Unified`
- `RandomNoise`
- `BasicGuider`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **85%**（17/20）

**有卡**：`SamplerCustomAdvanced`、`ResolutionSelector`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`ModelPreviewOverrideKJ`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`ModelAttentionBackend`、`CLIPLoader`、`VAELoader`、`MiniMaxH3Unified`、`RandomNoise`、`BasicGuider`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（2）：`CR Text`、`Label (rgthree)`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、MiniMaxH3AVDecodeT8

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
