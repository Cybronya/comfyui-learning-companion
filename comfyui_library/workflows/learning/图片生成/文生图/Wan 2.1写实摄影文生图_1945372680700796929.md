---
key: Wan 2.1写实摄影文生图_1945372680700796929.json
name: Wan 2.1写实摄影文生图_1945372680700796929
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan 2.1写实摄影文生图_1945372680700796929.json
hash: e195685a91ca9185
coverage: 0.863636
learned_at: 2026-10-10 20:59:13
nodes: [EmptyLatentImage, KSampler, VAEDecode, VAELoader, LoraLoader, WanVideoNAG, ModelSamplingSD3, SaveImage, PathchSageAttentionKJ, CLIPLoader, FluxResolutionNode, LoraLoaderModelOnly, UNETLoader, JjkText, JjkText, CR Text Concatenate, RH_Prompter, ShowText, RH_Translator, CLIPTextEncode, FastFilmGrain, CLIPTextEncode]
patterns: [text_to_image, lora]
missing: [CR Text Concatenate]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 524029734907686, "steps": 10, "strength_clip": 1, "strength_model": 1, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# Wan 2.1写实摄影文生图_1945372680700796929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan 2.1写实摄影文生图_1945372680700796929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `LoraLoader` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `SaveImage`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `FluxResolutionNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `JjkText`
- `JjkText`
- `CR Text Concatenate`
- `RH_Prompter`
- `ShowText`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `FastFilmGrain`
- `CLIPTextEncode` ★核心

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

覆盖率 **86%**（19/22）

**有卡**：`EmptyLatentImage`、`KSampler`、`VAEDecode`、`VAELoader`、`LoraLoader`、`WanVideoNAG`、`ModelSamplingSD3`、`SaveImage`、`PathchSageAttentionKJ`、`CLIPLoader`、`FluxResolutionNode`、`LoraLoaderModelOnly`、`UNETLoader`、`RH_Prompter`、`ShowText`、`RH_Translator`、`CLIPTextEncode`、`FastFilmGrain`

**缺卡**（1）：`CR Text Concatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
