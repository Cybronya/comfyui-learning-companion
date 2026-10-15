---
key: 视频生成/文生视频/HUNYUAN 1.5 T2V 4步极速版_2073281127351144450.json
name: HUNYUAN 1.5 T2V 4步极速版_2073281127351144450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/HUNYUAN 1.5 T2V 4步极速版_2073281127351144450.json
hash: aee79676402355cb
coverage: 0.966667
learned_at: 2026-10-15 22:44:26
nodes: [CLIPTextEncode, HunyuanVideo15LatentUpscaleWithModel, BasicScheduler, CFGGuider, ModelSamplingSD3, KSamplerSelect, VAELoader, CFGGuider, PathchSageAttentionKJ, HunyuanVideo15SuperResolution, KSamplerSelect, VHS_VideoCombine, LatentUpscaleModelLoader, RandomNoise, RandomNoise, UNETLoader, MarkdownNote, SamplerCustomAdvanced, VAEDecode, SamplerCustomAdvanced, VAEDecode, PathchSageAttentionKJ, DualCLIPLoader, UNETLoader, EmptyHunyuanVideo15Latent, VHS_VideoCombine, BasicScheduler, LoraLoader, CLIPTextEncode, ModelSamplingSD3]
patterns: [lora]
missing: []
parameters: {"lora_name": "hunyuanvideo1.5_t2v_480p_lightx2v_4step_lora_rank_32_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/文生视频/HUNYUAN 1.5 T2V 4步极速版_2073281127351144450.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/HUNYUAN 1.5 T2V 4步极速版_2073281127351144450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `HunyuanVideo15LatentUpscaleWithModel`
- `BasicScheduler`
- `CFGGuider`
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
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
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `EmptyHunyuanVideo15Latent`
- `VHS_VideoCombine`
- `BasicScheduler`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `hunyuanvideo1.5_t2v_480p_lightx2v_4step_lora_rank_32_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`CLIPTextEncode`、`HunyuanVideo15LatentUpscaleWithModel`、`BasicScheduler`、`CFGGuider`、`ModelSamplingSD3`、`KSamplerSelect`、`VAELoader`、`PathchSageAttentionKJ`、`HunyuanVideo15SuperResolution`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`RandomNoise`、`UNETLoader`、`SamplerCustomAdvanced`、`VAEDecode`、`DualCLIPLoader`、`EmptyHunyuanVideo15Latent`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyHunyuanVideo15Latent
