---
name: unknown_workflow_lora_sampler_clip_181
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.898333
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CR Model Input Switch, EmptyImage, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, ImageBatch, KSamplerSelect, LayerUtility: BooleanOperator, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RH_Captioner, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SaveImage, StringToInt, TextBox, VAEDecode, VAELoader, easy ifElse, easy imageSize, easy int, easy showAnything, easy textSwitch]
problems: []
missing: []
members: [图片生成/图生图/FLUX文生图【手写_反推】Nunchaku提速4连图_1957729971551961089.json, 图片生成/文生图/FLUX文生图 _ Nunchaku提速（4张）_1911226009696333826.json, 图片生成/文生图/FLUX文生图【手写_反推】Nunchaku提速4连图_1929402516499283970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_181

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX文生图【手写_反推】Nunchaku提速4连图_1957729971551961089.json、图片生成/文生图/FLUX文生图 _ Nunchaku提速（4张）_1911226009696333826.json、图片生成/文生图/FLUX文生图【手写_反推】Nunchaku提速4连图_1929402516499283970.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
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
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
