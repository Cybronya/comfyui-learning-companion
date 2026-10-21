---
name: unknown_workflow_sampler_clip_unet_240
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.88
common_nodes: [CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶Z-image文生图工作流整合_2036799699528720385.json, 图片生成/文生图/▶千问Qwen2512生图工作流(整合)_2036799795003662338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_240

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/▶Z-image文生图工作流整合_2036799699528720385.json、图片生成/文生图/▶千问Qwen2512生图工作流(整合)_2036799795003662338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
