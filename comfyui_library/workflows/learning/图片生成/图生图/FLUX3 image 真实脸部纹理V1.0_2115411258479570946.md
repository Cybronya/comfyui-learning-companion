---
key: 图片生成/图生图/FLUX3 image 真实脸部纹理V1.0_2115411258479570946.json
name: FLUX3 image 真实脸部纹理V1.0_2115411258479570946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX3 image 真实脸部纹理V1.0_2115411258479570946.json
hash: 0338f80938c8dc92
coverage: 0.904762
learned_at: 2026-10-30 17:49:36
nodes: [ReferenceLatent, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, SaveImage, UNETLoader, CLIPLoader, VAELoader, LoadImage, Flux3PELoader, CLIPTextEncode, Flux3PromptEnhance, CR Prompt Text, VAEEncode, kkGetImage, Image Comparer (rgthree), PreviewImage, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX3 image 真实脸部纹理V1.0_2115411258479570946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX3 image 真实脸部纹理V1.0_2115411258479570946.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ReferenceLatent`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `Flux3PELoader`
- `CLIPTextEncode` ★核心
- `Flux3PromptEnhance`
- `CR Prompt Text`
- `VAEEncode` ★核心
- `kkGetImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **90%**（19/21）

**有卡**：`ReferenceLatent`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`Flux3PELoader`、`CLIPTextEncode`、`Flux3PromptEnhance`、`CR Prompt Text`、`VAEEncode`、`kkGetImage`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
