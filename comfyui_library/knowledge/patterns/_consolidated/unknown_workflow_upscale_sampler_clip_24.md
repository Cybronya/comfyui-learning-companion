---
name: unknown_workflow_upscale_sampler_clip_24
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-imagebase蛋挞Lora+放大_2026169943431057410.json, 图片生成/文生图/一键超多图（Z-image）_2005259720401317890.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-imagebase蛋挞Lora+放大_2026169943431057410.json、图片生成/文生图/一键超多图（Z-image）_2005259720401317890.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Load Image Batch` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `NunchakuZImageDiTLoader` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | - | 2 | 28% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，样本不足，未给区间，2 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
