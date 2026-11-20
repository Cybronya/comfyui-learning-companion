---
key: 平台全量/WAN2.2图像洗图放大_1955889468760838145.json
name: WAN2.2图像洗图放大_1955889468760838145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WAN2.2图像洗图放大_1955889468760838145.json
hash: 67cdd1319e6c233c
coverage: 0.909091
learned_at: 2026-11-14 01:03:44
nodes: [VAEEncode, easy cleanGpuUsed, SDXLPromptStyler, RandomNoise, SplitSigmas, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, RH_Captioner, CFGGuider, UpscaleModelLoader, CLIPTextEncode, SaveImage, ImageConcatMulti, PreviewImage, WanVideoNAG, VAEDecode, UNETLoader, SamplerCustomAdvanced, CLIPTextEncode, CLIPLoader, VAELoader, CLIPTextEncode, Image Comparer (rgthree), LoraLoaderModelOnly, LoadImage, PreviewImage, BasicScheduler, CLIPTextEncode, SaveImage, UltimateSDUpscale, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 平台全量/WAN2.2图像洗图放大_1955889468760838145.json

> 来源文件 `comfyui_library/workflows/平台全量/WAN2.2图像洗图放大_1955889468760838145.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `SDXLPromptStyler`
- `RandomNoise`
- `SplitSigmas`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `RH_Captioner`
- `CFGGuider`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `PreviewImage`
- `WanVideoNAG`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PreviewImage`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `UltimateSDUpscale`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`VAEEncode`、`easy cleanGpuUsed`、`SDXLPromptStyler`、`RandomNoise`、`SplitSigmas`、`DisableNoise`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`KSamplerSelect`、`RH_Captioner`、`CFGGuider`、`UpscaleModelLoader`、`CLIPTextEncode`、`SaveImage`、`ImageConcatMulti`、`WanVideoNAG`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`BasicScheduler`、`UltimateSDUpscale`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider
