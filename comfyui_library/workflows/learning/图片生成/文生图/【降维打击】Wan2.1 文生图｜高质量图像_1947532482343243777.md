---
key: 图片生成/文生图/【降维打击】Wan2.1 文生图｜高质量图像_1947532482343243777.json
name: 【降维打击】Wan2.1 文生图｜高质量图像_1947532482343243777.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【降维打击】Wan2.1 文生图｜高质量图像_1947532482343243777.json
hash: 7ecda7c0e67d556c
coverage: 0.6875
learned_at: 2026-10-07 22:53:00
nodes: [CR Text Concatenate, ShowText, ShowText, RH_Prompter, JjkText, TextCombinerSix, RH_Translator, EmptyLatentImage, WanVideoNAG, CLIPTextEncode, ModelSamplingSD3, VAELoader, FastFilmGrain, easy clearCacheAll, JjkText, easy showAnything, easy cleanGpuUsed, JjkText, JjkText, FastFilmGrain, PathchSageAttentionKJ, UnetLoaderGGUF, LoraLoader, CLIPLoader, VAEDecode, FluxResolutionNode, ImpactSwitch, RH_Prompter, JjkText, SaveImage, KSampler, CLIPTextEncode]
patterns: [text_to_image, lora]
missing: [CR Text Concatenate, easy cleanGpuUsed, easy clearCacheAll]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 524029734907686, "steps": 10, "strength_clip": 1, "strength_model": 1, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/【降维打击】Wan2.1 文生图｜高质量图像_1947532482343243777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1947532482343243777.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
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
- `easy cleanGpuUsed`
- `JjkText`
- `JjkText`
- `FastFilmGrain`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `FluxResolutionNode`
- `ImpactSwitch`
- `RH_Prompter`
- `JjkText`
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `524029734907686`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **69%**（22/32）

**有卡**：`ShowText`、`RH_Prompter`、`TextCombinerSix`、`RH_Translator`、`EmptyLatentImage`、`WanVideoNAG`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAELoader`、`FastFilmGrain`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`LoraLoader`、`CLIPLoader`、`VAEDecode`、`FluxResolutionNode`、`SaveImage`、`KSampler`

**缺卡**（3）：`CR Text Concatenate`、`easy cleanGpuUsed`、`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoraLoader、LoraLoader

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
