---
key: 图片生成/图生图/【电商】Wan2.1 模特洗图（无脸部控制）_1953345654779248641.json
name: 【电商】Wan2.1 模特洗图（无脸部控制）_1953345654779248641
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【电商】Wan2.1 模特洗图（无脸部控制）_1953345654779248641.json
hash: cd6eb24baea7b456
coverage: 0.923077
learned_at: 2026-10-23 11:50:59
nodes: [LoraLoader, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, CR Text Concatenate, CLIPLoader, VAELoader, CFGZeroStarAndInit, LoraLoader, LoraLoader, UNETLoader, KSampler, CLIPTextEncode, CLIPTextEncode, VAEEncode, VAEDecode, UpscaleModelLoader, LoadImage, ImageUpscaleWithModel, easy cleanGpuUsed, ShowText, PreviewImage, SaveImage, LayerUtility: ImageReel, RHHiddenNodes, RHHiddenNodes, Note]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 829543752571394, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【电商】Wan2.1 模特洗图（无脸部控制）_1953345654779248641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【电商】Wan2.1 模特洗图（无脸部控制）_1953345654779248641.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `LoraLoader` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `CR Text Concatenate`
- `CLIPLoader`
- `VAELoader`
- `CFGZeroStarAndInit`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `LoadImage`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `ShowText`
- `PreviewImage`
- `SaveImage`
- `LayerUtility: ImageReel`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Note`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `829543752571394`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`LoraLoader`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`CR Text Concatenate`、`CLIPLoader`、`VAELoader`、`CFGZeroStarAndInit`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`UpscaleModelLoader`、`LoadImage`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`ShowText`、`SaveImage`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
