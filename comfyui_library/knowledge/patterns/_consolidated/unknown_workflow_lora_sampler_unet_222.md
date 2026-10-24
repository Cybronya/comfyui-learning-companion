---
name: unknown_workflow_lora_sampler_unet_222
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.636
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen-Edit2509 双图融合_1999735236688740354.json, 图片生成/图生图/千问Qwen-Edit2509多图融合-多实例1.0-test_2000486442172284930.json, 图片生成/文生图/观行➡️qwen_image_edit_plus人物换装_1974486765111218177.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_222

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问Qwen-Edit2509 双图融合_1999735236688740354.json、图片生成/图生图/千问Qwen-Edit2509多图融合-多实例1.0-test_2000486442172284930.json、图片生成/文生图/观行➡️qwen_image_edit_plus人物换装_1974486765111218177.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Seed` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `GetImageSize+` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 30 | 3 | 43% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 30，3 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
