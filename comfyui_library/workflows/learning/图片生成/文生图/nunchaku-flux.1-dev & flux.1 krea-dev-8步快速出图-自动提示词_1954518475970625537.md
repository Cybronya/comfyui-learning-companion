---
key: 图片生成/文生图/nunchaku-flux.1-dev & flux.1 krea-dev-8步快速出图-自动提示词_1954518475970625537.json
name: nunchaku-flux.1-dev & flux.1 krea-dev-8步快速出图-自动提示词_1954518475970625537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev & flux.1 krea-dev-8步快速出图-自动提示词_1954518475970625537.json
hash: c31717e8ab2ee5a3
coverage: 0.702703
learned_at: 2026-10-10 20:59:23
nodes: [ShowText|pysssss, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, RH_LLMAPI_NODE, VAEDecode, FluxGuidance, CLIPTextEncode, NunchakuTextEncoderLoader, NunchakuFluxDiTLoader, RandomNoise, SamplerCustomAdvanced, VAELoader, ModelSamplingFlux, NunchakuFluxLoraLoader, BasicScheduler, BasicGuider, SamplerCustomAdvanced, VAEDecode, NunchakuFluxDiTLoader, PrimitiveNode, PrimitiveNode, RH_Translator, KSamplerSelect, EmptySD3LatentImage, BasicGuider, BasicScheduler, ModelSamplingFlux, easy cleanGpuUsed, PreviewImage, SaveImage, PrimitiveNode, ImageConcanate, easy cleanGpuUsed, CR Overlay Text, CR Overlay Text, PreviewImage, PreviewImage]
patterns: []
missing: [CR Overlay Text, CR Overlay Text, easy cleanGpuUsed, easy cleanGpuUsed]
discoveries: [次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/nunchaku-flux.1-dev & flux.1 krea-dev-8步快速出图-自动提示词_1954518475970625537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku-flux.1-dev & flux.1 krea-dev-8步快速出图-自动提示词_1954518475970625537.json`

## 结构

**节点**（37 个）：
- `ShowText|pysssss`
- `NunchakuFluxLoraLoader`
- `NunchakuFluxLoraLoader`
- `RH_LLMAPI_NODE`
- `VAEDecode`
- `FluxGuidance`
- `CLIPTextEncode`
- `NunchakuTextEncoderLoader`
- `NunchakuFluxDiTLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoader`
- `ModelSamplingFlux`
- `NunchakuFluxLoraLoader`
- `BasicScheduler`
- `BasicGuider`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `NunchakuFluxDiTLoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `RH_Translator`
- `KSamplerSelect`
- `EmptySD3LatentImage`
- `BasicGuider`
- `BasicScheduler`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `PreviewImage`
- `SaveImage`
- `PrimitiveNode`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `CR Overlay Text`
- `CR Overlay Text`
- `PreviewImage`
- `PreviewImage`

## 知识

覆盖率 **70%**（26/37）

**有卡**：`ShowText|pysssss`、`NunchakuFluxLoraLoader`、`RH_LLMAPI_NODE`、`VAEDecode`、`FluxGuidance`、`CLIPTextEncode`、`NunchakuTextEncoderLoader`、`NunchakuFluxDiTLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`VAELoader`、`ModelSamplingFlux`、`BasicScheduler`、`BasicGuider`、`PrimitiveNode`、`RH_Translator`、`KSamplerSelect`、`EmptySD3LatentImage`

**缺卡**（4）：`CR Overlay Text`、`CR Overlay Text`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

## 学习发现

- 次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
