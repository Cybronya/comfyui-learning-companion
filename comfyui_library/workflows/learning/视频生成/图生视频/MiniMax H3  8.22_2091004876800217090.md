---
key: 视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json
name: MiniMax H3  8.22_2091004876800217090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json
hash: e0f4f582dcf889e9
coverage: 0.955556
learned_at: 2026-10-16 22:30:34
nodes: [MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, LoadAudio, LoadAudio, UNETLoader, SigmasToFloat, KSamplerSelect, VAELoader, ComfyMathExpression, BasicGuider, VAEDecode, VAEDecodeAudio, CLIPLoader, RandomNoise, LoadImage, Lora Loader Stack (rgthree), LoadImage, PixaromaSaveMp4, BasicScheduler, VAELoader, LoadImage, MarkdownNote, LoadAudio, SamplerCustomAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, MiniMaxH3ReferenceToVideo, LTXVConcatAVLatent, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SplitSigmas, SolAttnMiniMax, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, LTXVSeparateAVLatent, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, easy cleanGpuUsed, PrimitiveFloat, MiniMaxH3SigmaShift, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `UNETLoader` ★核心
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
- `MarkdownNote`
- `LoadAudio`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `MiniMaxH3ReferenceToVideo`
- `LTXVConcatAVLatent`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SplitSigmas`
- `SolAttnMiniMax`
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `LTXVSeparateAVLatent`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `MiniMaxH3SigmaShift`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **96%**（43/45）

**有卡**：`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`LoadAudio`、`UNETLoader`、`SigmasToFloat`、`KSamplerSelect`、`VAELoader`、`ComfyMathExpression`、`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`RandomNoise`、`Lora Loader Stack (rgthree)`、`PixaromaSaveMp4`、`BasicScheduler`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`MiniMaxH3ReferenceToVideo`、`LTXVConcatAVLatent`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`SplitSigmas`、`SolAttnMiniMax`、`MinimaxH3LatentUpscaler3D`、`LTXVSeparateAVLatent`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3SigmaShift`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
