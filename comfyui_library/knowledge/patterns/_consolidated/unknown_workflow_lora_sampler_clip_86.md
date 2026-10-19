---
name: unknown_workflow_lora_sampler_clip_86
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.919
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CreateVideo, Fast Groups Muter (rgthree), GetVideoComponents, KSampler, LoadImage, LoadVideo, ModelSamplingSD3, Power Lora Loader (rgthree), PreviewImage, SaveVideo, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, WanVaceToVideo, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: [easy imageColorMatch, Power Lora Loader (rgthree)]
members: [视频生成/图生视频/1928466472526553089.json, 视频生成/文生视频/1928466472526553089.json, 视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_2067499478541750274.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1928466472526553089.json、视频生成/文生视频/1928466472526553089.json、视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_2067499478541750274.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `Fast Groups Muter (rgthree)`
- `GetVideoComponents`
- `KSampler`
- `LoadImage`
- `LoadVideo`
- `ModelSamplingSD3`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `SaveVideo`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `WanVaceToVideo`
- `easy imageColorMatch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageColorMatch、Power Lora Loader (rgthree)
