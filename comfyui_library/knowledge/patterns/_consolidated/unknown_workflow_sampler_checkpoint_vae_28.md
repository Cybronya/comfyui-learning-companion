---
name: unknown_workflow_sampler_checkpoint_vae_28
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.507
common_nodes: [CLIPLoader, CR Prompt Text, CheckpointLoaderSimple, ConditioningZeroOut, CropWithPadInfo, GetNode, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen1-3工作流_2029594780891619330.json, 图片生成/图生图/qwen编辑_2060049031971295233.json, 图片生成/图生图/史上最强改图→换头_换脸_换装_换姿势_高清放大_去水印_多姿势多视角_老照片修复_局部重绘_证件照_2010176186307055617.json, 图片生成/图生图/洗图控图改图（换头_换脸_换装_换姿势_高清放大_去水印_多姿势多视角）_2099877234684284930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_28

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen1-3工作流_2029594780891619330.json、图片生成/图生图/qwen编辑_2060049031971295233.json、图片生成/图生图/史上最强改图→换头_换脸_换装_换姿势_高清放大_去水印_多姿势多视角_老照片修复_局部重绘_证件照_2010176186307055617.json、图片生成/图生图/洗图控图改图（换头_换脸_换装_换姿势_高清放大_去水印_多姿势多视角）_2099877234684284930.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `GetNode`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `DuckQREncodeNode` —— 1/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（10/4 个样本）：Steps较低可能导致细节不足
