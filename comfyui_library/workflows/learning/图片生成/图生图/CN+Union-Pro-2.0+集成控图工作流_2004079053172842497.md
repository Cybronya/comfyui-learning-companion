---
key: 图片生成/图生图/CN+Union-Pro-2.0+集成控图工作流_2004079053172842497.json
name: CN+Union-Pro-2.0+集成控图工作流_2004079053172842497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CN+Union-Pro-2.0+集成控图工作流_2004079053172842497.json
hash: 5aa928f0bde4fb48
coverage: 0.871795
learned_at: 2026-10-23 10:51:51
nodes: [DualCLIPLoader, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, EmptySD3LatentImage, RandomNoise, Image Comparer (rgthree), UNETLoader, ModelSamplingFlux, FluxGuidance, LayerUtility: ImageScaleByAspectRatio V2, easy saveText, easy seed, CR Text, AILab_QwenVL, VAELoader, AIO_Preprocessor, PreviewImage, StyleModelLoader, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJ, LoraLoaderModelOnly, LoadImage, RH_Prompter, Text to Conditioning, ConditioningZeroOut, TextCombinerTwo, ShowText|pysssss, VAEDecode, SaveImage, BasicScheduler, LoadImage, ShowText|pysssss, StyleModelApply, Fast Groups Bypasser (rgthree), ControlNetLoader, Textbox, ControlNetApplySD3]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.8000000000000002}
---

# 图片生成/图生图/CN+Union-Pro-2.0+集成控图工作流_2004079053172842497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/CN+Union-Pro-2.0+集成控图工作流_2004079053172842497.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `EmptySD3LatentImage`
- `RandomNoise`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `ModelSamplingFlux`
- `FluxGuidance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy saveText`
- `easy seed`
- `CR Text`
- `AILab_QwenVL`
- `VAELoader`
- `AIO_Preprocessor`
- `PreviewImage`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJ`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `RH_Prompter`
- `Text to Conditioning`
- `ConditioningZeroOut`
- `TextCombinerTwo`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `SaveImage`
- `BasicScheduler`
- `LoadImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `Fast Groups Bypasser (rgthree)`
- `ControlNetLoader`
- `Textbox`
- `ControlNetApplySD3` ★核心

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`DualCLIPLoader`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`EmptySD3LatentImage`、`RandomNoise`、`UNETLoader`、`ModelSamplingFlux`、`FluxGuidance`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy saveText`、`easy seed`、`CR Text`、`AILab_QwenVL`、`VAELoader`、`AIO_Preprocessor`、`StyleModelLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJ`、`LoraLoaderModelOnly`、`LoadImage`、`RH_Prompter`、`Text to Conditioning`、`ConditioningZeroOut`、`TextCombinerTwo`、`VAEDecode`、`SaveImage`、`BasicScheduler`、`StyleModelApply`、`ControlNetLoader`、`Textbox`、`ControlNetApplySD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、ControlNetLoader
