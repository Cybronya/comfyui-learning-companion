---
name: unknown_workflow_sampler_clip_checkpoint_34
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.778
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyHiDreamO1LatentImage, HiDreamO1PatchSeamSmoothing, JjkText, KSampler, ModelNoiseScale, PrimitiveBoolean, SaveImage, VAEDecode, easy ifElse, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/hidream o1 2604 + zimage细化 文生图_2057083543095963650.json, 图片生成/文生图/hidream o1 2604 文生图 提示词增强_2057018930434232322.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_34

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/hidream o1 2604 + zimage细化 文生图_2057083543095963650.json、图片生成/文生图/hidream o1 2604 文生图 提示词增强_2057018930434232322.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyHiDreamO1LatentImage`
- `HiDreamO1PatchSeamSmoothing`
- `JjkText`
- `KSampler`
- `ModelNoiseScale`
- `PrimitiveBoolean`
- `SaveImage`
- `VAEDecode`
- `easy ifElse`
- `easy int`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | - | 2 | 25% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.675 | - | 2 | 52% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.675，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
