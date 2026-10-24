---
name: unknown_workflow_sampler_clip_unet_370
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.649
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, FluxKontextMultiReferenceLatentMethod, KSamplerSelect, ModelSamplingAuraFlow, RandomNoise, SamplerCustomAdvanced, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein 光速文生图&图生图&多图编辑大合集_2012036300836179970.json, 图片生成/文生图/yxmys-遗物生成_2039166117398192130.json, 图片生成/文生图/游戏道具图标生成+全节点注释_2039697938036822018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_370

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein 光速文生图&图生图&多图编辑大合集_2012036300836179970.json、图片生成/文生图/yxmys-遗物生成_2039166117398192130.json、图片生成/文生图/游戏道具图标生成+全节点注释_2039697938036822018.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxKontextMultiReferenceLatentMethod`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AV_LoraLoader` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `MultiTextConcatenate` —— 2/3 个有
- `MuyeTextEditOutput` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `Text` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
