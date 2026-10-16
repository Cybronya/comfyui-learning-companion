---
key: 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986.json
name: MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986.json
hash: f91edbb916fb2e85
coverage: 0.678571
learned_at: 2026-10-16 21:07:18
nodes: [KSamplerSelect, SamplerCustomAdvanced, BasicGuider, RandomNoise, MiniMaxH3ImageToVideo, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, VAELoader, ImageResizeKJv2, PreviewImage, MarkdownNote, MarkdownNote, MarkdownNote, 孤海注释, MarkdownNote, MarkdownNote, ResolutionSelector, BasicScheduler, CLIPLoader, ComfyMathExpression, VAELoader, UNETLoader, PathchSageAttentionKJ, LoadImage, PrimitiveStringMultiline, PrimitiveFloat, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `MiniMaxH3ImageToVideo`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `孤海注释`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `VAELoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **68%**（19/28）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`VAELoader`、`ImageResizeKJv2`、`ResolutionSelector`、`BasicScheduler`、`CLIPLoader`、`ComfyMathExpression`、`UNETLoader`、`PathchSageAttentionKJ`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
