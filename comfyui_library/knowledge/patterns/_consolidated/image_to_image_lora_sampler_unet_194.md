---
name: image_to_image_lora_sampler_unet_194
type: Image To Image
frequency: 3
level: strong
coverage: 0.654
common_nodes: [CLIPLoader, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 edit turbo 文改图工作流_2080951422828503042.json, 图片生成/文生图/单图生成三视图完整工作流（模版一）消耗积分：KREA-2-EDIT版本_2088932692376248322.json, 图片生成/文生图/单图生成人物资产三视图完整工作流_2095809006400004097.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/krea2 edit turbo 文改图工作流_2080951422828503042.json、图片生成/文生图/单图生成三视图完整工作流（模版一）消耗积分：KREA-2-EDIT版本_2088932692376248322.json、图片生成/文生图/单图生成人物资产三视图完整工作流_2095809006400004097.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `Textbox` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `ImageResize+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
