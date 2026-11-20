---
name: text_to_image_controlnet_inpaint_lora_12
type: Text To Image
frequency: 2
level: weak
coverage: 0.86
common_nodes: [ApplyInstantID, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropFaces, DeepTranslatorTextNode, DetectFaces, DualCLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImagePass, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: TextJoin, LoadImage, Mask Invert, MaskPreview+, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, RandomNoise, SAMModelLoader (segment anything), SamplerCustomAdvanced, SaveImage, Seed Everywhere, ShowText|pysssss, TextInput_, VAEDecode, VAELoader, WarpFacesBack, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/文生宠物合影换脸，万能清晰加速版_2000539300594843649.json, 平台全量/宠物合影换脸加速版-小宣喧_1837825435320172546.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生宠物合影换脸，万能清晰加速版_2000539300594843649.json、平台全量/宠物合影换脸加速版-小宣喧_1837825435320172546.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `CropFaces`
- `DeepTranslatorTextNode`
- `DetectFaces`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImagePass`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: TextJoin`
- `LoadImage`
- `Mask Invert`
- `MaskPreview+`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SAMModelLoader (segment anything)`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `ShowText|pysssss`
- `TextInput_`
- `VAEDecode`
- `VAELoader`
- `WarpFacesBack`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1600 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.55 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1600，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.55，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
