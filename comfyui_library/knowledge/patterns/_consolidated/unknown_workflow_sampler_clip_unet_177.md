---
name: unknown_workflow_sampler_clip_unet_177
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.9765
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json, 图片生成/文生图/完美中文海报生成_2002018843826503681.json, 图片生成/文生图/文生图工作流购买的1 (1)_2045309169393209345.json, 图片生成/文生图/文生图工作流购买的1 (1)_2068998152438501378.json, 图片生成/文生图/文生图工作流购买的1_2047220596840341506.json, 图片生成/文生图/文生图工作流购买的1_2047619516003262466.json, 图片生成/文生图/文生图片工作流_2056608192112713729.json, 图片生成/文生图/超强文生图Z-image-base_2016185060738732034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_177

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json、图片生成/文生图/完美中文海报生成_2002018843826503681.json、图片生成/文生图/文生图工作流购买的1 (1)_2045309169393209345.json、图片生成/文生图/文生图工作流购买的1 (1)_2068998152438501378.json、图片生成/文生图/文生图工作流购买的1_2047220596840341506.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/8 个有
- `DoubaoSizePreset` —— 1/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `Image Filter Adjustments` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 8 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 8 | 20% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，8 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，8 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
