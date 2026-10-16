---
key: 视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json
name: MiniMax H3  8.20_2084615308018540545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json
hash: a3e02ce7ec76ee77
coverage: 0.95122
learned_at: 2026-10-16 20:35:33
nodes: [MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, LoadAudio, LoadAudio, UNETLoader, PrimitiveFloat, SigmasToFloat, KSamplerSelect, VAELoader, ComfyMathExpression, BasicGuider, VAEDecode, VAEDecodeAudio, CLIPLoader, RandomNoise, LoadImage, Lora Loader Stack (rgthree), LoadImage, PixaromaSaveMp4, BasicScheduler, VAELoader, LoadImage, LoadImage, MarkdownNote, ResolutionSelector, LoadAudio, MiniMaxH3SigmaShift, SplitSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, MinimaxH3LatentUpscalerNode3D, LTXVConcatAVLatent, SamplerCustomAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `SigmasToFloat`
- `KSamplerSelect` ★核心
- `VAELoader`
- `ComfyMathExpression`
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CLIPLoader`
- `RandomNoise`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `LoadImage`
- `PixaromaSaveMp4`
- `BasicScheduler`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `ResolutionSelector`
- `LoadAudio`
- `MiniMaxH3SigmaShift`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscalerNode3D`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`LoadAudio`、`UNETLoader`、`SigmasToFloat`、`KSamplerSelect`、`VAELoader`、`ComfyMathExpression`、`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`RandomNoise`、`Lora Loader Stack (rgthree)`、`PixaromaSaveMp4`、`BasicScheduler`、`ResolutionSelector`、`MiniMaxH3SigmaShift`、`SplitSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscalerNode3D`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`MiniMaxH3ReferenceToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
