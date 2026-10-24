---
key: 图片生成/图生图/WAN2.2图像洗图放大（纯种WAN2.2）_1952371299358322690.json
name: WAN2.2图像洗图放大（纯种WAN2.2）_1952371299358322690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2图像洗图放大（纯种WAN2.2）_1952371299358322690.json
hash: 9c152d18aba25fdd
coverage: 0.903226
learned_at: 2026-10-23 11:27:31
nodes: [UNETLoader, CLIPTextEncode, VAEEncode, SaveImage, easy cleanGpuUsed, LoraLoaderModelOnly, VAELoader, ImageConcatMulti, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, BasicScheduler, ModelSamplingSD3, KSamplerSelect, CLIPTextEncode, Image Comparer (rgthree), RH_Captioner, WanVideoNAG, CFGGuider, VAEDecode, PreviewImage, CLIPLoader, CLIPTextEncode, CLIPTextEncode, LoadImage, PreviewImage, UpscaleModelLoader, SDXLPromptStyler, UltimateSDUpscale]
patterns: []
missing: []
---

# 图片生成/图生图/WAN2.2图像洗图放大（纯种WAN2.2）_1952371299358322690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2图像洗图放大（纯种WAN2.2）_1952371299358322690.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ImageConcatMulti`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `RH_Captioner`
- `WanVideoNAG`
- `CFGGuider`
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewImage`
- `UpscaleModelLoader`
- `SDXLPromptStyler`
- `UltimateSDUpscale`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`VAEEncode`、`SaveImage`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`VAELoader`、`ImageConcatMulti`、`RandomNoise`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`BasicScheduler`、`ModelSamplingSD3`、`KSamplerSelect`、`RH_Captioner`、`WanVideoNAG`、`CFGGuider`、`VAEDecode`、`CLIPLoader`、`LoadImage`、`UpscaleModelLoader`、`SDXLPromptStyler`、`UltimateSDUpscale`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider
