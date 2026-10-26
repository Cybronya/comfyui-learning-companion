---
key: 图片生成/反推提示词/joy caption two+deepseek反推风格图像_1949006978589831170.json
name: joy caption two+deepseek反推风格图像_1949006978589831170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/joy caption two+deepseek反推风格图像_1949006978589831170.json
hash: 78d1957a4ea180f9
coverage: 0.72973
learned_at: 2026-10-26 01:46:49
nodes: [PreviewImage, KSamplerSelect, CFGGuider, ShowText|pysssss, CLIPTextEncodeFlux, Reroute, ControlNetLoader, SetUnionControlNetType, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, Joy_extra_options, BasicScheduler, DeepTranslatorTextNode, DeepTranslatorTextNode, JanusImageUnderstanding, AIO_Preprocessor, JanusModelLoader, CLIPTextEncode, EmptyLatentImage, UNETLoader, VAELoader, DualCLIPLoader, ShowText|pysssss, Anything Everywhere3, ControlNetApplyAdvanced, LoadImage, Fast Groups Muter (rgthree), Joy_caption_two_advanced, ShowText|pysssss, Joy_caption_two_load, LoraLoader, easy stylesSelector, SaveImage, PreviewImage, VAEDecode, Note]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.6000000000000001, "height": 1536, "lora_name": "超真实日常生活照.safetensors", "strength_clip": 0.6000000000000001, "strength_model": 0.6000000000000001, "width": 1024}
---

# 图片生成/反推提示词/joy caption two+deepseek反推风格图像_1949006978589831170.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/joy caption two+deepseek反推风格图像_1949006978589831170.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `PreviewImage`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ShowText|pysssss`
- `CLIPTextEncodeFlux` ★核心
- `Reroute`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ShowText|pysssss`
- `Joy_extra_options`
- `BasicScheduler`
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `JanusImageUnderstanding`
- `AIO_Preprocessor`
- `JanusModelLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `ShowText|pysssss`
- `Anything Everywhere3`
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `Joy_caption_two_advanced`
- `ShowText|pysssss`
- `Joy_caption_two_load`
- `LoraLoader` ★核心
- `easy stylesSelector`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `Note`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `controlnet_strength` = `0.6000000000000001`
- `lora_name` = `超真实日常生活照.safetensors`
- `strength_model` = `0.6000000000000001`
- `strength_clip` = `0.6000000000000001`

## 知识

覆盖率 **73%**（27/37）

**有卡**：`KSamplerSelect`、`CFGGuider`、`CLIPTextEncodeFlux`、`ControlNetLoader`、`SetUnionControlNetType`、`RandomNoise`、`SamplerCustomAdvanced`、`Joy_extra_options`、`BasicScheduler`、`DeepTranslatorTextNode`、`JanusImageUnderstanding`、`AIO_Preprocessor`、`JanusModelLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`ControlNetApplyAdvanced`、`LoadImage`、`Joy_caption_two_advanced`、`Joy_caption_two_load`、`LoraLoader`、`easy stylesSelector`、`SaveImage`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
