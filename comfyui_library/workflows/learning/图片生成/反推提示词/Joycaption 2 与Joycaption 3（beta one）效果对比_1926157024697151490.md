---
key: 图片生成/反推提示词/Joycaption 2 与Joycaption 3（beta one）效果对比_1926157024697151490.json
name: Joycaption 2 与Joycaption 3（beta one）效果对比_1926157024697151490
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Joycaption 2 与Joycaption 3（beta one）效果对比_1926157024697151490.json
hash: c8d99bb61fbba55c
coverage: 0.888889
learned_at: 2026-10-26 01:45:23
nodes: [VAELoader, KSampler, CLIPTextEncode, VAEEncode, Joy_caption_two, Joy_caption_two_load, ShowText|pysssss, VAEDecode, ConditioningZeroOut, SaveImage, SaveImage, LoadImage, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, KSampler, UNETLoader, DualCLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, CLIPTextEncode, FluxGuidance, FluxGuidance, VAEDecode, LayerUtility: LoadJoyCaptionBeta1Model, ConstrainImage|pysssss, Note, LayerUtility: JoyCaptionBeta1ExtraOptions]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "FLUX1大模型-追求极致超逼真亚洲美女_FLUX亚洲超逼真美女V1.0.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 683116498958937, "steps": 20}
---

# 图片生成/反推提示词/Joycaption 2 与Joycaption 3（beta one）效果对比_1926157024697151490.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Joycaption 2 与Joycaption 3（beta one）效果对比_1926157024697151490.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Joy_caption_two`
- `Joy_caption_two_load`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `FluxGuidance`
- `VAEDecode` ★核心
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `ConstrainImage|pysssss`
- `Note`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `683116498958937`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `FLUX1大模型-追求极致超逼真亚洲美女_FLUX亚洲超逼真美女V1.0.safetensors`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`VAELoader`、`KSampler`、`CLIPTextEncode`、`VAEEncode`、`Joy_caption_two`、`Joy_caption_two_load`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`LoadImage`、`LayerUtility: JoyCaptionBeta1`、`UNETLoader`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`FluxGuidance`、`LayerUtility: LoadJoyCaptionBeta1Model`、`ConstrainImage|pysssss`、`LayerUtility: JoyCaptionBeta1ExtraOptions`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
