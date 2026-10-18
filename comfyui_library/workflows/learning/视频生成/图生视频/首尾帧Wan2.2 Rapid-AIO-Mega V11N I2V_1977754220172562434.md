---
key: 视频生成/图生视频/首尾帧Wan2.2 Rapid-AIO-Mega V11N I2V_1977754220172562434.json
name: 首尾帧Wan2.2 Rapid-AIO-Mega V11N I2V_1977754220172562434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧Wan2.2 Rapid-AIO-Mega V11N I2V_1977754220172562434.json
hash: 7de1762e1bee9e55
coverage: 0.8125
learned_at: 2026-10-15 22:32:16
nodes: [WanVideoVACEStartToEndFrame, WanVaceToVideo, ModelSamplingSD3, INTConstant, CLIPTextEncode, PrimitiveInt, PrimitiveInt, KSampler, CLIPTextEncode, LoadImage, LoadImage, CheckpointLoaderSimple, Note, DF_Int_to_Float, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v9.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1086171196011762, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/首尾帧Wan2.2 Rapid-AIO-Mega V11N I2V_1977754220172562434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977754220172562434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `WanVideoVACEStartToEndFrame`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `DF_Int_to_Float`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1086171196011762`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v9.safetensors`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`WanVideoVACEStartToEndFrame`、`WanVaceToVideo`、`ModelSamplingSD3`、`INTConstant`、`CLIPTextEncode`、`KSampler`、`LoadImage`、`CheckpointLoaderSimple`、`DF_Int_to_Float`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
