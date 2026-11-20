---
name: unknown_workflow_sampler_checkpoint_vae_46
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.981333
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, GetImageSizeAndCount, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen-Edit Aio V5模型去水印_1979111339127902209.json, 平台全量/单图编辑Qwen-Edit 2511 Aio V16_2004825613858992130.json, 平台全量/🦖Qwen漫转变真（Anything 2 Real）_1997925160583880705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_46

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen-Edit Aio V5模型去水印_1979111339127902209.json、平台全量/单图编辑Qwen-Edit 2511 Aio V16_2004825613858992130.json、平台全量/🦖Qwen漫转变真（Anything 2 Real）_1997925160583880705.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `Float` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 768 | 768 - 768 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
