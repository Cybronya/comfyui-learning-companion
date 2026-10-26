---
name: unknown_workflow_lora_sampler_unet_106
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.861143
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键精准人物替换 二创必备_2033184455149494273.json, 图片生成/图生图/产品图换装Clothes_swap_2055459015823511553.json, 图片生成/图生图/产品图的换装Clothes_swap_2055110104705454081.json, 图片生成/图生图/产品贴标_2049328622414073857.json, 图片生成/图生图/修图 改图  换装 换衣  电商服装展示_2095215433443012610.json, 图片生成/图生图/去除水印工作流_2078477762511327234.json, 图片生成/图生图/多图编辑替换神器FireRed-Image-Edit+1.1_2034432725708447746.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_106

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/一键精准人物替换 二创必备_2033184455149494273.json、图片生成/图生图/产品图换装Clothes_swap_2055459015823511553.json、图片生成/图生图/产品图的换装Clothes_swap_2055110104705454081.json、图片生成/图生图/产品贴标_2049328622414073857.json、图片生成/图生图/修图 改图  换装 换衣  电商服装展示_2095215433443012610.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 6/7 个有
- `LayerUtility: ImageReelComposit` —— 6/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `Int` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `PIP_图像联结` —— 1/7 个有
- `Text` —— 1/7 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 7 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 7 | 93% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，7 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
