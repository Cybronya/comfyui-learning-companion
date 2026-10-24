---
key: 图片生成/图生图/Flex.2+LORA图片反推洗图专用工作流_1917435411239735297.json
name: Flex.2+LORA图片反推洗图专用工作流_1917435411239735297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.2+LORA图片反推洗图专用工作流_1917435411239735297.json
hash: c6eec850a5e04a1e
coverage: 0.916667
learned_at: 2026-10-23 10:56:02
nodes: [SaveImage, CR Prompt Text, GoogleTranslateTextNode, CLIPTextEncode, FlexGuidance, easy showAnything, ImpactInt, VAELoader, LayerUtility: PurgeVRAM, Flex2Conditioner, KSampler, Note Plus (mtb), UpscaleModelLoader, ImageUpscaleWithModel, VAEDecode, EmptySD3LatentImage, ApplyFBCacheOnModel, UNETLoader, ConditioningZeroOut, easy showAnything, DualCLIPLoader, LoadImage, RH_Captioner, LoraLoader]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "wangyiAI小红书超甜美可爱女生.safetensors", "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/Flex.2+LORA图片反推洗图专用工作流_1917435411239735297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.2+LORA图片反推洗图专用工作流_1917435411239735297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SaveImage`
- `CR Prompt Text`
- `GoogleTranslateTextNode`
- `CLIPTextEncode` ★核心
- `FlexGuidance`
- `easy showAnything`
- `ImpactInt`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `Flex2Conditioner`
- `KSampler` ★核心
- `Note Plus (mtb)`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `ApplyFBCacheOnModel`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `easy showAnything`
- `DualCLIPLoader`
- `LoadImage`
- `RH_Captioner`
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `seed` = `726210541184116`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `wangyiAI小红书超甜美可爱女生.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`SaveImage`、`CR Prompt Text`、`GoogleTranslateTextNode`、`CLIPTextEncode`、`FlexGuidance`、`ImpactInt`、`VAELoader`、`LayerUtility: PurgeVRAM`、`Flex2Conditioner`、`KSampler`、`Note Plus (mtb)`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEDecode`、`EmptySD3LatentImage`、`ApplyFBCacheOnModel`、`UNETLoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`LoadImage`、`RH_Captioner`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、FlexGuidance
