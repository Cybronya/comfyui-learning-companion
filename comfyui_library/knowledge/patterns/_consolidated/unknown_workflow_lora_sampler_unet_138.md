---
name: unknown_workflow_lora_sampler_unet_138
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.883
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/模特一键三视图_2041098956314251265.json, 图片生成/图生图/温暖日光CCD_2075075472152682497.json, 图片生成/图生图/电商服装全自动换装+换衣+展示_2068367201345826818.json, 图片生成/图生图/电商服装展示  换装  换衣_2059722425989951489.json, 图片生成/图生图/贴身衣物一键溶图_2033158445423136769.json, 平台全量/三视图 _QWEN-EDIT-AIO-一键三视图 精简版_1982113252421320706.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_138

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/模特一键三视图_2041098956314251265.json、图片生成/图生图/温暖日光CCD_2075075472152682497.json、图片生成/图生图/电商服装全自动换装+换衣+展示_2068367201345826818.json、图片生成/图生图/电商服装展示  换装  换衣_2059722425989951489.json、图片生成/图生图/贴身衣物一键溶图_2033158445423136769.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `easy getNode` —— 2/6 个有
- `easy setNode` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `BiRefNet_Hugo` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `FastCanvas` —— 1/6 个有
- `FastCanvasTool` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `KOOK_SaveJPGImage` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 6 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
