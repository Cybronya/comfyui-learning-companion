---
key: 视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json
name: Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json
hash: bef35c0e2c61cdab
coverage: 0.95122
learned_at: 2026-10-15 22:47:13
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, CreateVideo, ComfyMathExpression, CLIPLoader, BasicGuider, MiniMaxH3SigmaShift, PathchSageAttentionKJ, LoraLoaderModelOnly, BasicScheduler, KSamplerSelect, RandomNoise, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, CreateVideo, ComfyMathExpression, CLIPLoader, BasicGuider, MiniMaxH3SigmaShift, PathchSageAttentionKJ, LoraLoaderModelOnly, BasicScheduler, KSamplerSelect, MiniMaxH3ImageToVideo, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, CreateVideo, ComfyMathExpression, CLIPLoader, BasicGuider, MiniMaxH3SigmaShift, PathchSageAttentionKJ, LoraLoaderModelOnly, KSamplerSelect, RandomNoise, UNETLoader, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, CreateVideo, ComfyMathExpression, CLIPLoader, BasicGuider, MiniMaxH3SigmaShift, PathchSageAttentionKJ, LoraLoaderModelOnly, KSamplerSelect, UNETLoader, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, ImageResizeKJv2, PrimitiveFloat, ResolutionSelector, JjkText, PrimitiveFloat, SaveVideo, SaveVideo, SaveVideo, SaveVideo, JjkText, LoadImage, ResolutionSelector, BasicScheduler, BasicScheduler]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `CLIPLoader`
- `BasicGuider`
- `MiniMaxH3SigmaShift`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `CLIPLoader`
- `BasicGuider`
- `MiniMaxH3SigmaShift`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `MiniMaxH3ImageToVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ImageToVideo`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `CLIPLoader`
- `BasicGuider`
- `MiniMaxH3SigmaShift`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ImageToVideo`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `CLIPLoader`
- `BasicGuider`
- `MiniMaxH3SigmaShift`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ImageToVideo`
- `ImageResizeKJv2`
- `PrimitiveFloat`
- `ResolutionSelector`
- `JjkText`
- `PrimitiveFloat`
- `SaveVideo`
- `SaveVideo`
- `SaveVideo`
- `SaveVideo`
- `JjkText`
- `LoadImage`
- `ResolutionSelector`
- `BasicScheduler`
- `BasicScheduler`

## 知识

覆盖率 **95%**（78/82）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`CreateVideo`、`ComfyMathExpression`、`CLIPLoader`、`BasicGuider`、`MiniMaxH3SigmaShift`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`ImageResizeKJv2`、`ResolutionSelector`、`SaveVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
