---
key: 视频生成/图生视频/WH-AI-Studio-Wan2.2-运镜加速完美版-图生视频_2015621082249695233.json
name: WH-AI-Studio-Wan2.2-运镜加速完美版-图生视频_2015621082249695233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WH-AI-Studio-Wan2.2-运镜加速完美版-图生视频_2015621082249695233.json
hash: 0e700aea0a3fe67f
coverage: 0.972222
learned_at: 2026-10-15 22:34:39
nodes: [LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPVisionLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, PainterI2V, CLIPVisionEncode, wanBlockSwap, Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), VAEDecode, easy cleanGpuUsed, ModelSamplingSD3, ModelSamplingSD3, MathExpression|pysssss, Mute / Bypass Repeater (rgthree), Fast Muter (rgthree), WanMoeKSampler, RIFE VFI, VHS_VideoCombine, CLIPTextEncode, VHS_VideoCombine, CLIPTextEncode, LoadImage, ImpactInt, Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/WH-AI-Studio-Wan2.2-运镜加速完美版-图生视频_2015621082249695233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2015621082249695233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `PainterI2V`
- `CLIPVisionEncode`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Muter (rgthree)`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MathExpression|pysssss`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Muter (rgthree)`
- `WanMoeKSampler` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImpactInt`
- `Int`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelPatchTorchSettings`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterI2V`、`CLIPVisionEncode`、`Mute / Bypass Repeater (rgthree)`、`Fast Muter (rgthree)`、`VAEDecode`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`MathExpression|pysssss`、`WanMoeKSampler`、`RIFE VFI`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoadImage`、`ImpactInt`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
