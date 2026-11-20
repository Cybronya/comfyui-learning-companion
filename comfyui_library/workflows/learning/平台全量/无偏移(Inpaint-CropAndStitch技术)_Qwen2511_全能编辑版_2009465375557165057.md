---
key: 平台全量/无偏移(Inpaint-CropAndStitch技术)_Qwen2511_全能编辑版_2009465375557165057.json
name: 无偏移(Inpaint-CropAndStitch技术)_Qwen2511_全能编辑版_2009465375557165057
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/无偏移(Inpaint-CropAndStitch技术)_Qwen2511_全能编辑版_2009465375557165057.json
hash: bfd39e095120b188
coverage: 0.882353
learned_at: 2026-11-14 02:12:45
nodes: [easy getNode, KSampler, CFGNorm, Image Comparer (rgthree), easy getNode, easy promptConcat, easy setNode, SaveImage, InpaintStitchImproved, easy getNode, easy setNode, VAEDecode, easy setNode, easy getNode, easy setNode, InpaintCropImproved, LoadImage, ModelSamplingAuraFlow, CR SDXL Aspect Ratio, easy getNode, ConditioningZeroOut, VAEEncode, PreviewImage, LoadImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, LoadImage, LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, easy positive, easy stylesSelector]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 848667694296525, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/无偏移(Inpaint-CropAndStitch技术)_Qwen2511_全能编辑版_2009465375557165057.json

> 来源文件 `comfyui_library/workflows/平台全量/无偏移(Inpaint-CropAndStitch技术)_Qwen2511_全能编辑版_2009465375557165057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（34 个）：
- `easy getNode`
- `KSampler` ★核心
- `CFGNorm`
- `Image Comparer (rgthree)`
- `easy getNode`
- `easy promptConcat`
- `easy setNode`
- `SaveImage`
- `InpaintStitchImproved`
- `easy getNode`
- `easy setNode`
- `VAEDecode` ★核心
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `InpaintCropImproved`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CR SDXL Aspect Ratio`
- `easy getNode`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `PreviewImage`
- `LoadImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `easy positive`
- `easy stylesSelector`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `848667694296525`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`easy getNode`、`KSampler`、`CFGNorm`、`easy promptConcat`、`easy setNode`、`SaveImage`、`InpaintStitchImproved`、`VAEDecode`、`InpaintCropImproved`、`LoadImage`、`ModelSamplingAuraFlow`、`CR SDXL Aspect Ratio`、`ConditioningZeroOut`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`easy positive`、`easy stylesSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
