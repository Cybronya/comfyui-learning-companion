---
key: 视频生成/文生视频/res_multistep 2.46×零质量损加速｜MiniMax-H3文生视频RH版_2089008529712705537.json
name: res_multistep 2.46×零质量损加速｜MiniMax-H3文生视频RH版_2089008529712705537
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/res_multistep 2.46×零质量损加速｜MiniMax-H3文生视频RH版_2089008529712705537.json
hash: 7e239bdc385f058f
coverage: 0.891892
learned_at: 2026-10-11 21:19:52
nodes: [RHMiniMaxH3DirectTextEncoderLoader, RHMiniMaxH3DirectModelLoader, RHMiniMaxH3DirectVAELoader, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3DecodeAV, CreateVideo, SaveVideo, RHMiniMaxH3T2VATarget, RHMiniMaxH3T2VATextEncode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/res_multistep 2.46×零质量损加速｜MiniMax-H3文生视频RH版_2089008529712705537.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/res_multistep 2.46×零质量损加速｜MiniMax-H3文生视频RH版_2089008529712705537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `RHMiniMaxH3DirectTextEncoderLoader`
- `RHMiniMaxH3DirectModelLoader`
- `RHMiniMaxH3DirectVAELoader`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3DualSigmaSampler` ★核心
- `RHMiniMaxH3DecodeAV`
- `CreateVideo`
- `SaveVideo`
- `RHMiniMaxH3T2VATarget`
- `RHMiniMaxH3T2VATextEncode`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`RHMiniMaxH3DirectTextEncoderLoader`、`RHMiniMaxH3DirectModelLoader`、`RHMiniMaxH3DirectVAELoader`、`RHMiniMaxH3EmptyAVLatent`、`RHMiniMaxH3DualSigmaSampler`、`RHMiniMaxH3DecodeAV`、`CreateVideo`、`SaveVideo`、`RHMiniMaxH3T2VATarget`、`RHMiniMaxH3T2VATextEncode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
