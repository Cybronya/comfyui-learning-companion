---
name: image_to_image_lora_sampler_clip_125
type: Image To Image
frequency: 2
level: weak
coverage: 0.833
common_nodes: [ApplyFBCacheOnModel, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageResize+, ImpactInt, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SetNode, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy mathString]
problems: []
missing: []
members: [图片生成/图生图/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_2087195460535668738.json, 图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_2087195460535668738.json、图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactInt`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy mathString`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
