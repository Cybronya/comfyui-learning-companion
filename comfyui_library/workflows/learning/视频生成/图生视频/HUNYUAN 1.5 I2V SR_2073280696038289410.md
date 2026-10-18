---
key: 视频生成/图生视频/HUNYUAN 1.5 I2V SR_2073280696038289410.json
name: HUNYUAN 1.5 I2V SR_2073280696038289410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/HUNYUAN 1.5 I2V SR_2073280696038289410.json
hash: 2200a2b3f98ed65a
coverage: 0.971429
learned_at: 2026-10-15 22:41:02
nodes: [BasicScheduler, CFGGuider, ModelSamplingSD3, KSamplerSelect, ModelSamplingSD3, DualCLIPLoader, PathchSageAttentionKJ, HunyuanVideo15SuperResolution, KSamplerSelect, UNETLoader, VHS_VideoCombine, VHS_VideoCombine, LatentUpscaleModelLoader, RandomNoise, RandomNoise, PathchSageAttentionKJ, BasicScheduler, CFGGuider, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, HunyuanVideo15ImageToVideo, HunyuanVideo15LatentUpscaleWithModel, GetImageSize, CLIPTextEncode, UNETLoader, ResizeLongestToNode, easy cleanGpuUsed, LoadImage, MarkdownNote, SamplerCustomAdvanced, VAEDecode, SamplerCustomAdvanced, VAELoader, VAEDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/HUNYUAN 1.5 I2V SR_2073280696038289410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073280696038289410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `BasicScheduler`
- `CFGGuider`
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `PathchSageAttentionKJ`
- `HunyuanVideo15SuperResolution`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `RandomNoise`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `HunyuanVideo15ImageToVideo`
- `HunyuanVideo15LatentUpscaleWithModel`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ResizeLongestToNode`
- `easy cleanGpuUsed`
- `LoadImage`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAEDecode` ★核心

## 知识

覆盖率 **97%**（34/35）

**有卡**：`BasicScheduler`、`CFGGuider`、`ModelSamplingSD3`、`KSamplerSelect`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`HunyuanVideo15SuperResolution`、`UNETLoader`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`RandomNoise`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`HunyuanVideo15ImageToVideo`、`HunyuanVideo15LatentUpscaleWithModel`、`GetImageSize`、`ResizeLongestToNode`、`easy cleanGpuUsed`、`LoadImage`、`SamplerCustomAdvanced`、`VAEDecode`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
