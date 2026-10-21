---
name: unknown_workflow_lora_sampler_clip_112
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.851333
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [String Literal, easy seed]
members: [图片生成/文生图/1958755877442445314.json, 图片生成/文生图/1958819414923751425.json, 图片生成/文生图/1960378242681155586.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1958755877442445314.json、图片生成/文生图/1958819414923751425.json、图片生成/文生图/1960378242681155586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `ModelPatchLoader` —— 2/3 个有
- `QwenImageDiffsynthControlnet` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ResizeMask` —— 1/3 个有
- `SaveImageAndMetadata_` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy seed
