---
name: unknown_workflow_lora_sampler_clip_200
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/厚涂cg画风-moss_2116722911682846721.json, 图片生成/文生图/轮回画风-moss_2116483754695942145.json, 平台全量/国漫cg画风-moss_2117207553963814914.json, 平台全量/韩系女生插画画风-moss_2117208380271063041.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_200

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/厚涂cg画风-moss_2116722911682846721.json、图片生成/文生图/轮回画风-moss_2116483754695942145.json、平台全量/国漫cg画风-moss_2117207553963814914.json、平台全量/韩系女生插画画风-moss_2117208380271063041.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 2/4 个有
- `LatentUpscaleBy` —— 1/4 个有
- `Qwen2.5` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 8 | 4 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.7 - 1 | 4 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，4 个样本，取值集中（一致性 86%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
