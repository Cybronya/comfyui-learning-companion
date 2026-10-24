---
name: unknown_workflow_lora_sampler_clip_199
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.887
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LatentCutToBatch, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-layered海报生成_2002548035265654786.json, 图片生成/文生图/qwen-image-layered-t2i-分层式生图-文生图-图片反推_2003319772265775105.json, 图片生成/文生图/qwen-image-layered-t2i_2002756318526074881.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-layered海报生成_2002548035265654786.json、图片生成/文生图/qwen-image-layered-t2i-分层式生图-文生图-图片反推_2003319772265775105.json、图片生成/文生图/qwen-image-layered-t2i_2002756318526074881.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LatentCutToBatch`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `CR Text Replace` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LatentFromBatch` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | lcm | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
