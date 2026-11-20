---
name: unknown_workflow_sampler_checkpoint_vae_16
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.874667
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Pose-Control_2068695721599131650.json, 图片生成/图生图/双图编辑：Qwen-image-Edite-Remix-AIO-v2.0_2048992154864852994.json, 图片生成/图生图/姿势参考：Qwen-image-Edite-Remix-AIO-v2.0_2049410315644833794.json, 图片生成/图生图/局部重绘：Qwen-image-Edite-Remix-AIO-v2.0_2049400083560534017.json, 图片生成/图生图/扩图：Qwen-image-Edite-Remix-AIO-v2.0_2049034505599590401.json, 图片生成/图生图/拯救废片（扩图) Qwen-image-Edite-v2.0版_2054026261445521410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Pose-Control_2068695721599131650.json、图片生成/图生图/双图编辑：Qwen-image-Edite-Remix-AIO-v2.0_2048992154864852994.json、图片生成/图生图/姿势参考：Qwen-image-Edite-Remix-AIO-v2.0_2049410315644833794.json、图片生成/图生图/局部重绘：Qwen-image-Edite-Remix-AIO-v2.0_2049400083560534017.json、图片生成/图生图/扩图：Qwen-image-Edite-Remix-AIO-v2.0_2049034505599590401.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `ImagePadForOutpaint` —— 2/6 个有
- `SDPoseOODLoader` —— 2/6 个有
- `SDPoseOODProcessor` —— 2/6 个有
- `DrawMaskOnImage` —— 1/6 个有
- `LayerMask: MaskGrow` —— 1/6 个有
- `Mask Fill Holes` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 67% |
| 调度器 | beta | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 67%
- 调度器 最常用 beta，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
