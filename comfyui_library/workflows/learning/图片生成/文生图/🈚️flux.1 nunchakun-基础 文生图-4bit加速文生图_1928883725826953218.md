---
key: 图片生成/文生图/🈚️flux.1 nunchakun-基础 文生图-4bit加速文生图_1928883725826953218.json
name: 🈚️flux.1 nunchakun-基础 文生图-4bit加速文生图_1928883725826953218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🈚️flux.1 nunchakun-基础 文生图-4bit加速文生图_1928883725826953218.json
hash: 632075570a49dc82
coverage: 0.610169
learned_at: 2026-10-10 21:00:01
nodes: [BasicGuider, FluxGuidance, ConditioningZeroOut, CLIPTextEncode, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, BasicGuider, RandomNoise, BasicScheduler, SamplerCustomAdvanced, GetNode, GetNode, InjectLatentNoise+, RandomNoise, RebatchLatents, CR Aspect Ratio, SamplerCustomAdvanced, GetNode, VAEDecode, ImageSmartSharpen+, GetNode, KSamplerSelect, DetailDaemonSamplerNode, BasicScheduler, GetNode, KSamplerSelect, VAEDecode, DetailDaemonSamplerNode, EnhanceDetail, GetNode, LatentPixelScale, UpscaleModelLoader, ImageSmartSharpen+, ShowText|pysssss, LayerUtility: TextJoin, SetNode, ShowText|pysssss, Text, LoadImage, SaveImage, SaveImage, Text, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, SetNode, ImpactSwitch, AILab_QwenVL, NunchakuFluxDiTLoader, DualCLIPLoader, NunchakuTextEncoderLoaderV2, RH_Translator]
patterns: []
missing: [CR Aspect Ratio, ImageSmartSharpen+, ImageSmartSharpen+, LayerUtility: TextJoin, InjectLatentNoise+]
discoveries: [次要节点 `CR Aspect Ratio` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `InjectLatentNoise+` 仅有 VAE 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/🈚️flux.1 nunchakun-基础 文生图-4bit加速文生图_1928883725826953218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/🈚️flux.1 nunchakun-基础 文生图-4bit加速文生图_1928883725826953218.json`

## 结构

**节点**（59 个）：
- `BasicGuider`
- `FluxGuidance`
- `ConditioningZeroOut`
- `CLIPTextEncode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `RandomNoise`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `GetNode`
- `GetNode`
- `InjectLatentNoise+`
- `RandomNoise`
- `RebatchLatents`
- `CR Aspect Ratio`
- `SamplerCustomAdvanced`
- `GetNode`
- `VAEDecode`
- `ImageSmartSharpen+`
- `GetNode`
- `KSamplerSelect`
- `DetailDaemonSamplerNode`
- `BasicScheduler`
- `GetNode`
- `KSamplerSelect`
- `VAEDecode`
- `DetailDaemonSamplerNode`
- `EnhanceDetail`
- `GetNode`
- `LatentPixelScale`
- `UpscaleModelLoader`
- `ImageSmartSharpen+`
- `ShowText|pysssss`
- `LayerUtility: TextJoin`
- `SetNode`
- `ShowText|pysssss`
- `Text`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `Text`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `SetNode`
- `ImpactSwitch`
- `AILab_QwenVL`
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `NunchakuTextEncoderLoaderV2`
- `RH_Translator`

## 知识

覆盖率 **61%**（36/59）

**有卡**：`BasicGuider`、`FluxGuidance`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`SetNode`、`GetNode`、`RandomNoise`、`BasicScheduler`、`SamplerCustomAdvanced`、`InjectLatentNoise+`、`RebatchLatents`、`CR Aspect Ratio`、`VAEDecode`、`ImageSmartSharpen+`、`KSamplerSelect`、`DetailDaemonSamplerNode`、`EnhanceDetail`

**缺卡**（5）：`CR Aspect Ratio`、`ImageSmartSharpen+`、`ImageSmartSharpen+`、`LayerUtility: TextJoin`、`InjectLatentNoise+`

## 学习发现

- 次要节点 `CR Aspect Ratio` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `InjectLatentNoise+` 仅有 VAE 的通用知识，没有该节点自己的说明
