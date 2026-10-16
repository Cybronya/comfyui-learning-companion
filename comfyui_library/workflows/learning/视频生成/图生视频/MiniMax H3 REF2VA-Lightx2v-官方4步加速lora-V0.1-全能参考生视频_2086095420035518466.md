---
key: 视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-全能参考生视频_2086095420035518466.json
name: MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-全能参考生视频_2086095420035518466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-全能参考生视频_2086095420035518466.json
hash: bb9ea0471c6668fb
coverage: 0.714286
learned_at: 2026-10-16 21:07:19
nodes: [KSamplerSelect, SamplerCustomAdvanced, BasicGuider, RandomNoise, MiniMaxH3ReferenceToVideo, VAEDecodeAudio, VAEDecode, MarkdownNote, MarkdownNote, MarkdownNote, 孤海注释, ComfyMathExpression, MarkdownNote, MarkdownNote, VAELoader, VAELoader, CLIPLoader, PathchSageAttentionKJ, LoadImage, BasicScheduler, ResolutionSelector, PrimitiveFloat, LoadImage, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-全能参考生视频_2086095420035518466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-全能参考生视频_2086095420035518466.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（28 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `MiniMaxH3ReferenceToVideo`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `孤海注释`
- `ComfyMathExpression`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `LoadImage`
- `BasicScheduler`
- `ResolutionSelector`
- `PrimitiveFloat`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 知识

覆盖率 **71%**（20/28）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`VAELoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`LoadImage`、`BasicScheduler`、`ResolutionSelector`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
