---
key: 图片生成/图生图/wan2.2低频超真实+图生图V3_1951075062482972674.json
name: wan2.2低频超真实+图生图V3_1951075062482972674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2低频超真实+图生图V3_1951075062482972674.json
hash: 9754a2e08536456e
coverage: 0.952381
learned_at: 2026-10-23 11:46:02
nodes: [LoraLoader, CLIPTextEncode, CLIPLoader, CR Text Concatenate, UNETLoader, ShowText|pysssss, LoraLoader, CLIPTextEncode, LoraLoader, RHHiddenNodes, VAELoader, RH_LLMAPI_NODE, RH_Captioner, ImageScaleDownToSize, VAEEncode, SaveImage, LoadImage, RHHiddenNodes, KSampler, VAEDecode, CFGZeroStarAndInit]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 538284665218932, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan2.2低频超真实+图生图V3_1951075062482972674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2低频超真实+图生图V3_1951075062482972674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `RHHiddenNodes`
- `VAELoader`
- `RH_LLMAPI_NODE`
- `RH_Captioner`
- `ImageScaleDownToSize`
- `VAEEncode` ★核心
- `SaveImage`
- `LoadImage`
- `RHHiddenNodes`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CFGZeroStarAndInit`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `538284665218932`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`LoraLoader`、`CLIPTextEncode`、`CLIPLoader`、`CR Text Concatenate`、`UNETLoader`、`RHHiddenNodes`、`VAELoader`、`RH_LLMAPI_NODE`、`RH_Captioner`、`ImageScaleDownToSize`、`VAEEncode`、`SaveImage`、`LoadImage`、`KSampler`、`VAEDecode`、`CFGZeroStarAndInit`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
