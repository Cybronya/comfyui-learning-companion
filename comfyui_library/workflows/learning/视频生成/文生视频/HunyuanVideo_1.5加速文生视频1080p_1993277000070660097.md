---
key: 视频生成/文生视频/HunyuanVideo_1.5加速文生视频1080p_1993277000070660097.json
name: HunyuanVideo_1.5加速文生视频1080p_1993277000070660097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HunyuanVideo_1.5加速文生视频1080p_1993277000070660097.json
hash: 6a636abcb731d7cf
coverage: 0.878049
learned_at: 2026-10-15 22:44:28
nodes: [DualCLIPLoader, UNETLoader, CreateVideo, VAEDecodeTiled, SaveVideo, HunyuanVideo15LatentUpscaleWithModel, CreateVideo, VAELoader, VAEDecode, VAEDecodeTiled, VAEDecode, MarkdownNote, HunyuanVideo15SuperResolution, Note, Note, EmptyHunyuanVideo15Latent, MarkdownNote, LatentUpscaleModelLoader, CLIPTextEncode, RandomNoise, KSamplerSelect, ModelSamplingSD3, RandomNoise, KSamplerSelect, ModelSamplingSD3, BasicScheduler, SplitSigmas, Note, DisableNoise, SamplerCustomAdvanced, CFGGuider, CFGGuider, SamplerCustomAdvanced, BasicScheduler, CLIPTextEncode, SamplerCustomAdvanced, LoraLoaderModelOnly, CFGGuider, UNETLoader, PathchSageAttentionKJ, SaveVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/HunyuanVideo_1.5加速文生视频1080p_1993277000070660097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HunyuanVideo_1.5加速文生视频1080p_1993277000070660097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `HunyuanVideo15LatentUpscaleWithModel`
- `CreateVideo`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `HunyuanVideo15SuperResolution`
- `Note`
- `Note`
- `EmptyHunyuanVideo15Latent`
- `MarkdownNote`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `SplitSigmas`
- `Note`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `SaveVideo`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`CreateVideo`、`VAEDecodeTiled`、`SaveVideo`、`HunyuanVideo15LatentUpscaleWithModel`、`VAELoader`、`VAEDecode`、`HunyuanVideo15SuperResolution`、`EmptyHunyuanVideo15Latent`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`RandomNoise`、`KSamplerSelect`、`ModelSamplingSD3`、`BasicScheduler`、`SplitSigmas`、`DisableNoise`、`SamplerCustomAdvanced`、`CFGGuider`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
