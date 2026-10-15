---
key: 视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473.json
name: MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 All-in-One Accelerated V3 一体化工作流_2099131023387881473.json
hash: 35f5f5624704dbda
coverage: 0.95
learned_at: 2026-10-15 22:45:29
nodes: [SamplerCustomAdvanced, ResolutionSelector, KSamplerSelect, BasicScheduler, H3SigmaRefiner, ModelPreviewOverrideKJ, MarkdownNote, MiniMaxH3AVDecodeT8, VHS_VideoCombine, Label (rgthree), ModelAttentionBackend, CLIPLoader, VAELoader, VAELoader, CR Text, MiniMaxH3Unified, RandomNoise, BasicGuider, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
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

覆盖率 **95%**（19/20）

**有卡**：`SamplerCustomAdvanced`、`ResolutionSelector`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`ModelPreviewOverrideKJ`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`Label (rgthree)`、`ModelAttentionBackend`、`CLIPLoader`、`VAELoader`、`CR Text`、`MiniMaxH3Unified`、`RandomNoise`、`BasicGuider`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、MiniMaxH3AVDecodeT8
