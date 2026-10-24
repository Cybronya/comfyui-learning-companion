---
key: 图片生成/图生图/FLUX最强精修工作流，无需controlnet参与，更快更强.ai_1915020344825184258.json
name: FLUX最强精修工作流，无需controlnet参与，更快更强.ai_1915020344825184258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX最强精修工作流，无需controlnet参与，更快更强.ai_1915020344825184258.json
hash: ae38a5993174c002
coverage: 0.673077
learned_at: 2026-10-23 10:55:00
nodes: [Note, PreviewImage, IPAdapterUnifiedLoader, IPAdapterAdvanced, IPAdapterNoise, CannyEdgePreprocessor, Note, PreviewImage, ControlNetApplyAdvanced, Image Comparer (rgthree), Note, Note, CR Latent Batch Size, VAEEncode, LineArtPreprocessor, DepthAnythingPreprocessor, PreviewImage, ControlNetApplyAdvanced, ControlNetApplyAdvanced, Note, Note, PreviewImage, PreviewImage, PreviewImage, CLIPTextEncodeWithWeight //Inspire, Note, CheckpointLoaderSimple, CLIPTextEncodeWithWeight //Inspire, StringFunction|pysssss, KSampler, LayerMask: MaskGrow, LayerColor: Exposure, LayerUtility: ImageBlendAdvance V2, MaskToImage, InspyrenetRembgAdvanced, easy imageSize, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, TextInput_, ShowText|pysssss, CR Color Panel, LayerUtility: HLFrequencyDetailRestore, Text Concatenate, CLIPSetLastLayer, TextInput_, LoadImage, ControlNetLoader, ControlNetLoader, ControlNetLoader, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 112778158420944, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX最强精修工作流，无需controlnet参与，更快更强.ai_1915020344825184258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX最强精修工作流，无需controlnet参与，更快更强.ai_1915020344825184258.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Note`
- `PreviewImage`
- `IPAdapterUnifiedLoader`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `CannyEdgePreprocessor`
- `Note`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `CR Latent Batch Size`
- `VAEEncode` ★核心
- `LineArtPreprocessor`
- `DepthAnythingPreprocessor`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `Note`
- `Note`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncodeWithWeight //Inspire` ★核心
- `Note`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncodeWithWeight //Inspire` ★核心
- `StringFunction|pysssss`
- `KSampler` ★核心
- `LayerMask: MaskGrow`
- `LayerColor: Exposure`
- `LayerUtility: ImageBlendAdvance V2`
- `MaskToImage`
- `InspyrenetRembgAdvanced`
- `easy imageSize`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextInput_`
- `ShowText|pysssss`
- `CR Color Panel`
- `LayerUtility: HLFrequencyDetailRestore`
- `Text Concatenate`
- `CLIPSetLastLayer`
- `TextInput_`
- `LoadImage`
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`
- `seed` = `112778158420944`
- `steps` = `5`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **67%**（35/52）

**有卡**：`IPAdapterUnifiedLoader`、`IPAdapterAdvanced`、`IPAdapterNoise`、`CannyEdgePreprocessor`、`ControlNetApplyAdvanced`、`CR Latent Batch Size`、`VAEEncode`、`LineArtPreprocessor`、`DepthAnythingPreprocessor`、`CLIPTextEncodeWithWeight //Inspire`、`CheckpointLoaderSimple`、`StringFunction|pysssss`、`KSampler`、`LayerMask: MaskGrow`、`LayerColor: Exposure`、`LayerUtility: ImageBlendAdvance V2`、`MaskToImage`、`InspyrenetRembgAdvanced`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextInput_`、`CR Color Panel`、`LayerUtility: HLFrequencyDetailRestore`、`Text Concatenate`、`CLIPSetLastLayer`、`LoadImage`、`ControlNetLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、DepthAnythingPreprocessor、CannyEdgePreprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
