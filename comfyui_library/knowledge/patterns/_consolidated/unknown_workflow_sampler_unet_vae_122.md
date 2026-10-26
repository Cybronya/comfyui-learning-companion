---
name: unknown_workflow_sampler_unet_vae_122
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.892625
common_nodes: [CLIPLoader, ConditioningZeroOut, Flux2KleinEditTextEncode_EditUtils, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3d相机控制角度切换klein_2023012447916924929.json, 图片生成/图生图/cos后期美颜260616_2066692878470041601.json, 图片生成/图生图/klein9b-真实感洗图_2045696592337969153.json, 图片生成/图生图/klein9b-风格转绘工作流_2039186439677677570.json, 图片生成/图生图/产品精修翻新-klein9b_2067892313631842306.json, 图片生成/图生图/极致真实皮肤纹理-klein9b_2026599835666747393.json, 图片生成/图生图/涂鸦蜡笔画-klein_2032234206062977026.json, 图片生成/文生图/klein9b-图像转赛璐璐风格_2029151365393555458.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_122

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/3d相机控制角度切换klein_2023012447916924929.json、图片生成/图生图/cos后期美颜260616_2066692878470041601.json、图片生成/图生图/klein9b-真实感洗图_2045696592337969153.json、图片生成/图生图/klein9b-风格转绘工作流_2039186439677677570.json、图片生成/图生图/产品精修翻新-klein9b_2067892313631842306.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Flux2KleinEditTextEncode_EditUtils`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 7/8 个有
- `PIP_图像联结` —— 7/8 个有
- `EmptyLatentImage` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `JjkText` —— 4/8 个有
- `CR Simple Image Compare` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `PreviewAny` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `QwenMultiangleCameraNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |
| LoRA 模型强度 | 0.8 | 0.2 - 1 | 7 | 60% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 7 | 93% |
| 采样步数 | 4 | 2 - 8 | 8 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.2 - 1，7 个样本
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，7 个样本，取值集中（一致性 93%）
- 采样步数 中位数 4，观测区间 2 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
