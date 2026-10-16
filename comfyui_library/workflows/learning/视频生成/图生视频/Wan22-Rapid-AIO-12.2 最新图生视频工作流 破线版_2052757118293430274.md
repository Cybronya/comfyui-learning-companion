---
key: 视频生成/图生视频/Wan22-Rapid-AIO-12.2 最新图生视频工作流 破线版_2052757118293430274.json
name: Wan22-Rapid-AIO-12.2 最新图生视频工作流 破线版_2052757118293430274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052757118293430274.json
hash: 09219c009b6208bf
coverage: 0.863636
learned_at: 2026-10-15 22:37:32
nodes: [VAEDecode, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoVACEStartToEndFrame, easy cleanGpuUsed, SimpleMath+, LoraLoader, WanVaceToVideo, LoadImage, KSampler, SaveLatent, VHS_VideoCombine, Fast Groups Bypasser (rgthree), CLIPTextEncode, CLIPTextEncode, Note, MarkdownNote, Int, Int, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v12.2.safetensors", "denoise": 1, "lora_name": "VBVR-low_noise_lora.safetensors", "sampler_name": "sa_solver", "scheduler": "beta", "seed": 291112861242414, "steps": 4, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan22-Rapid-AIO-12.2 最新图生视频工作流 破线版_2052757118293430274.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052757118293430274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoVACEStartToEndFrame`
- `easy cleanGpuUsed`
- `SimpleMath+`
- `LoraLoader` ★核心
- `WanVaceToVideo`
- `LoadImage`
- `KSampler` ★核心
- `SaveLatent`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `MarkdownNote`
- `Int`
- `Int`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `VBVR-low_noise_lora.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `291112861242414`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v12.2.safetensors`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`VAEDecode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVideoVACEStartToEndFrame`、`easy cleanGpuUsed`、`SimpleMath+`、`LoraLoader`、`WanVaceToVideo`、`LoadImage`、`KSampler`、`SaveLatent`、`VHS_VideoCombine`、`CLIPTextEncode`、`Int`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveLatent、LoraLoader、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
