---
name: image_to_image_lora_sampler_unet_141
type: Image To Image
frequency: 6
level: strong
coverage: 0.916
common_nodes: [DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/kontext-dev-儿童手绘具象化_1947559305114492929.json, 平台全量/产品光影溶图_1955860262287015937.json, 平台全量/人像光影融合-MAGIC-K-V1_2001594272090583041.json, 平台全量/光影融合工作流_1955137691119751170.json, 平台全量/婚纱摄影 季节变换 梦幻雪景 kontext 图片变雪景 冬季雪景氛围 一键变下雪_2002561774287241217.json, 平台全量/电商跟品模特姿势套图裂变-mazh_1993861379912384514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_141

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/kontext-dev-儿童手绘具象化_1947559305114492929.json、平台全量/产品光影溶图_1955860262287015937.json、平台全量/人像光影融合-MAGIC-K-V1_2001594272090583041.json、平台全量/光影融合工作流_1955137691119751170.json、平台全量/婚纱摄影 季节变换 梦幻雪景 kontext 图片变雪景 冬季雪景氛围 一键变下雪_2002561774287241217.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `Anything Everywhere` —— 2/6 个有
- `ConstrainImage|pysssss` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `easy positive` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `CLIPTextEncodeBREAK` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LoraLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
