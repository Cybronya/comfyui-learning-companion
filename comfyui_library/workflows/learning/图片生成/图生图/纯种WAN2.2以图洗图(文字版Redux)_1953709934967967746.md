---
key: 图片生成/图生图/纯种WAN2.2以图洗图(文字版Redux)_1953709934967967746.json
name: 纯种WAN2.2以图洗图(文字版Redux)_1953709934967967746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/纯种WAN2.2以图洗图(文字版Redux)_1953709934967967746.json
hash: 4c645b37283b9992
coverage: 0.896552
learned_at: 2026-10-23 13:21:11
nodes: [VAELoader, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, CLIPLoader, SamplerCustomAdvanced, WanVideoNAG, KSamplerSelect, BasicScheduler, CFGGuider, ModelSamplingSD3, Image Comparer (rgthree), VAEDecode, SaveImage, ImageConcatMulti, PreviewImage, UNETLoader, LoraLoaderModelOnly, RH_Captioner, LoraLoaderModelOnly, CLIPTextEncode, VAEEncode, CLIPTextEncode, LoadImage, ImageResize, LoadImage, PrimitiveFloat, ImageMirror]
patterns: []
missing: []
---

# 图片生成/图生图/纯种WAN2.2以图洗图(文字版Redux)_1953709934967967746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/纯种WAN2.2以图洗图(文字版Redux)_1953709934967967746.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAELoader`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `WanVideoNAG`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `ModelSamplingSD3`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RH_Captioner`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResize`
- `LoadImage`
- `PrimitiveFloat`
- `ImageMirror`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`VAELoader`、`RandomNoise`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`CLIPLoader`、`WanVideoNAG`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`ModelSamplingSD3`、`VAEDecode`、`SaveImage`、`ImageConcatMulti`、`UNETLoader`、`LoraLoaderModelOnly`、`RH_Captioner`、`CLIPTextEncode`、`VAEEncode`、`LoadImage`、`ImageResize`、`ImageMirror`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider
