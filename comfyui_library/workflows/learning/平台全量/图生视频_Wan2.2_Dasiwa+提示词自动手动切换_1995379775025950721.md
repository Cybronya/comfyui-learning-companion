---
key: 平台全量/图生视频_Wan2.2_Dasiwa+提示词自动手动切换_1995379775025950721.json
name: 图生视频_Wan2.2_Dasiwa+提示词自动手动切换_1995379775025950721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图生视频_Wan2.2_Dasiwa+提示词自动手动切换_1995379775025950721.json
hash: d564e444c282cdde
coverage: 0.875
learned_at: 2026-11-14 01:56:29
nodes: [UNETLoader, CLIPLoader, VAELoader, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPVisionLoader, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, CLIPVisionEncode, CR Prompt Text, LayerUtility: PurgeVRAM, LoadImage, CLIPTextEncode, ModelSamplingSD3, PrimitiveInt, ModelSamplingSD3, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, CR Prompt Text, easy anythingIndexSwitch, ImageResizeKJv2, WanImageToVideo, AILab_QwenVL, CR Prompt Text, CLIPTextEncode, ConcatTextOfUtils, easy showAnything, Int, VAEDecode, VAEDecode, SaveImage, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SaveLatent, TT_img_enc_v2]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/图生视频_Wan2.2_Dasiwa+提示词自动手动切换_1995379775025950721.json

> 来源文件 `comfyui_library/workflows/平台全量/图生视频_Wan2.2_Dasiwa+提示词自动手动切换_1995379775025950721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PrimitiveInt`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `easy anythingIndexSwitch`
- `ImageResizeKJv2`
- `WanImageToVideo`
- `AILab_QwenVL`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `ConcatTextOfUtils`
- `easy showAnything`
- `Int`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveLatent`
- `TT_img_enc_v2`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`CLIPVisionLoader`、`KSamplerAdvanced`、`CLIPVisionEncode`、`CR Prompt Text`、`LayerUtility: PurgeVRAM`、`LoadImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`easy anythingIndexSwitch`、`ImageResizeKJv2`、`WanImageToVideo`、`AILab_QwenVL`、`ConcatTextOfUtils`、`Int`、`VAEDecode`、`SaveImage`、`VHS_VideoCombine`、`SaveLatent`、`TT_img_enc_v2`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader、KSamplerAdvanced
