---
key: 图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json
name: Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json
hash: 22248cd96b34a0fc
coverage: 0.866667
learned_at: 2026-10-20 00:18:43
nodes: [CLIPLoader, VAELoader, PreviewImage, llama_cpp_model_loader, CR Prompt Text, EmptyLatentImage, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, llama_cpp_instruct_adv, ShowText|pysssss, KSampler, CLIPTextEncode, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "er_sde", "scheduler": "beta", "seed": 620754103798044, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `llama_cpp_model_loader`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `620754103798044`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAELoader`、`llama_cpp_model_loader`、`CR Prompt Text`、`EmptyLatentImage`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`llama_cpp_instruct_adv`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
