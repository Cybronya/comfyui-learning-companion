---
key: 视频生成/文生视频/MEGA_V2_AllInOne_Wan2.2_文生视频_1970012767400960001.json
name: MEGA_V2_AllInOne_Wan2.2_文生视频_1970012767400960001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1970012767400960001.json
hash: d110abe367359e4d
coverage: 0.944444
learned_at: 2026-10-15 22:43:47
nodes: [KSampler, TrimVideoLatent, WanVaceToVideo, INTConstant, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ConcatTextOfUtils, VAEDecode, VHS_VideoCombine, Wan22PromptSelector, ShowText|pysssss, LoadImage, CheckpointLoaderSimple, INTConstant, INTConstant, RH_LLMAPI_NODE, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v2.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA_V2_AllInOne_Wan2.2_文生视频_1970012767400960001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1970012767400960001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `KSampler` ★核心
- `TrimVideoLatent`
- `WanVaceToVideo`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ConcatTextOfUtils`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `ShowText|pysssss`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `INTConstant`
- `INTConstant`
- `RH_LLMAPI_NODE`
- `CR Text`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v2.safetensors`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`KSampler`、`TrimVideoLatent`、`WanVaceToVideo`、`INTConstant`、`CLIPTextEncode`、`ModelSamplingSD3`、`ConcatTextOfUtils`、`VAEDecode`、`VHS_VideoCombine`、`Wan22PromptSelector`、`LoadImage`、`CheckpointLoaderSimple`、`RH_LLMAPI_NODE`、`CR Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、TrimVideoLatent、Wan22PromptSelector、INTConstant

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
