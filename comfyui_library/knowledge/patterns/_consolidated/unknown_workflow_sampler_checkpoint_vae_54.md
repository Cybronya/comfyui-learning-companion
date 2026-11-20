---
name: unknown_workflow_sampler_checkpoint_vae_54
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8065
common_nodes: [CFGNorm, CLIPLoader, CheckpointLoaderSimple, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), Image Save, ImageScaleToTotalPixels, KSampler, Label (rgthree), LoadImage, ModelSamplingAuraFlow, NuiKr.OpenPoseEditor, PreviewImage, SaveImage, ShowText|pysssss, Switch any [Crystools], Text Concatenate, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, easy boolean, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit Aio 模特换动作姿势 自定义3D pose+参考姿态图 2合1 图像编辑工作流_2062778723623067649.json, 平台全量/Qwen Edit Aio 模特换动作姿势 自定义3D pose 多人姿态任意组合  图像编辑工作流_2062780608010608641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_54

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Edit Aio 模特换动作姿势 自定义3D pose+参考姿态图 2合1 图像编辑工作流_2062778723623067649.json、平台全量/Qwen Edit Aio 模特换动作姿势 自定义3D pose 多人姿态任意组合  图像编辑工作流_2062780608010608641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `Image Save`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NuiKr.OpenPoseEditor`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `Switch any [Crystools]`
- `Text Concatenate`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `easy boolean`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `YOLOModelLoader` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
