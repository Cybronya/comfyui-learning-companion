---
name: unknown_workflow_sampler_clip_unet_263
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.788
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein-9B-True-bf16_2024822336939106306.json, 图片生成/文生图/Zimage生图-随机增强-两步法_2004931976354299905.json, 图片生成/文生图/ernie+klein双采_2045055189861801985.json, 图片生成/文生图/ernie+zit双采样_2045054582375587842.json, 图片生成/文生图/百度ernie+zit双采样_2045695437658656770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_263

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein-9B-True-bf16_2024822336939106306.json、图片生成/文生图/Zimage生图-随机增强-两步法_2004931976354299905.json、图片生成/文生图/ernie+klein双采_2045055189861801985.json、图片生成/文生图/ernie+zit双采样_2045054582375587842.json、图片生成/文生图/百度ernie+zit双采样_2045695437658656770.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `MuyeSizeSelector` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 25 | 5 | 44% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 60% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 25，5 个样本，取值分散，一致性仅 44%
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
