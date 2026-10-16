---
key: 视频生成/图生视频/wan2.2图生视频-加速工作流_1950763373552164866.json
name: wan2.2图生视频-加速工作流_1950763373552164866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950763373552164866.json
hash: f1be0b3e8b3ee8f1
coverage: 0.888889
learned_at: 2026-10-15 22:30:56
nodes: [TextBox, TextBox, CR Text Replace, RH_Captioner, easy showAnything, Wan_video_prompt_generator, easy int, TextBox, easy showAnything, RH_Captioner, easy ifElse, WanImageToVideo, SimpleMath+, DF_Integer, ModelSamplingSD3, KSampler, UNETLoader, VAELoader, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPLoader, CLIPTextEncode, VAEDecode, VHS_VideoCombine, PrimitiveBoolean, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 979544989028601, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2图生视频-加速工作流_1950763373552164866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950763373552164866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `TextBox`
- `TextBox`
- `CR Text Replace`
- `RH_Captioner`
- `easy showAnything`
- `Wan_video_prompt_generator`
- `easy int`
- `TextBox`
- `easy showAnything`
- `RH_Captioner`
- `easy ifElse`
- `WanImageToVideo`
- `SimpleMath+`
- `DF_Integer`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `LoadImage`

## 关键参数

- `seed` = `979544989028601`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`TextBox`、`CR Text Replace`、`RH_Captioner`、`Wan_video_prompt_generator`、`easy int`、`WanImageToVideo`、`SimpleMath+`、`DF_Integer`、`ModelSamplingSD3`、`KSampler`、`UNETLoader`、`VAELoader`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`PrimitiveBoolean`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan_video_prompt_generator

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
