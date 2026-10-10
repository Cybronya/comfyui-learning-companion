---
key: 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p（熊叔版）_1993572660164706305.json
name: HunyuanVideo_1.5加速图生视频1080p（熊叔版）_1993572660164706305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p（熊叔版）_1993572660164706305.json
hash: 8001b90da3a5d61c
coverage: 0.883721
learned_at: 2026-10-11 02:57:35
nodes: [CLIPVisionLoader, DualCLIPLoader, LatentUpscaleModelLoader, UNETLoader, CreateVideo, VAEDecodeTiled, CLIPVisionEncode, HunyuanVideo15SuperResolution, CLIPTextEncode, CreateVideo, VAELoader, MarkdownNote, VAEDecode, VAEDecodeTiled, MarkdownNote, MarkdownNote, KSamplerSelect, ModelSamplingSD3, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, Note, DisableNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, CFGGuider, CFGGuider, SplitSigmas, BasicScheduler, LoraLoaderModelOnly, CFGGuider, RandomNoise, Note, PathchSageAttentionKJ, UNETLoader, HunyuanVideo15LatentUpscaleWithModel, SaveVideo, SaveVideo, CLIPTextEncode, LoadImage, HunyuanVideo15ImageToVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p（熊叔版）_1993572660164706305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p（熊叔版）_1993572660164706305.json`

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
- `HunyuanVideo15SuperResolution`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAELoader`
- `MarkdownNote`
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
- `CFGGuider`
- `RandomNoise`
- `Note`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `HunyuanVideo15LatentUpscaleWithModel`
- `SaveVideo`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `HunyuanVideo15ImageToVideo`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`CreateVideo`、`VAEDecodeTiled`、`CLIPVisionEncode`、`HunyuanVideo15SuperResolution`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`KSamplerSelect`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicScheduler`、`DisableNoise`、`CFGGuider`、`SplitSigmas`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`HunyuanVideo15LatentUpscaleWithModel`、`SaveVideo`、`LoadImage`、`HunyuanVideo15ImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
