---
key: 视频生成/文生视频/wan2.2文生视频-RAPID_1952688538144993282.json
name: wan2.2文生视频-RAPID_1952688538144993282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频-RAPID_1952688538144993282.json
hash: 39df2d333f5ee7e2
coverage: 0.941176
learned_at: 2026-10-15 22:43:38
nodes: [UNETLoader, ModelSamplingSD3, VAELoader, KSampler, VAEDecode, LayerUtility: PurgeVRAM, easy showAnything, RH_Translator, Wan_video_prompt_generator, TextCombinerSix, easy cleanGpuUsed, CLIPLoader, CLIPTextEncode, RH_Translator, CLIPTextEncode, EmptyHunyuanLatentVideo, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 887375440310681, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2文生视频-RAPID_1952688538144993282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1952688538144993282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `RH_Translator`
- `Wan_video_prompt_generator`
- `TextCombinerSix`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `887375440310681`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`RH_Translator`、`Wan_video_prompt_generator`、`TextCombinerSix`、`easy cleanGpuUsed`、`CLIPLoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、Wan_video_prompt_generator

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
