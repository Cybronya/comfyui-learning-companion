---
name: unknown_workflow_sampler_unet_vae_161
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.899167
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein-9B-人物场景迁移升级版_2019038881462624257.json, 图片生成/图生图/Flux2-Klein-9B-动作迁移（升级版）_2019758694229086210.json, 图片生成/图生图/Klein-9B-人像打光_2060940192906833921.json, 图片生成/图生图/Klein-9B-单图编辑+一致性增加lora_2036060642293063681.json, 图片生成/图生图/Klein-9B-图像人物三视图生成_2020033275313524737.json, 图片生成/图生图/Klein-9B-多人动作迁移_2058188256558272513.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_161

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-9B-人物场景迁移升级版_2019038881462624257.json、图片生成/图生图/Flux2-Klein-9B-动作迁移（升级版）_2019758694229086210.json、图片生成/图生图/Klein-9B-人像打光_2060940192906833921.json、图片生成/图生图/Klein-9B-单图编辑+一致性增加lora_2036060642293063681.json、图片生成/图生图/Klein-9B-图像人物三视图生成_2020033275313524737.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `YC Color Match` —— 4/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `BBoxYOLO` —— 1/6 个有
- `BodyRatioMapperSDPoseRender` —— 1/6 个有
- `CheckpointLoaderSimple` —— 1/6 个有
- `DWPreprocessor` —— 1/6 个有
- `SDPoseKeypointExtractor` —— 1/6 个有
- `YOLOModelLoader` —— 1/6 个有
- `easy imageRemBg` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
