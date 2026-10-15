---
key: 视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json
name: MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json
hash: d7d149489d4e3ef3
coverage: 0.72
learned_at: 2026-10-15 22:45:30
nodes: [KSamplerSelect, SamplerCustomAdvanced, BasicGuider, RandomNoise, VAEDecode, VAEDecodeAudio, ComfyMathExpression, MiniMaxH3ImageToVideo, MarkdownNote, MarkdownNote, MarkdownNote, VHS_VideoCombine, 孤海注释, MarkdownNote, PrimitiveFloat, Text, VAELoader, VAELoader, CLIPLoader, PathchSageAttentionKJ, UNETLoader, MarkdownNote, ResolutionSelector, BasicScheduler, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（25 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `MiniMaxH3ImageToVideo`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `孤海注释`
- `MarkdownNote`
- `PrimitiveFloat`
- `Text`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `MarkdownNote`
- `ResolutionSelector`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **72%**（18/25）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`VAEDecode`、`VAEDecodeAudio`、`ComfyMathExpression`、`MiniMaxH3ImageToVideo`、`VHS_VideoCombine`、`Text`、`VAELoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`UNETLoader`、`ResolutionSelector`、`BasicScheduler`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
