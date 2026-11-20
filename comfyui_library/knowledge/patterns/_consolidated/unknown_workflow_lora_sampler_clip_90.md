---
name: unknown_workflow_lora_sampler_clip_90
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.988143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-8步和4步对比_1955503632722661377.json, 图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1955586331033288705.json, 图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1970690059521454082.json, 图片生成/文生图/qwen-文生图_2090010243379060737.json, 图片生成/文生图/qwen2512文生图工作流_2068284987354476546.json, 图片生成/文生图/qwen2512粗线条水墨_2082670662396760065.json, 图片生成/文生图/超可爱的q版3d风格动画角色设计_2067581459497578498.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-8步和4步对比_1955503632722661377.json、图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1955586331033288705.json、图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1970690059521454082.json、图片生成/文生图/qwen-文生图_2090010243379060737.json、图片生成/文生图/qwen2512文生图工作流_2068284987354476546.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 5/7 个有
- `easy seed` —— 3/7 个有
- `LatentUpscaleBy` —— 2/7 个有
- `String Literal` —— 2/7 个有
- `UnetLoaderGGUF` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 12 | 7 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 12，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（25/7 个样本）：Steps较低可能导致细节不足
