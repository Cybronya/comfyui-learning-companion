---
key: 图片生成/文生图/超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529.json
name: 超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/超细节 Flux Sigma Vision Alpha1 - T2I - v1 (slow)_1887868607894806529.json
hash: 74f5fdcef348ca23
coverage: 0.788462
learned_at: 2026-10-07 03:05:45
nodes: [KSamplerSelect, Anything Everywhere, VAEDecodeTiled, UpscaleModelLoader, ModelSamplingFlux, BasicScheduler, mxSlider, mxSlider, mxSlider, Bookmark (rgthree), MultiplySigmas, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, Bookmark (rgthree), UpscaleModelLoader, ModelSamplingFlux, MultiplySigmas, mxSlider, DetailDaemonGraphSigmasNode, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, mxSlider, Seed (rgthree), Bookmark (rgthree), Reroute, mxSlider, mxSlider, mxSlider, mxSlider, KSamplerSelect, BasicScheduler, mxSlider, MultiplySigmas, DetailDaemonSamplerNode, mxSlider, DetailDaemonGraphSigmasNode, DetailDaemonSamplerNode, DetailDaemonGraphSigmasNode, DetailDaemonSamplerNode, CLIPTextEncode, BasicScheduler, KSamplerSelect, ModelSamplingFlux, UltimateSDUpscaleCustomSample, easy imageColorMatch, CLIPTextEncode, CLIPTextEncode, RandomNoise, easy imageColorMatch, SaveImage, VAEDecode, SaveImage, Note, Note, mxSlider, mxSlider, SamplerCustomAdvanced, CFGGuider, SaveImage, CR Aspect Ratio, ETN_CropImage, mxSlider, CLIPTextEncode, mxSlider, mxSlider, mxSlider, Fast Groups Bypasser (rgthree), UltimateSDUpscaleCustomSample, ETN_CropImage, mxSlider, mxSlider, Fast Bypasser (rgthree), mxSlider, Image Comparer (rgthree), mxSlider, mxSlider, Fast Bypasser (rgthree), Seed (rgthree), Image Comparer (rgthree), mxSlider, Seed (rgthree), mxSlider, mxSlider, mxSlider, mxSlider, Text _O, UNETLoader, VAELoader, TripleCLIPLoader, Power Lora Loader (rgthree), DualCLIPLoader, TripleCLIPLoader, PreviewImage, Power Lora Loader (rgthree)]
patterns: []
missing: [Bookmark (rgthree), Bookmark (rgthree), Bookmark (rgthree), CR Aspect Ratio, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Text _O, easy imageColorMatch, easy imageColorMatch, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Seed (rgthree), Seed (rgthree), Seed (rgthree)]
discoveries: [次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Aspect Ratio` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text _O` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **79%**（82/104）

**有卡**：`KSamplerSelect`、`VAEDecodeTiled`、`UpscaleModelLoader`、`ModelSamplingFlux`、`BasicScheduler`、`mxSlider`、`MultiplySigmas`、`DetailDaemonGraphSigmasNode`、`DetailDaemonSamplerNode`、`CLIPTextEncode`、`UltimateSDUpscaleCustomSample`、`RandomNoise`、`SaveImage`、`VAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`ETN_CropImage`、`UNETLoader`、`VAELoader`、`TripleCLIPLoader`、`DualCLIPLoader`

**缺卡**（14）：`Bookmark (rgthree)`、`Bookmark (rgthree)`、`Bookmark (rgthree)`、`CR Aspect Ratio`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Text _O`、`easy imageColorMatch`、`easy imageColorMatch`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`、`Seed (rgthree)`、`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CFGGuider、DetailDaemonSamplerNode、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Bookmark (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Aspect Ratio` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text _O` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
