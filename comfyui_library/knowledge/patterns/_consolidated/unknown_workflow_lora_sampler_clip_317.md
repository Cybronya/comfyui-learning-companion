---
name: unknown_workflow_lora_sampler_clip_317
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.863
common_nodes: [BasicGuider, BasicScheduler, BatchCount+, CLIPTextEncode, DisableNoise, Display Int (rgthree), FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, ImageFromBatch, ImageGenResolutionFromImage, ImageTile+, ImageUntile+, InFluxModelSamplingPred, Int, LayerUtility: PurgeVRAM V2, LoadImage, MathExpression|pysssss, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, OutFluxModelSamplingPred, PreviewImage, SamplerCustomAdvanced, SaveImage, SaveImageToLocal, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [图片生成/图生图/平滑修图场景_2067132188365246465.json, 平台全量/8K实拍图片精修终极封装版本_1958058345657675777.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_317

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/平滑修图场景_2067132188365246465.json、平台全量/8K实拍图片精修终极封装版本_1958058345657675777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BatchCount+`
- `CLIPTextEncode`
- `DisableNoise`
- `Display Int (rgthree)`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `ImageFromBatch`
- `ImageGenResolutionFromImage`
- `ImageTile+`
- `ImageUntile+`
- `InFluxModelSamplingPred`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MathExpression|pysssss`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveImageToLocal`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
