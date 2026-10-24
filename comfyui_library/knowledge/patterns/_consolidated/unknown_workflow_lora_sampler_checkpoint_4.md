---
name: unknown_workflow_lora_sampler_checkpoint_4
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.870667
common_nodes: [AutoCropFaces, CheckpointLoaderSimple, EmptyLatentImage, ImageLoader, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, WujiCleaner, WujiStyleSelector]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/IP写真九宫格变现利器（人物、动漫、宠物、拟人全类型）Krea2影楼写真_1990631741633302530.json, 图片生成/图生图/IP写真九宫格变现利器（人物、动漫、宠物、拟人全类型）Krea2影楼写真_2091114914478907393.json, 图片生成/图生图/IP写真九宫格影楼写真（人物、动漫、宠物、拟人全类型）_2098989949889634305.json, 图片生成/图生图/Krea2影楼写真_九宫格变现利器_2091797572871614465.json, 图片生成/图生图/旅游网红打卡写真九宫变现利器（人物、动漫、宠物、拟人全类型）Krea2影楼写真_2038299433443532801.json, 图片生成/图生图/旅游网红打卡写真九宫变现利器（人物、动漫、宠物、拟人全类型）Krea2影楼写真_2091121282367705090.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/IP写真九宫格变现利器（人物、动漫、宠物、拟人全类型）Krea2影楼写真_1990631741633302530.json、图片生成/图生图/IP写真九宫格变现利器（人物、动漫、宠物、拟人全类型）Krea2影楼写真_2091114914478907393.json、图片生成/图生图/IP写真九宫格影楼写真（人物、动漫、宠物、拟人全类型）_2098989949889634305.json、图片生成/图生图/Krea2影楼写真_九宫格变现利器_2091797572871614465.json、图片生成/图生图/旅游网红打卡写真九宫变现利器（人物、动漫、宠物、拟人全类型）Krea2影楼写真_2038299433443532801.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `AutoCropFaces`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageLoader`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `WujiCleaner`
- `WujiStyleSelector`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
