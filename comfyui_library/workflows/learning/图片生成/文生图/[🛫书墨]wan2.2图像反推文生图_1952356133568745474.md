---
key: 图片生成/文生图/[🛫书墨]wan2.2图像反推文生图_1952356133568745474.json
name: [🛫书墨]wan2.2图像反推文生图_1952356133568745474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/[🛫书墨]wan2.2图像反推文生图_1952356133568745474.json
hash: dfcf322c7843861e
coverage: 0.923077
learned_at: 2026-10-15 22:27:42
nodes: [MarkdownNote, EmptyHunyuanLatentVideo, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, WanVideoNAG, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1ExtraOptions, VAEDecode, SaveImage, LayerUtility: JoyCaptionBeta1, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, ShowText|pysssss]
patterns: []
missing: []
---

# 图片生成/文生图/[🛫书墨]wan2.2图像反推文生图_1952356133568745474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/[🛫书墨]wan2.2图像反推文生图_1952356133568745474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `MarkdownNote`
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
- `LoadImage`
- `ShowText|pysssss`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`EmptyHunyuanLatentVideo`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`VAEDecode`、`SaveImage`、`LayerUtility: JoyCaptionBeta1`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider
