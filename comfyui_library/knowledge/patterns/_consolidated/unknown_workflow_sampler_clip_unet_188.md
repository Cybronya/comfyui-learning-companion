---
name: unknown_workflow_sampler_clip_unet_188
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.89475
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, PrimitiveStringMultiline, ReferenceMultiLatent, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】flux3 image 图生图和图片参考_2111309354984108033.json, 图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2114589396241575937.json, 图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2115296729280110593.json, 图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2115305648924745730.json, 图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2115625037553295361.json, 图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2115670896622006274.json, 图片生成/图生图/千府AI-flux3_klein线稿转效果图工作流_2112069097197490178.json, 图片生成/图生图/千府AI-flux3_klein线稿转效果图工作流_2114885151695130625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_188

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/【遇见AI】flux3 image 图生图和图片参考_2111309354984108033.json、图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2114589396241575937.json、图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2115296729280110593.json、图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2115305648924745730.json、图片生成/图生图/千府AI-KLEIN3建筑立面迁移工作流_2115625037553295361.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ReferenceMultiLatent`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `ImageConcanate` —— 7/8 个有
- `图像缩放V2_孤海` —— 7/8 个有
- `AIO_Preprocessor` —— 5/8 个有
- `Text Multiline` —— 5/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `ShunjingAIShade` —— 2/8 个有
- `ShowText|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 16 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 16，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
