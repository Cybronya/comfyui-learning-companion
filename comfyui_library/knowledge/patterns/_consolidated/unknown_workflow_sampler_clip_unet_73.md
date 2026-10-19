---
name: unknown_workflow_sampler_clip_unet_73
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.72925
common_nodes: [BasicScheduler, CFGGuider, CFGZeroStar, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLatentImage, ImpactInt, KSamplerSelect, RHHiddenNodes, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch]
problems: []
missing: [CR Text, easy anythingIndexSwitch]
members: [图片生成/文生图/1973180639434420225.json, 图片生成/文生图/1973209784952467457.json, 图片生成/文生图/1973223203931820034.json, 视频生成/图生视频/1973209784952467457.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1973180639434420225.json、图片生成/文生图/1973209784952467457.json、图片生成/文生图/1973223203931820034.json、视频生成/图生视频/1973209784952467457.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CFGZeroStar`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImpactInt`
- `KSamplerSelect`
- `RHHiddenNodes`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 4 | 100% |
| 高度 | 1920 | 1920 - 1920 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy anythingIndexSwitch
