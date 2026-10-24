---
key: 图片生成/图生图/Flex.2+DEEPSEEK图片反推洗图专用工作流_1925012752870350849.json
name: Flex.2+DEEPSEEK图片反推洗图专用工作流_1925012752870350849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.2+DEEPSEEK图片反推洗图专用工作流_1925012752870350849.json
hash: dafae1858f01e69d
coverage: 0.92
learned_at: 2026-10-23 10:56:01
nodes: [SaveImage, CLIPTextEncode, FlexGuidance, ImpactInt, VAELoader, LayerUtility: PurgeVRAM, Flex2Conditioner, KSampler, UpscaleModelLoader, ImageUpscaleWithModel, VAEDecode, EmptySD3LatentImage, ApplyFBCacheOnModel, UNETLoader, ConditioningZeroOut, DualCLIPLoader, LoraLoader, RH_Translator, easy showAnything, easy showAnything, CR Prompt Text, LoadImage, JanusImageUnderstanding, RH_Captioner, JanusModelLoader]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "wangyiAI小红书超甜美可爱女生.safetensors", "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/Flex.2+DEEPSEEK图片反推洗图专用工作流_1925012752870350849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.2+DEEPSEEK图片反推洗图专用工作流_1925012752870350849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `SaveImage`
- `CLIPTextEncode` ★核心
- `FlexGuidance`
- `ImpactInt`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `Flex2Conditioner`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `ApplyFBCacheOnModel`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `RH_Translator`
- `easy showAnything`
- `easy showAnything`
- `CR Prompt Text`
- `LoadImage`
- `JanusImageUnderstanding`
- `RH_Captioner`
- `JanusModelLoader`

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

覆盖率 **92%**（23/25）

**有卡**：`SaveImage`、`CLIPTextEncode`、`FlexGuidance`、`ImpactInt`、`VAELoader`、`LayerUtility: PurgeVRAM`、`Flex2Conditioner`、`KSampler`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEDecode`、`EmptySD3LatentImage`、`ApplyFBCacheOnModel`、`UNETLoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`LoraLoader`、`RH_Translator`、`CR Prompt Text`、`LoadImage`、`JanusImageUnderstanding`、`RH_Captioner`、`JanusModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、FlexGuidance
