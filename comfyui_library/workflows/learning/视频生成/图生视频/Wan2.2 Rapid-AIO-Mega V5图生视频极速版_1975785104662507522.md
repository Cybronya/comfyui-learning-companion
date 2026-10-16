---
key: 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V5图生视频极速版_1975785104662507522.json
name: Wan2.2 Rapid-AIO-Mega V5图生视频极速版_1975785104662507522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975785104662507522.json
hash: 26dce74e4a9cea5a
coverage: 0.882353
learned_at: 2026-10-15 22:32:09
nodes: [LoadImage, JWInteger, Note, JWInteger, Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVACEStartToEndFrame, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, ApplySageAttention, ModelSamplingSD3, WanVaceToVideo, KSampler, VAEDecode, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v5.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "beta", "seed": 789419981205462, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V5图生视频极速版_1975785104662507522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975785104662507522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `LoadImage`
- `JWInteger`
- `Note`
- `JWInteger`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVACEStartToEndFrame`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CR Prompt Text`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v5.safetensors`
- `seed` = `789419981205462`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`LoadImage`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVACEStartToEndFrame`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`ApplySageAttention`、`ModelSamplingSD3`、`WanVaceToVideo`、`KSampler`、`VAEDecode`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Prompt Text、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
