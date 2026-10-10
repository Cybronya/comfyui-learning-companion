---
key: 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-首尾帧_1982051197618135041.json
name: MEGA-v10-WAN2.2-AllInOne-首尾帧_1982051197618135041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-首尾帧_1982051197618135041.json
hash: 2efba229282dae3a
coverage: 1
learned_at: 2026-10-11 02:45:00
nodes: [TrimVideoLatent, VAEDecode, ModelSamplingSD3, INTConstant, ImageResizeKJv2, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, INTConstant, LoadImage, ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVaceToVideo, CLIPTextEncode, CLIPTextEncode, AV_VAELoader, UNETLoader, CLIPLoader, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 192054346835137, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-首尾帧_1982051197618135041.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-首尾帧_1982051197618135041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `INTConstant`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `INTConstant`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AV_VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`INTConstant`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`LoadImage`、`VHS_VideoCombine`、`WanVaceToVideo`、`CLIPTextEncode`、`AV_VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、TrimVideoLatent、AV_VAELoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
