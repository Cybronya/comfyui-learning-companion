---
key: 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-姿态视频引导加参考_1968251354269536257.json
name: MEGA Merge-WAN2.2-AllInOne-姿态视频引导加参考_1968251354269536257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-姿态视频引导加参考_1968251354269536257.json
hash: be821a4b58b309ad
coverage: 1
learned_at: 2026-10-10 23:00:44
nodes: [TrimVideoLatent, VAEDecode, CLIPTextEncode, VHS_VideoCombine, WanVaceToVideo, INTConstant, ImageResizeKJv2, GetImageSizeAndCount, CLIPTextEncode, VHS_LoadVideo, Miaoshouai_Tagger, AIO_Preprocessor, LoadImage, CheckpointLoaderSimple, KSampler, ModelSamplingSD3, INTConstant]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-姿态视频引导加参考_1968251354269536257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-姿态视频引导加参考_1968251354269536257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `Miaoshouai_Tagger`
- `AIO_Preprocessor`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `INTConstant`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`
- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanVaceToVideo`、`INTConstant`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`Miaoshouai_Tagger`、`AIO_Preprocessor`、`LoadImage`、`CheckpointLoaderSimple`、`KSampler`、`ModelSamplingSD3`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、TrimVideoLatent、GetImageSizeAndCount、ImageResizeKJv2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
