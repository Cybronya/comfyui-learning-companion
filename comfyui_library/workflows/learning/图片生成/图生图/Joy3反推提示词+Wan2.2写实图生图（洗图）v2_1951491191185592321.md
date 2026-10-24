---
key: 图片生成/图生图/Joy3反推提示词+Wan2.2写实图生图（洗图）v2_1951491191185592321.json
name: Joy3反推提示词+Wan2.2写实图生图（洗图）v2_1951491191185592321
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Joy3反推提示词+Wan2.2写实图生图（洗图）v2_1951491191185592321.json
hash: dab41eb58bf7cece
coverage: 0.8
learned_at: 2026-10-23 11:03:49
nodes: [RH_Captioner, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, CLIPLoader, UNETLoader, LoraLoader, LoraLoader, CLIPTextEncode, VAELoader, VAEEncode, PathchSageAttentionKJ, CFGZeroStarAndInit, DeepTranslatorTextNode, LayerUtility: JoyCaptionBeta1, easy cleanGpuUsed, Note, CR Text Concatenate, CR Text, LayerUtility: ImageReel, SaveImage, Reroute, LoadImage, Note, Note, CLIPTextEncode, Reroute, LoraLoader, ModelSamplingSD3, VAEDecode, SaveImage, LayerUtility: ImageReelComposit, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ShowText|pysssss, DeepTranslatorTextNode, TextInputBasic, LayerUtility: LoadJoyCaptionBeta1Model, ShowText|pysssss, LayerUtility: JoyCaptionBeta1ExtraOptions]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 919052511453328, "steps": 20, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
---

# 图片生成/图生图/Joy3反推提示词+Wan2.2写实图生图（洗图）v2_1951491191185592321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Joy3反推提示词+Wan2.2写实图生图（洗图）v2_1951491191185592321.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `RH_Captioner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `DeepTranslatorTextNode`
- `LayerUtility: JoyCaptionBeta1`
- `easy cleanGpuUsed`
- `Note`
- `CR Text Concatenate`
- `CR Text`
- `LayerUtility: ImageReel`
- `SaveImage`
- `Reroute`
- `LoadImage`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `Reroute`
- `LoraLoader` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ShowText|pysssss`
- `DeepTranslatorTextNode`
- `TextInputBasic`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `ShowText|pysssss`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `919052511453328`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`UNETLoader`、`LoraLoader`、`CLIPTextEncode`、`VAELoader`、`VAEEncode`、`PathchSageAttentionKJ`、`CFGZeroStarAndInit`、`DeepTranslatorTextNode`、`LayerUtility: JoyCaptionBeta1`、`easy cleanGpuUsed`、`CR Text Concatenate`、`CR Text`、`LayerUtility: ImageReel`、`SaveImage`、`LoadImage`、`ModelSamplingSD3`、`VAEDecode`、`LayerUtility: ImageReelComposit`、`KSampler`、`TextInputBasic`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit
