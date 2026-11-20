---
name: image_to_image_sampler_clip_unet_193
type: Image To Image
frequency: 3
level: strong
coverage: 0.979333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Kontext试衣间_1956916086128173058.json, 平台全量/kontext fp8 老照片修复_1955809962732634113.json, 平台全量/kontext一键取衣去人（去掉人物只留衣服）_1963049005674631169.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_193

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Kontext试衣间_1956916086128173058.json、平台全量/kontext fp8 老照片修复_1955809962732634113.json、平台全量/kontext一键取衣去人（去掉人物只留衣服）_1963049005674631169.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Random Line` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
