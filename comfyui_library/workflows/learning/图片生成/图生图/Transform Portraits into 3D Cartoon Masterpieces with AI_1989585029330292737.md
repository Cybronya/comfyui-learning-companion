---
key: 图片生成/图生图/Transform Portraits into 3D Cartoon Masterpieces with AI_1989585029330292737.json
name: Transform Portraits into 3D Cartoon Masterpieces with AI_1989585029330292737
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Transform Portraits into 3D Cartoon Masterpieces with AI_1989585029330292737.json
hash: c760944bbdba3d5c
coverage: 0.833333
learned_at: 2026-10-23 11:26:36
nodes: [PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, VAEDecode, ApplyPulidFlux, KSampler, PulidFluxModelLoader, ttN concat, LoadImage, DualCLIPLoader, VAELoader, LoraLoader, CLIPTextEncode, Joy_caption_two_load, Joy_extra_options, Joy_caption_two_advanced, SaveImage, EmptyLatentImage, ttN text, CLIPTextEncode, LoraLoaderModelOnly, Note, Note, Note, SUPIR_Upscale, ImageResize+, UNETLoader, Note, ttN text, Note, CheckpointLoaderSimple]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "miluo-flux-pro_模型配置更智能_v1.0", "denoise": 1, "height": 1248, "lora_name": "IP设计_可爱国风盲盒_1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 248847788886349, "steps": 20, "strength_clip": 1, "strength_model": 1, "width": 768}
---

# 图片生成/图生图/Transform Portraits into 3D Cartoon Masterpieces with AI_1989585029330292737.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Transform Portraits into 3D Cartoon Masterpieces with AI_1989585029330292737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `VAEDecode` ★核心
- `ApplyPulidFlux`
- `KSampler` ★核心
- `PulidFluxModelLoader`
- `ttN concat`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `Joy_caption_two_load`
- `Joy_extra_options`
- `Joy_caption_two_advanced`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `ttN text`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `Note`
- `SUPIR_Upscale`
- `ImageResize+`
- `UNETLoader` ★核心
- `Note`
- `ttN text`
- `Note`
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `248847788886349`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `IP设计_可爱国风盲盒_1.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `768`
- `height` = `1248`
- `batch_size` = `1`
- `checkpoint` = `miluo-flux-pro_模型配置更智能_v1.0`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`VAEDecode`、`ApplyPulidFlux`、`KSampler`、`PulidFluxModelLoader`、`ttN concat`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`LoraLoader`、`CLIPTextEncode`、`Joy_caption_two_load`、`Joy_extra_options`、`Joy_caption_two_advanced`、`SaveImage`、`EmptyLatentImage`、`ttN text`、`LoraLoaderModelOnly`、`SUPIR_Upscale`、`ImageResize+`、`UNETLoader`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage
