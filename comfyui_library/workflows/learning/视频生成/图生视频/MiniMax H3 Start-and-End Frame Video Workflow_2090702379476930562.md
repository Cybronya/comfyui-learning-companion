---
key: 视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json
name: MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json
hash: 516831863c74e062
coverage: 0.88
learned_at: 2026-10-16 22:30:36
nodes: [KSamplerSelect, SamplerCustomAdvanced, BasicGuider, ComfyMathExpression, VAELoader, VAELoader, easy showAnything, VAEDecode, CreateVideo, VAEDecodeAudio, easy showAnything, RandomNoise, PathchSageAttentionKJ, MiniMaxH3BlockCacheT8, LoraLoaderModelOnly, BasicScheduler, UNETLoader, CLIPLoader, PrimitiveFloat, MiniMaxH3ImageToVideo, ResolutionSelector, LoadImage, LoadImage, SaveVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `ComfyMathExpression`
- `VAELoader`
- `VAELoader`
- `easy showAnything`
- `VAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeAudio` ★核心
- `easy showAnything`
- `RandomNoise`
- `PathchSageAttentionKJ`
- `MiniMaxH3BlockCacheT8`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveFloat`
- `MiniMaxH3ImageToVideo`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `SaveVideo`
- `LoadImage`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`ComfyMathExpression`、`VAELoader`、`VAEDecode`、`CreateVideo`、`VAEDecodeAudio`、`RandomNoise`、`PathchSageAttentionKJ`、`MiniMaxH3BlockCacheT8`、`LoraLoaderModelOnly`、`BasicScheduler`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3ImageToVideo`、`ResolutionSelector`、`LoadImage`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
