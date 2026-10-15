---
key: 图片生成/文生图/超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529.json
name: 超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529.json
hash: 74f5fdcef348ca23
coverage: 0.923077
learned_at: 2026-10-15 22:29:06
nodes: [KSamplerSelect, Anything Everywhere, VAEDecodeTiled, UpscaleModelLoader, ModelSamplingFlux, BasicScheduler, mxSlider, mxSlider, mxSlider, Bookmark (rgthree), MultiplySigmas, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, Bookmark (rgthree), UpscaleModelLoader, ModelSamplingFlux, MultiplySigmas, mxSlider, DetailDaemonGraphSigmasNode, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, Seed (rgthree), Bookmark (rgthree), Reroute, mxSlider, mxSlider, mxSlider, mxSlider, KSamplerSelect, BasicScheduler, mxSlider, MultiplySigmas, DetailDaemonSamplerNode, mxSlider, DetailDaemonGraphSigmasNode, DetailDaemonSamplerNode, DetailDaemonGraphSigmasNode, DetailDaemonSamplerNode, CLIPTextEncode, BasicScheduler, KSamplerSelect, ModelSamplingFlux, UltimateSDUpscaleCustomSample, easy imageColorMatch, CLIPTextEncode, CLIPTextEncode, RandomNoise, easy imageColorMatch, SaveImage, VAEDecode, SaveImage, Note, Note, mxSlider, mxSlider, SamplerCustomAdvanced, CFGGuider, SaveImage, CR Aspect Ratio, ETN_CropImage, mxSlider, CLIPTextEncode, mxSlider, mxSlider, mxSlider, Fast Groups Bypasser (rgthree), UltimateSDUpscaleCustomSample, ETN_CropImage, mxSlider, mxSlider, Fast Bypasser (rgthree), mxSlider, Image Comparer (rgthree), mxSlider, mxSlider, Fast Bypasser (rgthree), Seed (rgthree), Image Comparer (rgthree), mxSlider, Seed (rgthree), mxSlider, mxSlider, mxSlider, mxSlider, Text _O, UNETLoader, VAELoader, TripleCLIPLoader, Power Lora Loader (rgthree), DualCLIPLoader, TripleCLIPLoader, PreviewImage, Power Lora Loader (rgthree)]
patterns: []
missing: []
---

# 图片生成/文生图/超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `KSamplerSelect` ★核心
- `Anything Everywhere`
- `VAEDecodeTiled` ★核心
- `UpscaleModelLoader`
- `ModelSamplingFlux`
- `BasicScheduler`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `Bookmark (rgthree)`
- `MultiplySigmas`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `Bookmark (rgthree)`
- `UpscaleModelLoader`
- `ModelSamplingFlux`
- `MultiplySigmas`
- `mxSlider`
- `DetailDaemonGraphSigmasNode`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `Seed (rgthree)`
- `Bookmark (rgthree)`
- `Reroute`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `mxSlider`
- `MultiplySigmas`
- `DetailDaemonSamplerNode` ★核心
- `mxSlider`
- `DetailDaemonGraphSigmasNode`
- `DetailDaemonSamplerNode` ★核心
- `DetailDaemonGraphSigmasNode`
- `DetailDaemonSamplerNode` ★核心
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `UltimateSDUpscaleCustomSample`
- `easy imageColorMatch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `easy imageColorMatch`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `Note`
- `mxSlider`
- `mxSlider`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `SaveImage`
- `CR Aspect Ratio`
- `ETN_CropImage`
- `mxSlider`
- `CLIPTextEncode` ★核心
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `Fast Groups Bypasser (rgthree)`
- `UltimateSDUpscaleCustomSample`
- `ETN_CropImage`
- `mxSlider`
- `mxSlider`
- `Fast Bypasser (rgthree)`
- `mxSlider`
- `Image Comparer (rgthree)`
- `mxSlider`
- `mxSlider`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `Image Comparer (rgthree)`
- `mxSlider`
- `Seed (rgthree)`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `mxSlider`
- `Text _O`
- `UNETLoader` ★核心
- `VAELoader`
- `TripleCLIPLoader`
- `Power Lora Loader (rgthree)`
- `DualCLIPLoader`
- `TripleCLIPLoader`
- `PreviewImage`
- `Power Lora Loader (rgthree)`

## 知识

覆盖率 **92%**（96/104）

**有卡**：`KSamplerSelect`、`VAEDecodeTiled`、`UpscaleModelLoader`、`ModelSamplingFlux`、`BasicScheduler`、`mxSlider`、`Bookmark (rgthree)`、`MultiplySigmas`、`DetailDaemonGraphSigmasNode`、`Seed (rgthree)`、`DetailDaemonSamplerNode`、`CLIPTextEncode`、`UltimateSDUpscaleCustomSample`、`easy imageColorMatch`、`RandomNoise`、`SaveImage`、`VAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`CR Aspect Ratio`、`ETN_CropImage`、`Fast Bypasser (rgthree)`、`Text _O`、`UNETLoader`、`VAELoader`、`TripleCLIPLoader`、`Power Lora Loader (rgthree)`、`DualCLIPLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CFGGuider、DetailDaemonSamplerNode、KSamplerSelect、SamplerCustomAdvanced
