---
name: unknown_workflow_upscale_lora_sampler_38
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.93
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1988616324257636353.json, 图片生成/文生图/千问（qwen）图片编辑+放大_1991788437487431681.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1988616324257636353.json、图片生成/文生图/千问（qwen）图片编辑+放大_1991788437487431681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 25% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1324 | - | 2 | 77% |
| 高度 | 2208 | - | 2 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1324，样本不足，未给区间，2 个样本
- 高度 中位数 2208，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
