---
key: 平台全量/写实摄影Wan 2.1 txt2img_1943608894898008065.json
name: 写实摄影Wan 2.1 txt2img_1943608894898008065
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/写实摄影Wan 2.1 txt2img_1943608894898008065.json
hash: b5d667379634df86
coverage: 0.78125
learned_at: 2026-11-14 01:43:11
nodes: [JjkText, CR Text Concatenate, ShowText, ShowText, RH_Prompter, JjkText, TextCombinerSix, RH_Translator, EmptyLatentImage, WanVideoNAG, CLIPTextEncode, ModelSamplingSD3, VAELoader, FastFilmGrain, easy clearCacheAll, JjkText, easy showAnything, SaveImage, easy cleanGpuUsed, RH_Prompter, KSampler, JjkText, JjkText, FastFilmGrain, PathchSageAttentionKJ, UnetLoaderGGUF, LoraLoader, CLIPLoader, CLIPTextEncode, VAEDecode, FluxResolutionNode, ImpactSwitch]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 524029734907686, "steps": 10, "strength_clip": 1, "strength_model": 1, "width": 1024}
---

# 平台全量/写实摄影Wan 2.1 txt2img_1943608894898008065.json

> 来源文件 `comfyui_library/workflows/平台全量/写实摄影Wan 2.1 txt2img_1943608894898008065.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `JjkText`
- `CR Text Concatenate`
- `ShowText`
- `ShowText`
- `RH_Prompter`
- `JjkText`
- `TextCombinerSix`
- `RH_Translator`
- `EmptyLatentImage` ★核心
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `FastFilmGrain`
- `easy clearCacheAll`
- `JjkText`
- `easy showAnything`
- `SaveImage`
- `easy cleanGpuUsed`
- `RH_Prompter`
- `KSampler` ★核心
- `JjkText`
- `JjkText`
- `FastFilmGrain`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `FluxResolutionNode`
- `ImpactSwitch`

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `524029734907686`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`CR Text Concatenate`、`ShowText`、`RH_Prompter`、`TextCombinerSix`、`RH_Translator`、`EmptyLatentImage`、`WanVideoNAG`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAELoader`、`FastFilmGrain`、`easy clearCacheAll`、`SaveImage`、`easy cleanGpuUsed`、`KSampler`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`LoraLoader`、`CLIPLoader`、`VAEDecode`、`FluxResolutionNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoraLoader、LoRALoader
