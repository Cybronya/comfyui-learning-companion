---
name: unknown_workflow_lora_sampler_clip_106
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.707
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyImage, EmptySD3LatentImage, Fast Groups Muter (rgthree), FluxGuidance, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RH_Captioner, RH_LLMAPI_NODE, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, TextBox, VAEDecode, VAELoader, easy imageConcat, easy imageSize, easy mathInt, easy showAnything]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy imageConcat, easy mathInt, easy imageSize]
members: [图片生成/文生图/1940255430561976321.json, 图片生成/文生图/1944008228478812161.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1940255430561976321.json、图片生成/文生图/1944008228478812161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

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

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy imageConcat、easy mathInt、easy imageSize
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
