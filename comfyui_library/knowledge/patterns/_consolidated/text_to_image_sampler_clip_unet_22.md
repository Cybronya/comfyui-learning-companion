---
name: text_to_image_sampler_clip_unet_22
type: Text To Image
frequency: 13
level: weak
coverage: 0.895308
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image Art文生图_2017603451194187778.json, 图片生成/文生图/Z image Art文生图_2017821403277430785.json, 图片生成/文生图/Z image Art文生图_2019704255820599297.json, 图片生成/文生图/Z image 文生图_1993886895799205889.json, 图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json, 图片生成/文生图/Z image绝对美写实人像｜美少女文生图质感在线_2101553419847815169.json, 图片生成/文生图/Z-Image-Turbo写真｜一键蜂腰身材曲线自定义调整_2101548693785759746.json, 图片生成/文生图/Z-Image基本文生图处理生成工作流工具包_2101786053643431937.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2097777800206970882.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2101478583771422722.json, 图片生成/文生图/动漫生图｜Anima base v1官方文生图直出_2089769718608650241.json, 图片生成/文生图/文生图基础流｜krea2文生图图生图双模式_2089846295853879298.json, 图片生成/文生图/极速版Krea2 Trubo文生图｜美商极高V2版 美感直接拉满_2105551057450524673.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Z image Art文生图_2017603451194187778.json、图片生成/文生图/Z image Art文生图_2017821403277430785.json、图片生成/文生图/Z image Art文生图_2019704255820599297.json、图片生成/文生图/Z image 文生图_1993886895799205889.json、图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/13 个有
- `JjkText` —— 8/13 个有
- `solarL_SaveImagesToZip` —— 8/13 个有
- `孤海注释` —— 8/13 个有
- `ConditioningZeroOut` —— 6/13 个有
- `PrimitiveInt` —— 4/13 个有
- `Int` —— 3/13 个有
- `ModelSamplingAuraFlow` —— 3/13 个有
- `SetNode` —— 2/13 个有
- `TextInput_` —— 2/13 个有
- `easy promptLine` —— 2/13 个有
- `AddLabel` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 13 | 61% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 46% |
| 采样算法 | er_sde | - | 13 | 62% |
| 调度器 | beta | - | 13 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 1440 | 13 | 0% |
| 高度 | 80 | 80 - 2160 | 13 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，13 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 er_sde，13 个样本，一致性 62%
- 调度器 最常用 beta，13 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1440，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 2160，13 个样本，取值分散，一致性仅 0%
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足
