---
name: image_to_image_sampler_clip_unet_120
type: Image To Image
frequency: 4
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2-半身转全身-三视图_2054190538517172226.json, 图片生成/图生图/zimageturbo图反推，根据反推生图_1998683765151031298.json, 图片生成/图生图/人物换装   Klein_2029535177847869442.json, 图片生成/文生图/Flux2图像编辑工作流_1993535727956852738.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux2-半身转全身-三视图_2054190538517172226.json、图片生成/图生图/zimageturbo图反推，根据反推生图_1998683765151031298.json、图片生成/图生图/人物换装   Klein_2029535177847869442.json、图片生成/文生图/Flux2图像编辑工作流_1993535727956852738.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `FluxGuidance` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `PurgeVRAM_UTK` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 20 | 4 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 20，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
