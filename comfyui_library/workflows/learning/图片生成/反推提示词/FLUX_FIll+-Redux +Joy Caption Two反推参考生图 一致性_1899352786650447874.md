---
key: 图片生成/反推提示词/FLUX_FIll+-Redux +Joy Caption Two反推参考生图 一致性_1899352786650447874.json
name: FLUX_FIll+-Redux +Joy Caption Two反推参考生图 一致性_1899352786650447874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/FLUX_FIll+-Redux +Joy Caption Two反推参考生图 一致性_1899352786650447874.json
hash: f494e0a1970359e9
coverage: 0.925926
learned_at: 2026-10-26 01:45:03
nodes: [SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, FluxGuidance, ModelSamplingFlux, CLIPVisionLoader, CLIPVisionEncode, StyleModelLoader, StyleModelApplySimple, SaveImage, VAEDecode, CLIPTextEncode, UNETLoader, DualCLIPLoader, VAELoader, CR Text, CR Text Concatenate, Joy_caption_two_load, DeepTranslatorTextNode, EmptySD3LatentImage, Image Comparer (rgthree), Joy_caption_two, ShowText|pysssss, LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 图片生成/反推提示词/FLUX_FIll+-Redux +Joy Caption Two反推参考生图 一致性_1899352786650447874.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/FLUX_FIll+-Redux +Joy Caption Two反推参考生图 一致性_1899352786650447874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `FluxGuidance`
- `ModelSamplingFlux`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `StyleModelApplySimple`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CR Text`
- `CR Text Concatenate`
- `Joy_caption_two_load`
- `DeepTranslatorTextNode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `Joy_caption_two`
- `ShowText|pysssss`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`FluxGuidance`、`ModelSamplingFlux`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelLoader`、`StyleModelApplySimple`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CR Text`、`CR Text Concatenate`、`Joy_caption_two_load`、`DeepTranslatorTextNode`、`EmptySD3LatentImage`、`Joy_caption_two`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
