---
key: 图片生成/文生图/文生图-wan2.2图像反推文生图_1954793772753182722.json
name: 文生图-wan2.2图像反推文生图_1954793772753182722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-wan2.2图像反推文生图_1954793772753182722.json
hash: 0d65e1df04f800f9
coverage: 0.96
learned_at: 2026-10-15 22:28:48
nodes: [EmptyHunyuanLatentVideo, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, WanVideoNAG, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1ExtraOptions, VAEDecode, SaveImage, LayerUtility: JoyCaptionBeta1, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LayerUtility: LoadJoyCaptionBeta1Model, ShowText|pysssss, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/文生图-wan2.2图像反推文生图_1954793772753182722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-wan2.2图像反推文生图_1954793772753182722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `EmptyHunyuanLatentVideo`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: JoyCaptionBeta1`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `ShowText|pysssss`
- `LoadImage`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`EmptyHunyuanLatentVideo`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`VAEDecode`、`SaveImage`、`LayerUtility: JoyCaptionBeta1`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider
