---
key: 视频生成/图生视频/wan2.2-14B-rapid 图生视频-最新加速模型_1950737220787458049.json
name: wan2.2-14B-rapid 图生视频-最新加速模型_1950737220787458049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-14B-rapid 图生视频-最新加速模型_1950737220787458049.json
hash: bb0aae47e0b853cf
coverage: 0.857143
learned_at: 2026-10-15 22:30:56
nodes: [DF_Integer, easy int, CLIPTextEncode, CLIPTextEncode, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, CR Text Replace, RH_Captioner, easy showAnything, TextBox, easy ifElse, Note, ModelSamplingSD3, SimpleMath+, VAELoader, CLIPLoader, VAEDecode, LayerUtility: PurgeVRAM, VHS_VideoCombine, TextBox, easy showAnything, TextBox, LoadImage, RH_Captioner, PrimitiveBoolean, WanImageToVideo, KSampler, Wan_video_prompt_generator]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 0, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2-14B-rapid 图生视频-最新加速模型_1950737220787458049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950737220787458049.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `DF_Integer`
- `easy int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text Replace`
- `RH_Captioner`
- `easy showAnything`
- `TextBox`
- `easy ifElse`
- `Note`
- `ModelSamplingSD3`
- `SimpleMath+`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `TextBox`
- `easy showAnything`
- `TextBox`
- `LoadImage`
- `RH_Captioner`
- `PrimitiveBoolean`
- `WanImageToVideo`
- `KSampler` ★核心
- `Wan_video_prompt_generator`

## 关键参数

- `seed` = `0`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`DF_Integer`、`easy int`、`CLIPTextEncode`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text Replace`、`RH_Captioner`、`TextBox`、`ModelSamplingSD3`、`SimpleMath+`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`LoadImage`、`PrimitiveBoolean`、`WanImageToVideo`、`KSampler`、`Wan_video_prompt_generator`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan_video_prompt_generator

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
