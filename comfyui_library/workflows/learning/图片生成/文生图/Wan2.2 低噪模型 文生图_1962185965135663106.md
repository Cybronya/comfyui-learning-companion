---
key: Wan2.2 低噪模型 文生图_1962185965135663106.json
name: Wan2.2 低噪模型 文生图_1962185965135663106
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 低噪模型 文生图_1962185965135663106.json
hash: 044f7227419f6dd2
coverage: 0.823529
learned_at: 2026-10-10 20:59:13
nodes: [WanVideoNAG, ModelSamplingSD3, CLIPTextEncode, VAELoader, CLIPTextEncode, VAEDecode, FastFilmGrain, KSampler, CR Upscale Image, CLIPLoader, LoraLoader, PathchSageAttentionKJ, easy cleanGpuUsed, easy clearCacheAll, EmptyLatentImage, SaveImage, UNETLoader]
patterns: [text_to_image, lora]
missing: [easy cleanGpuUsed, easy clearCacheAll, CR Upscale Image]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1600, "lora_name": "lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 842476343600367, "steps": 8, "strength_clip": 1, "strength_model": 1, "width": 904}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Wan2.2 低噪模型 文生图_1962185965135663106.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 低噪模型 文生图_1962185965135663106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `WanVideoNAG`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `FastFilmGrain`
- `KSampler` ★核心
- `CR Upscale Image`
- `CLIPLoader`
- `LoraLoader` ★核心
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `UNETLoader` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `842476343600367`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `904`
- `height` = `1600`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`WanVideoNAG`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`FastFilmGrain`、`KSampler`、`CLIPLoader`、`LoraLoader`、`PathchSageAttentionKJ`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`

**缺卡**（3）：`easy cleanGpuUsed`、`easy clearCacheAll`、`CR Upscale Image`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
