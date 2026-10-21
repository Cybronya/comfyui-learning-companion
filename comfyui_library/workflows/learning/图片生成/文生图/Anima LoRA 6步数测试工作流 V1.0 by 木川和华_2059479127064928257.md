---
key: 图片生成/文生图/Anima LoRA 6步数测试工作流 V1.0 by 木川和华_2059479127064928257.json
name: Anima LoRA 6步数测试工作流 V1.0 by 木川和华_2059479127064928257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima LoRA 6步数测试工作流 V1.0 by 木川和华_2059479127064928257.json
hash: bde6539b0aab9a0d
coverage: 0.428571
learned_at: 2026-10-19 23:02:09
nodes: [UNETLoader, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ModelSamplingAuraFlow, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, SDXL Empty Latent Image (rgthree), SaveImage, easy imageToBase64, Fast Groups Bypasser (rgthree), LayerUtility: TextBox, LayerUtility: TextBox, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, KSampler, KSampler, KSampler, KSampler, KSampler, GetNode, GetNode, LoraLoaderModelOnly, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, ImageConcatMulti, LayerUtility: ImageReel, ImageConcatMulti, AddLabel, AddLabel, AddLabel, AddLabel, AddLabel, PreviewImage, AddLabel, LoraLoaderModelOnly, MarkdownNote, PrimitiveFloat, PrimitiveInt, MarkdownNote, easy saveText]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 0, "steps": 30}
---

# 图片生成/文生图/Anima LoRA 6步数测试工作流 V1.0 by 木川和华_2059479127064928257.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima LoRA 6步数测试工作流 V1.0 by 木川和华_2059479127064928257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（119 个）：
- `UNETLoader` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelSamplingAuraFlow`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SDXL Empty Latent Image (rgthree)`
- `SaveImage`
- `easy imageToBase64`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `ImageConcatMulti`
- `LayerUtility: ImageReel`
- `ImageConcatMulti`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `PreviewImage`
- `AddLabel`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `PrimitiveFloat`
- `PrimitiveInt`
- `MarkdownNote`
- `easy saveText`

## 关键参数

- `seed` = `0`
- `steps` = `30`
- `cfg` = `8`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **43%**（51/119）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`ModelSamplingAuraFlow`、`SDXL Empty Latent Image (rgthree)`、`SaveImage`、`easy imageToBase64`、`LayerUtility: TextBox`、`LoraLoaderModelOnly`、`KSampler`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`ImageConcatMulti`、`AddLabel`、`easy saveText`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、SDXL Empty Latent Image (rgthree)
