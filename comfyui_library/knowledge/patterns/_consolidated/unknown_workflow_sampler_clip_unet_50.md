---
name: unknown_workflow_sampler_clip_unet_50
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.922059
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/自己用：标题字设计_qwen-image-2.0_1971022262755332097.json, 图片生成/文生图/1 超清人像 Z-image turbo_2071175125273239553.json, 图片生成/文生图/2029905977360785409.json, 图片生成/文生图/Qwen-Image基础工作流_1954423623698280449.json, 图片生成/文生图/QwenImage Comfyui官方工作流_1952820714467487746.json, 图片生成/文生图/QwenImage Comfyui官方工作流_1952877428207194113.json, 图片生成/文生图/Qwen千问图像大模型_1953710081516994562.json, 图片生成/文生图/Qwen文生图_1957383820934836225.json, 图片生成/文生图/Z-Image-Turbo 8步出图_2005643797847572481.json, 图片生成/文生图/Z-Image-Turbo基础文生图-工作流_2011542094619353089.json, 图片生成/文生图/Z-Image_turbo工作流_2066470777045741570.json, 图片生成/文生图/Z-Image批量文生图_1993908239676932097.json, 图片生成/文生图/千问AI工作台_字体生成_2048680548826091521.json, 图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json, 图片生成/文生图/字体设计_qwen-image-2.0_2037759609598906370.json, 平台全量/字体设计_qwen-imag_2.0_1953416801168359426.json, 平台全量/字体设计_qwen-image-2.0_1953485836962725889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_50

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/自己用：标题字设计_qwen-image-2.0_1971022262755332097.json、图片生成/文生图/1 超清人像 Z-image turbo_2071175125273239553.json、图片生成/文生图/2029905977360785409.json、图片生成/文生图/Qwen-Image基础工作流_1954423623698280449.json、图片生成/文生图/QwenImage Comfyui官方工作流_1952820714467487746.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/17 个有
- `ModelSamplingAuraFlow` —— 15/17 个有
- `PreviewImage` —— 10/17 个有
- `easy promptList` —— 8/17 个有
- `CR Text` —— 6/17 个有
- `CR Text Input Switch (4 way)` —— 6/17 个有
- `CR Text Replace` —— 6/17 个有
- `Bookmark (rgthree)` —— 1/17 个有
- `FromListGet1Image` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 17 | 58% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 17 | 50% |
| 采样算法 | euler | - | 17 | 82% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，17 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，17 个样本，取值分散，一致性仅 50%
- 采样算法 最常用 euler，17 个样本，一致性 82%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（10/17 个样本）：Steps较低可能导致细节不足
