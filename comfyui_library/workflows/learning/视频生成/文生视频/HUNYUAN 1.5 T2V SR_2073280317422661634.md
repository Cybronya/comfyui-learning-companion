---
key: 视频生成/文生视频/HUNYUAN 1.5 T2V SR_2073280317422661634.json
name: HUNYUAN 1.5 T2V SR_2073280317422661634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HUNYUAN 1.5 T2V SR_2073280317422661634.json
hash: bdf4734ded88d86c
coverage: 0.965517
learned_at: 2026-10-15 22:44:26
nodes: [CLIPTextEncode, HunyuanVideo15LatentUpscaleWithModel, BasicScheduler, CFGGuider, ModelSamplingSD3, KSamplerSelect, ModelSamplingSD3, DualCLIPLoader, VAELoader, CFGGuider, PathchSageAttentionKJ, HunyuanVideo15SuperResolution, KSamplerSelect, VHS_VideoCombine, LatentUpscaleModelLoader, RandomNoise, RandomNoise, UNETLoader, PathchSageAttentionKJ, BasicScheduler, CLIPTextEncode, UNETLoader, EmptyHunyuanVideo15Latent, MarkdownNote, SamplerCustomAdvanced, VHS_VideoCombine, VAEDecode, SamplerCustomAdvanced, VAEDecode]
patterns: []
missing: []
---

# 视频生成/文生视频/HUNYUAN 1.5 T2V SR_2073280317422661634.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HUNYUAN 1.5 T2V SR_2073280317422661634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `CLIPTextEncode` ★核心
- `HunyuanVideo15LatentUpscaleWithModel`
- `BasicScheduler`
- `CFGGuider`
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `VAELoader`
- `CFGGuider`
- `PathchSageAttentionKJ`
- `HunyuanVideo15SuperResolution`
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `RandomNoise`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanVideo15Latent`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心

## 知识

覆盖率 **97%**（28/29）

**有卡**：`CLIPTextEncode`、`HunyuanVideo15LatentUpscaleWithModel`、`BasicScheduler`、`CFGGuider`、`ModelSamplingSD3`、`KSamplerSelect`、`DualCLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`HunyuanVideo15SuperResolution`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`RandomNoise`、`UNETLoader`、`EmptyHunyuanVideo15Latent`、`SamplerCustomAdvanced`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyHunyuanVideo15Latent
