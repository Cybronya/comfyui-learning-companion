---
key: 图片生成/图生图/🈚️flux.1 nunchakun i2i-基础图生图_洗图-4bit加速_1929169338916356098.json
name: 🈚️flux.1 nunchakun i2i-基础图生图_洗图-4bit加速_1929169338916356098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🈚️flux.1 nunchakun i2i-基础图生图_洗图-4bit加速_1929169338916356098.json
hash: ec657bc6ae627bdb
coverage: 0.603448
learned_at: 2026-10-23 13:38:43
nodes: [LoadJanusModel, BasicGuider, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, VAELoader, SetNode, GetNode, SetNode, SetNode, SetNode, CR Text Concatenate, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, CR Text, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, SetNode, SetNode, RandomNoise, easy cleanGpuUsed, RebatchLatents, VAEEncode, GetNode, GetNode, RepeatLatentBatch, SamplerCustomAdvanced, GetNode, CLIPTextEncode, NunchakuFluxLoraLoader, JanusImage2Text, ShowText|pysssss, LoadImage, KSamplerSelect, DetailDaemonSamplerNode, UpscaleModelLoader, GetNode, InjectLatentNoise+, BasicScheduler, LatentPixelScale, VAEDecode, SetNode, GetNode, SetNode, GetNode, EnhanceDetail, ImageSmartSharpen+, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, SaveImage, DualCLIPLoader, NunchakuTextEncoderLoaderV2]
patterns: []
missing: []
---

# 图片生成/图生图/🈚️flux.1 nunchakun i2i-基础图生图_洗图-4bit加速_1929169338916356098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🈚️flux.1 nunchakun i2i-基础图生图_洗图-4bit加速_1929169338916356098.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `LoadJanusModel`
- `BasicGuider`
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text Concatenate`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CR Text`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `SetNode`
- `SetNode`
- `RandomNoise`
- `easy cleanGpuUsed`
- `RebatchLatents`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `JanusImage2Text`
- `ShowText|pysssss`
- `LoadImage`
- `KSamplerSelect` ★核心
- `DetailDaemonSamplerNode` ★核心
- `UpscaleModelLoader`
- `GetNode`
- `InjectLatentNoise+`
- `BasicScheduler`
- `LatentPixelScale`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `EnhanceDetail`
- `ImageSmartSharpen+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `SaveImage`
- `DualCLIPLoader`
- `NunchakuTextEncoderLoaderV2`

## 知识

覆盖率 **60%**（35/58）

**有卡**：`LoadJanusModel`、`BasicGuider`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`CR Text Concatenate`、`CR Text`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`RandomNoise`、`easy cleanGpuUsed`、`RebatchLatents`、`VAEEncode`、`RepeatLatentBatch`、`SamplerCustomAdvanced`、`JanusImage2Text`、`LoadImage`、`KSamplerSelect`、`DetailDaemonSamplerNode`、`UpscaleModelLoader`、`InjectLatentNoise+`、`BasicScheduler`、`LatentPixelScale`、`VAEDecode`、`EnhanceDetail`、`ImageSmartSharpen+`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`DualCLIPLoader`、`NunchakuTextEncoderLoaderV2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、DetailDaemonSamplerNode、FluxGuidance、KSamplerSelect
