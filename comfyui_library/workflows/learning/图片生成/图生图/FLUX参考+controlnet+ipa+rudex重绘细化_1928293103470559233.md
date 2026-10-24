---
key: 图片生成/图生图/FLUX参考+controlnet+ipa+rudex重绘细化_1928293103470559233.json
name: FLUX参考+controlnet+ipa+rudex重绘细化_1928293103470559233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX参考+controlnet+ipa+rudex重绘细化_1928293103470559233.json
hash: 5d0fb13828564722
coverage: 0.921053
learned_at: 2026-10-23 10:54:50
nodes: [UNETLoader, EmptyLatentImage, PreviewImage, KSamplerSelect, DualCLIPLoader, AIO_Preprocessor, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, GetImageSize, VAELoader, VAEEncode, ConditioningZeroOut, CLIPTextEncode, CLIPTextEncode, SamplerCustom, LoraLoaderModelOnly, AIO_Preprocessor, ControlNetLoader, VAEDecode, SaveImage, LoraLoaderModelOnly, ACN_AdvancedControlNetApply_v2, ACN_AdvancedControlNetApply_v2, BasicScheduler, ChinesePrompt_Mix, ImageScale, LoraLoaderModelOnly, LoadImage, LoadImage, MiniCPM_VQA, ShowText|pysssss, ImageScale, CLIPVisionLoader, StyleModelLoader, ReduxAdvanced, IPAdapterFluxLoader, ApplyIPAdapterFlux]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.6000000000000001, "height": 768, "width": 1560}
---

# 图片生成/图生图/FLUX参考+controlnet+ipa+rudex重绘细化_1928293103470559233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX参考+controlnet+ipa+rudex重绘细化_1928293103470559233.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `KSamplerSelect` ★核心
- `DualCLIPLoader`
- `AIO_Preprocessor`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `VAELoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `ACN_AdvancedControlNetApply_v2` ★核心
- `ACN_AdvancedControlNetApply_v2` ★核心
- `BasicScheduler`
- `ChinesePrompt_Mix`
- `ImageScale`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `MiniCPM_VQA`
- `ShowText|pysssss`
- `ImageScale`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `ReduxAdvanced`
- `IPAdapterFluxLoader`
- `ApplyIPAdapterFlux`

## 关键参数

- `width` = `1560`
- `height` = `768`
- `batch_size` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`UNETLoader`、`EmptyLatentImage`、`KSamplerSelect`、`DualCLIPLoader`、`AIO_Preprocessor`、`LoraLoaderModelOnly`、`GetImageSize`、`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`CLIPTextEncode`、`SamplerCustom`、`ControlNetLoader`、`VAEDecode`、`SaveImage`、`ACN_AdvancedControlNetApply_v2`、`BasicScheduler`、`ChinesePrompt_Mix`、`ImageScale`、`LoadImage`、`MiniCPM_VQA`、`CLIPVisionLoader`、`StyleModelLoader`、`ReduxAdvanced`、`IPAdapterFluxLoader`、`ApplyIPAdapterFlux`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
