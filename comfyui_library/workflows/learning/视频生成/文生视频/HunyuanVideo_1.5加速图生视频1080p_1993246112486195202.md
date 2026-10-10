---
key: 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p_1993246112486195202.json
name: HunyuanVideo_1.5加速图生视频1080p_1993246112486195202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p_1993246112486195202.json
hash: ec8d6e51310e7df7
coverage: 0.883721
learned_at: 2026-10-11 02:57:35
nodes: [CLIPVisionLoader, DualCLIPLoader, LatentUpscaleModelLoader, UNETLoader, CreateVideo, VAEDecodeTiled, CLIPVisionEncode, SaveVideo, HunyuanVideo15SuperResolution, HunyuanVideo15LatentUpscaleWithModel, CLIPTextEncode, CreateVideo, VAELoader, MarkdownNote, HunyuanVideo15ImageToVideo, VAEDecode, VAEDecodeTiled, MarkdownNote, MarkdownNote, KSamplerSelect, ModelSamplingSD3, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, Note, DisableNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, CFGGuider, SplitSigmas, BasicScheduler, LoraLoaderModelOnly, CLIPTextEncode, CFGGuider, RandomNoise, LoadImage, SaveVideo, Note, PathchSageAttentionKJ, UNETLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p_1993246112486195202.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p_1993246112486195202.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `CLIPVisionEncode`
- `SaveVideo`
- `HunyuanVideo15SuperResolution`
- `HunyuanVideo15LatentUpscaleWithModel`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAELoader`
- `MarkdownNote`
- `HunyuanVideo15ImageToVideo`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `Note`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `CFGGuider`
- `SplitSigmas`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `LoadImage`
- `SaveVideo`
- `Note`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心

## 知识

覆盖率 **88%**（38/43）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`CreateVideo`、`VAEDecodeTiled`、`CLIPVisionEncode`、`SaveVideo`、`HunyuanVideo15SuperResolution`、`HunyuanVideo15LatentUpscaleWithModel`、`CLIPTextEncode`、`VAELoader`、`HunyuanVideo15ImageToVideo`、`VAEDecode`、`KSamplerSelect`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicScheduler`、`DisableNoise`、`CFGGuider`、`SplitSigmas`、`LoraLoaderModelOnly`、`LoadImage`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
