---
key: 平台全量/【FLUX In-Context-LoRA】人物一致性换装v1.2_1902179598119886849.json
name: 【FLUX In-Context-LoRA】人物一致性换装v1.2_1902179598119886849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【FLUX In-Context-LoRA】人物一致性换装v1.2_1902179598119886849.json
hash: 458d35432a37fa9b
coverage: 0.871795
learned_at: 2026-11-14 01:21:45
nodes: [CR Text Concatenate, LayerMask: MaskInvert, LayerUtility: ExtendCanvas, CLIPTextEncode, RandomNoise, BasicGuider, VAEDecode, VAEEncode, RepeatLatentBatch, FluxGuidance, TextInput_, easy imageSize, ImageCrop+, KSamplerSelect, SetLatentNoiseMask, SamplerCustomAdvanced, PreviewImage, PreviewImage, CR Text Concatenate, Text Concatenate (JPS), ShowText|pysssss, ImageResize+, ImpactInt, TextInput_, TextInput_, TextInput_, SaveImage, ETN_Translate, Note, Note, BasicScheduler, ETN_Translate, ModelSamplingFlux, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoader]
patterns: []
missing: []
---

# 平台全量/【FLUX In-Context-LoRA】人物一致性换装v1.2_1902179598119886849.json

> 来源文件 `comfyui_library/workflows/平台全量/【FLUX In-Context-LoRA】人物一致性换装v1.2_1902179598119886849.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CR Text Concatenate`
- `LayerMask: MaskInvert`
- `LayerUtility: ExtendCanvas`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `FluxGuidance`
- `TextInput_`
- `easy imageSize`
- `ImageCrop+`
- `KSamplerSelect` ★核心
- `SetLatentNoiseMask`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `PreviewImage`
- `CR Text Concatenate`
- `Text Concatenate (JPS)`
- `ShowText|pysssss`
- `ImageResize+`
- `ImpactInt`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `SaveImage`
- `ETN_Translate`
- `Note`
- `Note`
- `BasicScheduler`
- `ETN_Translate`
- `ModelSamplingFlux`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`CR Text Concatenate`、`LayerMask: MaskInvert`、`LayerUtility: ExtendCanvas`、`CLIPTextEncode`、`RandomNoise`、`BasicGuider`、`VAEDecode`、`VAEEncode`、`RepeatLatentBatch`、`FluxGuidance`、`TextInput_`、`easy imageSize`、`ImageCrop+`、`KSamplerSelect`、`SetLatentNoiseMask`、`SamplerCustomAdvanced`、`Text Concatenate (JPS)`、`ImageResize+`、`ImpactInt`、`SaveImage`、`ETN_Translate`、`BasicScheduler`、`ModelSamplingFlux`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
