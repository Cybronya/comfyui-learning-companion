---
name: image_to_image_lora_sampler_clip_65
type: Image To Image
frequency: 5
level: strong
coverage: 0.8818
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/首饰草图转换首饰草图转换V1.0_2094360265574928385.json, 图片生成/图生图/高阶 FLUX 2 Klein 9B  动漫场景设计稿上色优化工作流_2049037571455459329.json, 图片生成/文生图/溜溜：flux2-klein+z-image动漫转真人_2048293605856518145.json, 图片生成/文生图/空白工作流_2088539683264483329.json, 数字人/数字人/空白工作流_2088544556475305986.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/首饰草图转换首饰草图转换V1.0_2094360265574928385.json、图片生成/图生图/高阶 FLUX 2 Klein 9B  动漫场景设计稿上色优化工作流_2049037571455459329.json、图片生成/文生图/溜溜：flux2-klein+z-image动漫转真人_2048293605856518145.json、图片生成/文生图/空白工作流_2088539683264483329.json、数字人/数字人/空白工作流_2088544556475305986.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `easy promptConcat` —— 3/5 个有
- `Float` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `Checkpoint Loader (Simple)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.5 - 1 | 5 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，5 个样本
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
