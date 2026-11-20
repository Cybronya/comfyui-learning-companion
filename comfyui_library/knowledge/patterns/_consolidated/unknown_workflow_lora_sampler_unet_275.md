---
name: unknown_workflow_lora_sampler_unet_275
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.874333
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/8步加速-QwenEdit图像编辑无位置偏移_1969228365477650434.json, 平台全量/Qwen edit保持一致性编辑工作流_1969014617370468353.json, 平台全量/图片编辑Qwen-image-edit_1958912056361693185.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_275

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/8步加速-QwenEdit图像编辑无位置偏移_1969228365477650434.json、平台全量/Qwen edit保持一致性编辑工作流_1969014617370468353.json、平台全量/图片编辑Qwen-image-edit_1958912056361693185.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ImageConcanate` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
