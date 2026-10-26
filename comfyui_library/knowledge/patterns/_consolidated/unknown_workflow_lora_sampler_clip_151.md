---
name: unknown_workflow_lora_sampler_clip_151
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.951
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, ColorCorrect, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Image Comparer (rgthree), ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAELoader, 取色器_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/商业级人像精修---校色+祛痘+磨皮+改背景色_2086642122295439361.json, 图片生成/图生图/商业级人像精修---校色+祛痘+磨皮+改背景色_2090271814491660290.json, 图片生成/图生图/商业级人像精修【极速版】——校色+祛痘+磨皮+改背景色_2089731406929940481.json, 图片生成/图生图/商业级人像精修【极速版】——校色+祛痘+磨皮+改背景色_2089731592951521282.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/商业级人像精修---校色+祛痘+磨皮+改背景色_2086642122295439361.json、图片生成/图生图/商业级人像精修---校色+祛痘+磨皮+改背景色_2090271814491660290.json、图片生成/图生图/商业级人像精修【极速版】——校色+祛痘+磨皮+改背景色_2089731406929940481.json、图片生成/图生图/商业级人像精修【极速版】——校色+祛痘+磨皮+改背景色_2089731592951521282.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `ColorCorrect`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `取色器_孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
