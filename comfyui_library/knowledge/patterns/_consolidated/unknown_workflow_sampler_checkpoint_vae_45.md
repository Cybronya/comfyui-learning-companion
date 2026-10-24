---
name: unknown_workflow_sampler_checkpoint_vae_45
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.912
common_nodes: [CR Text, CheckpointLoaderSimple, EmptyLatentImage, Fast Bypasser (rgthree), ImageConcanate, ImageConcatMulti, ImageScaleToTotalPixels, ImpactSwitch, KSampler, LoadImage, ModelSamplingAuraFlow, Mute / Bypass Repeater (rgthree), SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Remix-AIO-批图_2045570507235397633.json, 图片生成/图生图/🥯千问Edit-Rapid-AIO-v5 金总补习班优化版🥯_1979349762338099202.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-Remix-AIO-批图_2045570507235397633.json、图片生成/图生图/🥯千问Edit-Rapid-AIO-v5 金总补习班优化版🥯_1979349762338099202.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `ImpactSwitch`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `Mute / Bypass Repeater (rgthree)`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DF_Float` —— 1/2 个有
- `FluxResolutionNode` —— 1/2 个有
- `HAIGC_LoadImagesFromZip` —— 1/2 个有
- `HAIGC_SaveImagesToZip` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `TT_img_enc` —— 1/2 个有
- `easy imageScaleDownBy` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 796 | - | 2 | 64% |
| 高度 | 976 | - | 2 | 52% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 796，样本不足，未给区间，2 个样本
- 高度 中位数 976，样本不足，未给区间，2 个样本
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
