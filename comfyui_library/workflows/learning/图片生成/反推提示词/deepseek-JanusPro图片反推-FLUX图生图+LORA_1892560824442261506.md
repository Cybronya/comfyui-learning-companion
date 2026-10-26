---
key: 图片生成/反推提示词/deepseek-JanusPro图片反推-FLUX图生图+LORA_1892560824442261506.json
name: deepseek-JanusPro图片反推-FLUX图生图+LORA_1892560824442261506
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/deepseek-JanusPro图片反推-FLUX图生图+LORA_1892560824442261506.json
hash: 6e6a8726de1d2884
coverage: 0.857143
learned_at: 2026-10-26 01:46:44
nodes: [DualCLIPLoader, VAELoader, DifferentialDiffusion, ConditioningZeroOut, CLIPTextEncode, KSampler, VAEDecode, JanusImageUnderstanding, ShowText|pysssss, ShowText|pysssss, LayerUtility: PurgeVRAM, JanusModelLoader, EmptyLatentImage, ArgosTranslateTextNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, LoadImage, Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "normal", "seed": 167097440859209, "steps": 20, "width": 512}
---

# 图片生成/反推提示词/deepseek-JanusPro图片反推-FLUX图生图+LORA_1892560824442261506.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/deepseek-JanusPro图片反推-FLUX图生图+LORA_1892560824442261506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `DualCLIPLoader`
- `VAELoader`
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JanusImageUnderstanding`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `JanusModelLoader`
- `EmptyLatentImage` ★核心
- `ArgosTranslateTextNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `167097440859209`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `512`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`DualCLIPLoader`、`VAELoader`、`DifferentialDiffusion`、`ConditioningZeroOut`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`JanusImageUnderstanding`、`LayerUtility: PurgeVRAM`、`JanusModelLoader`、`EmptyLatentImage`、`ArgosTranslateTextNode`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
