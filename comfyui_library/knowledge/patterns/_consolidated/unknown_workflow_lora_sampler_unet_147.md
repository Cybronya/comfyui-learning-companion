---
name: unknown_workflow_lora_sampler_unet_147
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.723
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/最强电商模特换脸_2037072797817638913.json, 平台全量/模特多图参考产品展示 FireRed 1.1_2034446699824947202.json, 平台全量/电商产品图精修 FireRed_2030836502543998978.json, 平台全量/电商图片万物移除 FireRed_2029743755623927809.json, 平台全量/电商图片洗图  FireRed_2029384841199886337.json, 平台全量/电商模特服装提取 FireRed_2031180860698927105.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_147

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/最强电商模特换脸_2037072797817638913.json、平台全量/模特多图参考产品展示 FireRed 1.1_2034446699824947202.json、平台全量/电商产品图精修 FireRed_2030836502543998978.json、平台全量/电商图片万物移除 FireRed_2029743755623927809.json、平台全量/电商图片洗图  FireRed_2029384841199886337.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：72%

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
- `JjkText` —— 5/6 个有
- `JoinStrings` —— 2/6 个有
- `Qwen3VL_Chat` —— 2/6 个有
- `ShowText` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `Colored Image (mtb)` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `RH_Captioner_Pro` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
