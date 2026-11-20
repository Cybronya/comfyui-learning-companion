---
name: unknown_workflow_lora_sampler_unet_78
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.768556
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/模特一键三视图_2041098956314251265.json, 图片生成/图生图/电商产品图片加文字做电商主图 FireRed_2027939825982115841.json, 图片生成/图生图/电商产品贴图 FireRed 1.1_2039972727704002561.json, 图片生成/图生图/电商假人模特转真人+FireRed+1.1_2045761264483307521.json, 图片生成/图生图/电商服装全自动换装+换衣+展示_2068367201345826818.json, 图片生成/图生图/电商服装展示  换装  换衣_2059722425989951489.json, 图片生成/图生图/直播宠物写真 FireRed 1.1_2060324746780307457.json, 图片生成/图生图/直播生成证件照 保持人物一致性+FireRed+1.1_2051579794864783362.json, 图片生成/图生图/贴身衣物一键溶图_2033158445423136769.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_78

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/模特一键三视图_2041098956314251265.json、图片生成/图生图/电商产品图片加文字做电商主图 FireRed_2027939825982115841.json、图片生成/图生图/电商产品贴图 FireRed 1.1_2039972727704002561.json、图片生成/图生图/电商假人模特转真人+FireRed+1.1_2045761264483307521.json、图片生成/图生图/电商服装全自动换装+换衣+展示_2068367201345826818.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 5/9 个有
- `LayerUtility: ImageReel` —— 4/9 个有
- `LayerUtility: ImageReelComposit` —— 4/9 个有
- `PreviewImage` —— 3/9 个有
- `BiRefNet_Hugo` —— 1/9 个有
- `FastCanvas` —— 1/9 个有
- `FastCanvasTool` —— 1/9 个有
- `easy getNode` —— 1/9 个有
- `easy setNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 9 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | beta | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 beta，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
