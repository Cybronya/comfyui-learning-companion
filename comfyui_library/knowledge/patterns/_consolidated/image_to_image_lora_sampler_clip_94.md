---
name: image_to_image_lora_sampler_clip_94
type: Image To Image
frequency: 4
level: strong
coverage: 0.833
common_nodes: [ApplyFBCacheOnModel, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageResize+, ImpactInt, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SetNode, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy mathString]
problems: []
missing: []
members: [图片生成/图生图/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_2087195460535668738.json, 图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json, 平台全量/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_1964520134234787842.json, 平台全量/Kontext白昼一键灯光交替_1970502540901163009.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_2087195460535668738.json、图片生成/图生图/F.1-Kontext 自动转换 白天 ⇄ 夜晚_夜晚 ⇄ 白天_2109093477630959617.json、平台全量/F.1-Kontext 白天 ⇄ 夜晚（自动切换）_1964520134234787842.json、平台全量/Kontext白昼一键灯光交替_1970502540901163009.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
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
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
