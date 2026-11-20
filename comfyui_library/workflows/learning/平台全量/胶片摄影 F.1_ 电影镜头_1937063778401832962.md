---
key: 平台全量/胶片摄影 F.1_ 电影镜头_1937063778401832962.json
name: 胶片摄影 F.1_ 电影镜头_1937063778401832962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/胶片摄影 F.1_ 电影镜头_1937063778401832962.json
hash: 010bcc516d882dd3
coverage: 0.83871
learned_at: 2026-11-14 02:30:55
nodes: [DualCLIPLoader, SamplerCustomAdvanced, RandomNoise, VAELoader, BasicScheduler, EmptyLatentImage, BasicGuider, RandomNoise, VAEDecode, KSamplerSelect, VAEEncode, ImageUpscaleWithModel, UpscaleModelLoader, BasicScheduler, UNETLoader, VAEDecode, SamplerCustomAdvanced, CLIPTextEncode, TextCombinerTwo, JjkText, RH_Prompter, ShowText|pysssss, TextCombinerTwo, PreviewImage, PreviewImage, SaveImage, FluxResolutionNode, LayerColor: Brightness & Contrast, LoraLoader, JjkText, RH_Translator]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1280, "lora_name": "FLUX.吴冠中水乡风CNGHWCS_v1.0.safetensors", "strength_clip": 0.7500000000000001, "strength_model": 0.7500000000000001, "width": 1024}
---

# 平台全量/胶片摄影 F.1_ 电影镜头_1937063778401832962.json

> 来源文件 `comfyui_library/workflows/平台全量/胶片摄影 F.1_ 电影镜头_1937063778401832962.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `DualCLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAELoader`
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `BasicGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `BasicScheduler`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `TextCombinerTwo`
- `JjkText`
- `RH_Prompter`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `FluxResolutionNode`
- `LayerColor: Brightness & Contrast`
- `LoraLoader` ★核心
- `JjkText`
- `RH_Translator`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `lora_name` = `FLUX.吴冠中水乡风CNGHWCS_v1.0.safetensors`
- `strength_model` = `0.7500000000000001`
- `strength_clip` = `0.7500000000000001`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`DualCLIPLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`VAELoader`、`BasicScheduler`、`EmptyLatentImage`、`BasicGuider`、`VAEDecode`、`KSamplerSelect`、`VAEEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`UNETLoader`、`CLIPTextEncode`、`TextCombinerTwo`、`RH_Prompter`、`SaveImage`、`FluxResolutionNode`、`LayerColor: Brightness & Contrast`、`LoraLoader`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、KSamplerSelect、SamplerCustomAdvanced、VAEEncode
