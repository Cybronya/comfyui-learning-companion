---
key: 视频生成/文生视频/wan2.2-多图首尾帧（待更新）_1985625491241672705.json
name: wan2.2-多图首尾帧（待更新）_1985625491241672705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-多图首尾帧（待更新）_1985625491241672705.json
hash: b55c5197011c9188
coverage: 0.942857
learned_at: 2026-10-15 22:47:35
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, VAEDecode, VHS_VideoCombine, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ApplySageAttention, LoraLoaderModelOnly, ApplySageAttention, ImageResizeKJ, ImageResizeKJ, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, ImageBatchMulti, INTConstant, INTConstant, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, ImageResizeKJ, LoadImage, LoadImage, LoadImage, CLIPTextEncode, AILab_QwenVL, LoraLoaderModelOnly, easy showAnything, WanFirstMiddleLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "beta57", "sampler_name": 1, "scheduler": "deis_3m_ode", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2-多图首尾帧（待更新）_1985625491241672705.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-多图首尾帧（待更新）_1985625491241672705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ApplySageAttention`
- `LoraLoaderModelOnly` ★核心
- `ApplySageAttention`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `ImageBatchMulti`
- `INTConstant`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `AILab_QwenVL`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `WanFirstMiddleLastFrameToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `deis_3m_ode`
- `denoise` = `beta57`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`ApplySageAttention`、`ImageResizeKJ`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`ImageBatchMulti`、`INTConstant`、`LoadImage`、`AILab_QwenVL`、`WanFirstMiddleLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
