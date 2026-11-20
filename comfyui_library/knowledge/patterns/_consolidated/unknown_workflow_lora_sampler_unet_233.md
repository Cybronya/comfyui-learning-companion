---
name: unknown_workflow_lora_sampler_unet_233
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.83825
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/一键换装-换衣服_2071868765691793410.json, 平台全量/无遮罩控制 全自动换装  全自动服装迁移_2045359294048116738.json, 平台全量/模特一键换装+完美替换衣物，超高一致性保持_2064953407315734529.json, 平台全量/👉千问遮罩换装 更好一致性 支持遮罩 🧁_1989599912960643074.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_233

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/一键换装-换衣服_2071868765691793410.json、平台全量/无遮罩控制 全自动换装  全自动服装迁移_2045359294048116738.json、平台全量/模特一键换装+完美替换衣物，超高一致性保持_2064953407315734529.json、平台全量/👉千问遮罩换装 更好一致性 支持遮罩 🧁_1989599912960643074.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `QwenEditAdaptiveLongestEdge` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
