---
name: text_to_image_sampler_clip_checkpoint_8
type: Text To Image
frequency: 11
level: moderate
coverage: 0.960636
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/二分爱良配_2049140660023861250.json, 图片生成/文生图/剪影块面分割_2061724652694757378.json, 图片生成/文生图/文生图-线稿_2045431527156228098.json, 图片生成/文生图/文生图-转手绘_2054201953059647490.json, 图片生成/文生图/海洋_2069833381461970945.json, 图片生成/文生图/清晰_2013889963875639297.json, 图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json, 图片生成/文生图/质感笔触干练_2060512709078241281.json, 图片生成/文生图/赛博废土带笔触场景_2063495974462513153.json, 图片生成/文生图/酒馆2D角色卡封面生成_2002452758932385793.json, 平台全量/毛毡世界_1797856564732882946.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/二分爱良配_2049140660023861250.json、图片生成/文生图/剪影块面分割_2061724652694757378.json、图片生成/文生图/文生图-线稿_2045431527156228098.json、图片生成/文生图/文生图-转手绘_2054201953059647490.json、图片生成/文生图/海洋_2069833381461970945.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 10/11 个有
- `LatentUpscaleBy` —— 7/11 个有
- `CLIPSetLastLayer` —— 4/11 个有
- `KSampler //Inspire` —— 4/11 个有
- `PreviewImage` —— 3/11 个有
- `VAEEncode` —— 2/11 个有
- `HAIGC_SaveImagesToZip` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.475 | 0.2 - 0.85 | 10 | 63% |
| LoRA 文本强度 | 0.475 | 0.28 - 1 | 10 | 52% |
| 采样步数 | 25 | 5 - 40 | 11 | 66% |
| Prompt 约束强度(CFG) | 7 | 2 - 8 | 11 | 66% |
| 采样算法 | euler_ancestral | - | 11 | 55% |
| 调度器 | normal | - | 11 | 45% |
| 重绘幅度 | 1 | 0.4 - 1 | 11 | 74% |
| 宽度 | 768 | 608 - 1568 | 11 | 68% |
| 高度 | 1024 | 720 - 1280 | 11 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.475，观测区间 0.2 - 0.85，10 个样本
- LoRA 文本强度 中位数 0.475，观测区间 0.28 - 1，10 个样本
- 采样步数 中位数 25，观测区间 5 - 40，11 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 2 - 8，11 个样本
- 采样算法 最常用 euler_ancestral，11 个样本，一致性 55%
- 调度器 最常用 normal，11 个样本，一致性 45%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，11 个样本
- 宽度 中位数 768，观测区间 608 - 1568，11 个样本
- 高度 中位数 1024，观测区间 720 - 1280，11 个样本
