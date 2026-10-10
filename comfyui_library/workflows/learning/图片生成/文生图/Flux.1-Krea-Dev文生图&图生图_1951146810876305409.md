---
key: Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json
name: Flux.1-Krea-Dev文生图&图生图_1951146810876305409
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json
hash: 1eff3e074f219010
coverage: 0.774194
learned_at: 2026-10-10 20:58:36
nodes: [DualCLIPLoader, VAELoader, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, VAEDecode, easy showAnything, UNETLoader, RH_Translator, DualCLIPLoader, VAELoader, VAEDecode, UNETLoader, KSampler, SDXL Empty Latent Image (rgthree), RepeatLatentBatch, VAEEncode, RH_Translator, RH_Captioner, Text Concatenate, easy showAnything, LoadImage, LayerUtility: TextBox, KSampler, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, LayerUtility: TextBox, SaveImage, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: [LayerUtility: TextBox, LayerUtility: TextBox, Text Concatenate, SDXL Empty Latent Image (rgthree)]
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 202412543674784, "steps": 20}
discoveries: [次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `SDXL Empty Latent Image (rgthree)` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明]
---

# Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951146810876305409.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `DualCLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `UNETLoader` ★核心
- `RH_Translator`
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SDXL Empty Latent Image (rgthree)`
- `RepeatLatentBatch`
- `VAEEncode` ★核心
- `RH_Translator`
- `RH_Captioner`
- `Text Concatenate`
- `easy showAnything`
- `LoadImage`
- `LayerUtility: TextBox`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `LayerUtility: TextBox`
- `SaveImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `202412543674784`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`DualCLIPLoader`、`VAELoader`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`RH_Translator`、`KSampler`、`RepeatLatentBatch`、`VAEEncode`、`RH_Captioner`、`LoadImage`、`SaveImage`

**缺卡**（4）：`LayerUtility: TextBox`、`LayerUtility: TextBox`、`Text Concatenate`、`SDXL Empty Latent Image (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

## 学习发现

- 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `SDXL Empty Latent Image (rgthree)` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
