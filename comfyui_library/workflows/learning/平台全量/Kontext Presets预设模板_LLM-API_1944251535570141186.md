---
key: 平台全量/Kontext Presets预设模板_LLM-API_1944251535570141186.json
name: Kontext Presets预设模板_LLM-API_1944251535570141186
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext Presets预设模板_LLM-API_1944251535570141186.json
hash: ecf601acd3778bc0
coverage: 0.724138
learned_at: 2026-11-14 00:34:19
nodes: [DeepTranslatorTextNode, VAEEncode, ShowText|pysssss, ShowText|pysssss, RepeatLatentBatch, ShowText|pysssss, VAEDecode, DualCLIPLoader, UNETLoader, KSampler, ConditioningZeroOut, ImageStitch, Reroute, FluxGuidance, ReferenceLatent, CLIPTextEncode, SaveImage, FluxKontextImageScale, Reroute, PreviewImage, VAELoader, CR String To Combo, SDXLAspectRatioSelector, RH_LLMAPI_NODE, PreviewImage, LoadImage, LoadKontextPresets, LayerUtility: ImageScaleByAspectRatio V2, JjkText]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 354441408311018, "steps": 20}
---

# 平台全量/Kontext Presets预设模板_LLM-API_1944251535570141186.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext Presets预设模板_LLM-API_1944251535570141186.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `DeepTranslatorTextNode`
- `VAEEncode` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RepeatLatentBatch`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ImageStitch`
- `Reroute`
- `FluxGuidance`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `FluxKontextImageScale`
- `Reroute`
- `PreviewImage`
- `VAELoader`
- `CR String To Combo`
- `SDXLAspectRatioSelector`
- `RH_LLMAPI_NODE`
- `PreviewImage`
- `LoadImage`
- `LoadKontextPresets`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `354441408311018`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（21/29）

**有卡**：`DeepTranslatorTextNode`、`VAEEncode`、`RepeatLatentBatch`、`VAEDecode`、`DualCLIPLoader`、`UNETLoader`、`KSampler`、`ConditioningZeroOut`、`ImageStitch`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`SaveImage`、`FluxKontextImageScale`、`VAELoader`、`CR String To Combo`、`SDXLAspectRatioSelector`、`RH_LLMAPI_NODE`、`LoadImage`、`LoadKontextPresets`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
