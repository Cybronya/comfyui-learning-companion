---
name: unknown_workflow_lora_sampler_clip_319
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.935
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CreateVideo, Fast Groups Muter (rgthree), GetVideoComponents, KSampler, LoadImage, LoadVideo, ModelSamplingSD3, Power Lora Loader (rgthree), PreviewImage, SaveVideo, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, WanVaceToVideo, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_1928466472526553089.json, 视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_2067499478541750274.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_319

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_1928466472526553089.json、视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_2067499478541750274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
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
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
