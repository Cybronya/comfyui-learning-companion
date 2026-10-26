---
name: unknown_workflow_lora_sampler_clip_321
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.902
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyImage, EmptySD3LatentImage, Fast Groups Muter (rgthree), FluxGuidance, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RH_Captioner, RH_LLMAPI_NODE, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, TextBox, VAEDecode, VAELoader, easy imageConcat, easy imageSize, easy mathInt, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/文生图_反推洗图 _ 双截棍+kontext （速度极快）_1940255430561976321.json, 图片生成/文生图/文生图_反推洗图 _ 双截棍+kontext_1944008228478812161.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_321

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图_反推洗图 _ 双截棍+kontext （速度极快）_1940255430561976321.json、图片生成/文生图/文生图_反推洗图 _ 双截棍+kontext_1944008228478812161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptySD3LatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextBox`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`
- `easy imageSize`
- `easy mathInt`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
