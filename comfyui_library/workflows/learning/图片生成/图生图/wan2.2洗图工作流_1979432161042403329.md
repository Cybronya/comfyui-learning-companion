---
key: 图片生成/图生图/wan2.2洗图工作流_1979432161042403329.json
name: wan2.2洗图工作流_1979432161042403329
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2洗图工作流_1979432161042403329.json
hash: 29da2439c0a49d6b
coverage: 0.833333
learned_at: 2026-10-23 11:46:09
nodes: [CLIPLoader, VAELoader, Joy_caption_two_load, Joy_caption_two, ImageResize+, PathchSageAttentionKJ, VAEEncode, LoraLoader, CLIPTextEncode, CLIPTextEncode, KSampler, LoadImage, VAEDecode, Note, SaveImage, UNETLoader, PreviewImage, Note]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "lora_name": "Wan22_A14B_T2V_LOW_Lightning_4steps_lora_250928_rank64_fp16.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 614644988664074, "steps": 6, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan2.2洗图工作流_1979432161042403329.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2洗图工作流_1979432161042403329.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `ImageResize+`
- `PathchSageAttentionKJ`
- `VAEEncode` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `Note`
- `SaveImage`
- `UNETLoader` ★核心
- `PreviewImage`
- `Note`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan22_A14B_T2V_LOW_Lightning_4steps_lora_250928_rank64_fp16.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `614644988664074`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`VAELoader`、`Joy_caption_two_load`、`Joy_caption_two`、`ImageResize+`、`PathchSageAttentionKJ`、`VAEEncode`、`LoraLoader`、`CLIPTextEncode`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
