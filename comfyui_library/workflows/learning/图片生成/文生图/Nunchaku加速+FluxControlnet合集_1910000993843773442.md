---
key: Nunchaku加速+FluxControlnet合集_1910000993843773442.json
name: Nunchaku加速+FluxControlnet合集_1910000993843773442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku加速+FluxControlnet合集_1910000993843773442.json
hash: 1f774f63867c8cf8
coverage: 0.813333
learned_at: 2026-10-10 20:58:48
nodes: [KSamplerSelect, NunchakuFluxDiTLoader, ModelSamplingFlux, SamplerCustomAdvanced, DifferentialDiffusion, Note, ACN_AdvancedControlNetApplySingle_v2, SetUnionControlNetType, AIO_Preprocessor, SetUnionControlNetType, AIO_Preprocessor, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, ControlNetLoader, Reroute, KSamplerSelect, VAEDecode, DifferentialDiffusion, Note, ACN_AdvancedControlNetApplySingle_v2, SetUnionControlNetType, AIO_Preprocessor, SetUnionControlNetType, AIO_Preprocessor, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, Reroute, ControlNetLoader, BasicGuider, FluxGuidance, VAEEncode, NunchakuFluxLoraLoader, SetUnionControlNetType, VAELoader, EmptyLatentImage, AIO_Preprocessor, RandomNoise, BasicScheduler, VAELoader, RandomNoise, ConstrainImage|pysssss, ModelSamplingFlux, GetImageSize, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, NunchakuFluxLoraLoader, BasicScheduler, SamplerCustomAdvanced, CR Latent Batch Size, NunchakuTextEncoderLoader, FluxGuidance, BasicGuider, CLIPTextEncode, Reroute, Reroute, SaveImage, VAEDecode, Image Comparer (rgthree), ACN_AdvancedControlNetApplySingle_v2, CLIPTextEncode, SaveImage, LoadImage, Image Comparer (rgthree), Reroute, Get resolution [Crystools], CR Text, ConstrainImage|pysssss, LoadImage]
patterns: []
missing: [CR Text, ConstrainImage|pysssss, ConstrainImage|pysssss, CR Latent Batch Size, Get resolution [Crystools]]
parameters: {"batch_size": 1, "controlnet_strength": 0.7000000000000002, "height": 1024, "width": 952}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Latent Batch Size` 仅有 VAE/Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# Nunchaku加速+FluxControlnet合集_1910000993843773442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku加速+FluxControlnet合集_1910000993843773442.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `KSamplerSelect` ★核心
- `NunchakuFluxDiTLoader`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `DifferentialDiffusion`
- `Note`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `ControlNetLoader`
- `Reroute`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `DifferentialDiffusion`
- `Note`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `Reroute`
- `ControlNetLoader`
- `BasicGuider`
- `FluxGuidance`
- `VAEEncode` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `SetUnionControlNetType`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `AIO_Preprocessor`
- `RandomNoise`
- `BasicScheduler`
- `VAELoader`
- `RandomNoise`
- `ConstrainImage|pysssss`
- `ModelSamplingFlux`
- `GetImageSize`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `NunchakuFluxLoraLoader` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `CR Latent Batch Size`
- `NunchakuTextEncoderLoader`
- `FluxGuidance`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Reroute`
- `Get resolution [Crystools]`
- `CR Text`
- `ConstrainImage|pysssss`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.7000000000000002`
- `width` = `952`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（61/75）

**有卡**：`KSamplerSelect`、`NunchakuFluxDiTLoader`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`DifferentialDiffusion`、`ACN_AdvancedControlNetApplySingle_v2`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ControlNetLoader`、`VAEDecode`、`BasicGuider`、`FluxGuidance`、`VAEEncode`、`NunchakuFluxLoraLoader`、`VAELoader`、`EmptyLatentImage`、`RandomNoise`、`BasicScheduler`、`GetImageSize`、`NunchakuTextEncoderLoader`、`CLIPTextEncode`、`SaveImage`、`LoadImage`

**缺卡**（5）：`CR Text`、`ConstrainImage|pysssss`、`ConstrainImage|pysssss`、`CR Latent Batch Size`、`Get resolution [Crystools]`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、SetUnionControlNetType、ACN_AdvancedControlNetApplySingle_v2

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Latent Batch Size` 仅有 VAE/Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明
