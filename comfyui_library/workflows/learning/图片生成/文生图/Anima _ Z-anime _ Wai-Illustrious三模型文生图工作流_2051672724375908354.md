---
key: 图片生成/文生图/Anima _ Z-anime _ Wai-Illustrious三模型文生图工作流_2051672724375908354.json
name: Anima _ Z-anime _ Wai-Illustrious三模型文生图工作流_2051672724375908354
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima _ Z-anime _ Wai-Illustrious三模型文生图工作流_2051672724375908354.json
hash: 8027cdbf08494e81
coverage: 0.818182
learned_at: 2026-10-19 22:45:21
nodes: [KSampler, ModelSamplingAuraFlow, CLIPTextEncode, PrimitiveNode, PrimitiveFloat, PrimitiveInt, EmptyLatentImage, CLIPTextEncode, ModelSamplingAuraFlow, PrimitiveNode, KSampler, EmptySD3LatentImage, CLIPTextEncode, KSampler, EmptySD3LatentImage, VAEDecode, VAEDecode, VRAM_Debug, VAEDecode, VRAM_Debug, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, VRAM_Debug, Fast Groups Bypasser (rgthree), PreviewImage, SaveImage, AddLabel, PreviewImage, AddLabel, ImageConcatMulti, SaveImage, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, CheckpointLoaderSimple, Text Multiline, UNETLoader, AddLabel]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "waiIllustriousSDXL_v170.safetensors", "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "normal", "seed": 1024, "steps": 30, "width": 896}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Anima _ Z-anime _ Wai-Illustrious三模型文生图工作流_2051672724375908354.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima _ Z-anime _ Wai-Illustrious三模型文生图工作流_2051672724375908354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveFloat`
- `PrimitiveInt`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `PrimitiveNode`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VRAM_Debug`
- `VAEDecode` ★核心
- `VRAM_Debug`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `llama_cpp_model_loader`
- `VRAM_Debug`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `SaveImage`
- `AddLabel`
- `PreviewImage`
- `AddLabel`
- `ImageConcatMulti`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `Text Multiline`
- `UNETLoader` ★核心
- `AddLabel`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1024`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `896`
- `height` = `1152`
- `batch_size` = `1`
- `checkpoint` = `waiIllustriousSDXL_v170.safetensors`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`KSampler`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`EmptyLatentImage`、`EmptySD3LatentImage`、`VAEDecode`、`VRAM_Debug`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`SaveImage`、`AddLabel`、`ImageConcatMulti`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CheckpointLoaderSimple`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
