---
name: unknown_workflow_lora_sampler_unet_45
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.906727
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/39.tonnie-Qwen edit最正确的用法（加一致性lora）_2004243538080657409.json, 图片生成/图生图/42.tonnie-Qwen Edit Plus图像编辑升级版（换装换姿势）_2004274214813270018.json, 图片生成/图生图/54.tonnie-2509+eigen 全能图片V1（改风格效果不好）_2007964677136982018.json, 图片生成/图生图/Nunchaku-Pose姿势参考-千问Edit2509图像编辑_1971205875295830018.json, 图片生成/图生图/Nunchaku-人物首尾帧制作-Edit2509图像编辑_1971207824632168449.json, 图片生成/图生图/Nunchaku-人物首尾帧制作-Edit2509图像编辑_1971210529568149505.json, 图片生成/图生图/Nunchaku-证件照-Edit2509图像编辑_1971199922907336705.json, 图片生成/图生图/Pose姿势参考-千问Edit2509图像编辑_1970828887754186753.json, 图片生成/图生图/Pose姿势参考-千问Edit2509图像编辑_1971040326016212994.json, 图片生成/图生图/文字渲染-千问Edit2509图像编辑_1970532850070134786.json, 图片生成/图生图/雪4.tonnie-edit 2509-aux改变姿态_2002562915486035970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_45

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/39.tonnie-Qwen edit最正确的用法（加一致性lora）_2004243538080657409.json、图片生成/图生图/42.tonnie-Qwen Edit Plus图像编辑升级版（换装换姿势）_2004274214813270018.json、图片生成/图生图/54.tonnie-2509+eigen 全能图片V1（改风格效果不好）_2007964677136982018.json、图片生成/图生图/Nunchaku-Pose姿势参考-千问Edit2509图像编辑_1971205875295830018.json、图片生成/图生图/Nunchaku-人物首尾帧制作-Edit2509图像编辑_1971207824632168449.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 10/11 个有
- `ImageStitch` —— 7/11 个有
- `Text Multiline` —— 7/11 个有
- `AIO_Preprocessor` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `CFGNorm` —— 4/11 个有
- `ModelSamplingAuraFlow` —— 4/11 个有
- `NunchakuQwenImageDiTLoader` —— 4/11 个有
- `ImageConcatMulti` —— 2/11 个有
- `EmptyLatentImage` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 11 | 64% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 11 | 63% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta57 | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta57，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
