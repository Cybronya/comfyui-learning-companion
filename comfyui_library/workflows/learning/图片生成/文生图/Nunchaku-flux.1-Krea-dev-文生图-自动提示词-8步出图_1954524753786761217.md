---
key: 图片生成/文生图/Nunchaku-flux.1-Krea-dev-文生图-自动提示词-8步出图_1954524753786761217.json
name: Nunchaku-flux.1-Krea-dev-文生图-自动提示词-8步出图_1954524753786761217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku-flux.1-Krea-dev-文生图-自动提示词-8步出图_1954524753786761217.json
hash: 34d27ead8c4cdc86
coverage: 0.772727
learned_at: 2026-10-10 20:58:48
nodes: [ModelSamplingFlux, NunchakuTextEncoderLoader, KSamplerSelect, RandomNoise, NunchakuFluxLoraLoader, ShowText|pysssss, RH_LLMAPI_NODE, NunchakuFluxDiTLoader, PrimitiveNode, CLIPTextEncode, FluxGuidance, EmptyLatentImage, SaveImage, PreviewImage, VAEDecode, SamplerCustomAdvanced, BasicGuider, VAELoader, RH_Translator, BasicScheduler, PrimitiveNode, PrimitiveNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Nunchaku-flux.1-Krea-dev-文生图-自动提示词-8步出图_1954524753786761217.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku-flux.1-Krea-dev-文生图-自动提示词-8步出图_1954524753786761217.json`

## 结构

**节点**（22 个）：
- `ModelSamplingFlux`
- `NunchakuTextEncoderLoader`
- `KSamplerSelect`
- `RandomNoise`
- `NunchakuFluxLoraLoader`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `NunchakuFluxDiTLoader`
- `PrimitiveNode`
- `CLIPTextEncode`
- `FluxGuidance`
- `EmptyLatentImage`
- `SaveImage`
- `PreviewImage`
- `VAEDecode`
- `SamplerCustomAdvanced`
- `BasicGuider`
- `VAELoader`
- `RH_Translator`
- `BasicScheduler`
- `PrimitiveNode`
- `PrimitiveNode`

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `width` = `1024`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`ModelSamplingFlux`、`NunchakuTextEncoderLoader`、`KSamplerSelect`、`RandomNoise`、`NunchakuFluxLoraLoader`、`ShowText|pysssss`、`RH_LLMAPI_NODE`、`NunchakuFluxDiTLoader`、`PrimitiveNode`、`CLIPTextEncode`、`FluxGuidance`、`EmptyLatentImage`、`SaveImage`、`PreviewImage`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`
