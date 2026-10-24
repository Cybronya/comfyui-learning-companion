---
key: 图片生成/图生图/SUPERHERO pose generator Fast LCM  SDXL Openpose_1862363789558743041.json
name: SUPERHERO pose generator Fast LCM  SDXL Openpose_1862363789558743041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SUPERHERO pose generator Fast LCM  SDXL Openpose_1862363789558743041.json
hash: ead5d00f99e0aab2
coverage: 0.85
learned_at: 2026-10-23 11:24:10
nodes: [CheckpointLoaderSimple, LoraLoader, FreeU_V2, CLIPSetLastLayer, SDXLResolutionPresets, PrimitiveNode, SDXLPromptStyler, OpenposePreprocessor, SaveImage, Textbox, Textbox, EmptyLatentImage, Seed (rgthree), CLIPTextEncode, CLIPTextEncode, SaveImage, PreviewImage, PreviewImage, KSamplerAdvanced, VAEDecode]
patterns: [lora]
missing: []
parameters: {"batch_size": 16, "cfg": 8, "checkpoint": "crystalClearXL_ccxl.safetensors", "denoise": "sgm_uniform", "height": 1024, "lora_name": "pytorch_lora_weights_xl_lcm.safetensors", "sampler_name": 1.3, "scheduler": "lcm", "seed": "enable", "steps": "randomize", "strength_clip": 1, "strength_model": 1, "width": 1024}
---

# 图片生成/图生图/SUPERHERO pose generator Fast LCM  SDXL Openpose_1862363789558743041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SUPERHERO pose generator Fast LCM  SDXL Openpose_1862363789558743041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `FreeU_V2`
- `CLIPSetLastLayer`
- `SDXLResolutionPresets`
- `PrimitiveNode`
- `SDXLPromptStyler`
- `OpenposePreprocessor`
- `SaveImage`
- `Textbox`
- `Textbox`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `crystalClearXL_ccxl.safetensors`
- `lora_name` = `pytorch_lora_weights_xl_lcm.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `16`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1.3`
- `scheduler` = `lcm`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CheckpointLoaderSimple`、`LoraLoader`、`FreeU_V2`、`CLIPSetLastLayer`、`SDXLResolutionPresets`、`SDXLPromptStyler`、`OpenposePreprocessor`、`SaveImage`、`Textbox`、`EmptyLatentImage`、`Seed (rgthree)`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、OpenposePreprocessor、KSamplerAdvanced、Seed (rgthree)、LoraLoader
