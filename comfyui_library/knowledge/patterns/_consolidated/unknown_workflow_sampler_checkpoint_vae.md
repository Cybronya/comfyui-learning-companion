---
name: unknown_workflow_sampler_checkpoint_vae
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.896333
common_nodes: [CheckpointLoaderSimple, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, RHHiddenNodes, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/IP写真九宫格变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2509影楼写真_2035995310027186177.json, 图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2038273363747016706.json, 图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2038966204118867970.json, 图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2038968878218350593.json, 图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2043160913494155266.json, 图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2043526191616888834.json, 图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2055577841693151233.json, 图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）——影楼写真_2044395056760623105.json, 图片生成/图生图/IP文创九宫格变现利器Qwen-image-edit AIO_1993970158179991553.json, 图片生成/图生图/Qwen-Rapid-AIO V18 角色IP九宫格_1983502476076851201.json, 图片生成/图生图/图生图-明星写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511_2048962586577735682.json, 图片生成/图生图/水果专用九宫格qwan-image-edit_1993299515430076418.json, 图片生成/文生图/2031187599389364226.json, 图片生成/文生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image影楼写真_2038867949926223873.json, 图片生成/文生图/专为SeeDance 2.0AI短剧漫剧专用超真实感资产道具库QwenRapidAIO V23_2027230287247187970.json, 图片生成/文生图/十六宫变现利器（Qwen-image-edit2511写真）_2045435852054073345.json, 图片生成/文生图/超真实感道具生成_2027209573307785218.json, 图片生成/文生图/道具库QwenRapidAIO+V23_2027221533550190594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/IP写真九宫格变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2509影楼写真_2035995310027186177.json、图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2038273363747016706.json、图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2038966204118867970.json、图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2038968878218350593.json、图片生成/图生图/IP写真十六宫变现利器（人物、动漫、宠物、拟人全类型）Qwen-image-edit2511影楼写真_2043160913494155266.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `RHHiddenNodes`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 16/18 个有
- `LoraLoaderModelOnly` —— 15/18 个有
- `PrimitiveStringMultiline` —— 13/18 个有
- `easy showAnything` —— 13/18 个有
- `easy imageRemBg` —— 7/18 个有
- `CR Text` —— 4/18 个有
- `EmptyLatentImage` —— 2/18 个有
- `ImpactInt` —— 2/18 个有
- `LoadImage` —— 1/18 个有
- `TextConcat` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta57 | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 600 | - | 2 | 100% |
| 高度 | 800 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta57，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 600，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 800，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
