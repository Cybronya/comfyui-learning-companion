---
name: unknown_workflow_lora_sampler_clip_120
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8505
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSampler, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1968745066112143361.json, 图片生成/文生图/极速4步采样生图——SoilsihgStudio_1895380500704002050.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1968745066112143361.json、图片生成/文生图/极速4步采样生图——SoilsihgStudio_1895380500704002050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | - | 2 | 18% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
