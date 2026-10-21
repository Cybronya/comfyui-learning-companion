---
name: unknown_workflow_sampler_unet_vae_221
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.661
common_nodes: [CLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, KSampler, PreviewImage, ResizeImageMaskNode, ResolutionSelector, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【寄语秋歌】Qwen image-2.1 图片编辑工作流_2103294156843077634.json, 图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_221

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【寄语秋歌】Qwen image-2.1 图片编辑工作流_2103294156843077634.json、图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `PreviewImage`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `QwenImage21Cache` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 1 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
