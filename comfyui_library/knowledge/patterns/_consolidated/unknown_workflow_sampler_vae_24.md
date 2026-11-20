---
name: unknown_workflow_sampler_vae_24
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.790714
common_nodes: [AIO_Preprocessor, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit AIO 合集 - 编辑 换装 姿势迁移_2004099741057228801.json, 图片生成/图生图/Qwen-Edit-AIO合集。单图编辑，双图姿势控制，双图换装模式，不亏的AI合集！_2033383964844498945.json, 图片生成/图生图/Qwen-Edit-AIO合集。单图编辑，双图姿势控制，双图换装模式，不亏的AI合集！_2042057196292284418.json, 图片生成/图生图/Qwen-Edit-AIO合集（单图+姿势迁移+人物换装）_2044245209885708289.json, 图片生成/图生图/Qwen-Edit-AIO图像编辑合集_2047854197747486722.json, 图片生成/图生图/Work-Fisher Qwen-Edit-AIO合集_1976167606266806273.json, 图片生成/图生图/Work-Fisher+Qwen-Edit-AIO合集_2021114801375678465.json, 图片生成/图生图/一键换衣_1958237827177857026.json, 图片生成/图生图/动作迁移-电商换装-服装换色 -111_2084616605148991490.json, 图片生成/图生图/动作迁移-电商换装-服装换色_2044005288033914882.json, 图片生成/图生图/单图编辑_姿势迁移_人物换装，三流合一 Qwen V3  All In One模型_2060420022639611906.json, 图片生成/图生图/姿势迁移-2_2082317151964323841.json, 平台全量/Qwen-Edit-AIO三种做图合集_2056663898308308994.json, 平台全量/QwenEdit-AIO_1976928310624178178.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen Edit AIO 合集 - 编辑 换装 姿势迁移_2004099741057228801.json、图片生成/图生图/Qwen-Edit-AIO合集。单图编辑，双图姿势控制，双图换装模式，不亏的AI合集！_2033383964844498945.json、图片生成/图生图/Qwen-Edit-AIO合集。单图编辑，双图姿势控制，双图换装模式，不亏的AI合集！_2042057196292284418.json、图片生成/图生图/Qwen-Edit-AIO合集（单图+姿势迁移+人物换装）_2044245209885708289.json、图片生成/图生图/Qwen-Edit-AIO图像编辑合集_2047854197747486722.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 14 个 workflow 都包含：
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 13/14 个有
- `Image Comparer (rgthree)` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `PreviewImage` —— 13/14 个有
- `Fast Groups Bypasser (rgthree)` —— 12/14 个有
- `ImageColorMatch+` —— 12/14 个有
- `LayerUtility: ImageReel` —— 12/14 个有
- `LayerUtility: ImageReelComposit` —— 12/14 个有
- `ImageConcanate` —— 10/14 个有
- `CR Text` —— 2/14 个有
- `GetNode` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `EmptyImage` —— 1/14 个有
- `LayerUtility: GetImageSize` —— 1/14 个有
- `LayerUtility: ImageBlend` —— 1/14 个有
- `RHHiddenNodes` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | sa_solver | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 14 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 40/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，14 个样本，取值集中（一致性 95%）
- 高发问题（40/14 个样本）：Steps较低可能导致细节不足
