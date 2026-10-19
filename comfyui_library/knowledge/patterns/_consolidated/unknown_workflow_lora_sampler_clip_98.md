---
name: unknown_workflow_lora_sampler_clip_98
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7025
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CR Model Input Switch, EmptyImage, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, ImageBatch, KSamplerSelect, LayerUtility: BooleanOperator, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RH_Captioner, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SaveImage, StringToInt, TextBox, VAEDecode, VAELoader, easy ifElse, easy imageSize, easy int, easy showAnything, easy textSwitch]
problems: []
missing: [CR Model Input Switch, LayerUtility: BooleanOperator, easy int, easy textSwitch, easy imageSize]
members: [图片生成/文生图/1911226009696333826.json, 图片生成/文生图/1929402516499283970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1911226009696333826.json、图片生成/文生图/1929402516499283970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Model Input Switch`
- `EmptyImage`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `ImageBatch`
- `KSamplerSelect`
- `LayerUtility: BooleanOperator`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringToInt`
- `TextBox`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy int`
- `easy showAnything`
- `easy textSwitch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Model Input Switch、LayerUtility: BooleanOperator、easy int、easy textSwitch、easy imageSize
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
