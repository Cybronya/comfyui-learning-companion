---
name: unknown_workflow_lora_sampler_unet_133
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7694
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/18A_2035893292444950529.json, 图片生成/图生图/39.tonnie-Qwen edit最正确的用法（加一致性lora）_2004243538080657409.json, 图片生成/图生图/42.tonnie-Qwen Edit Plus图像编辑升级版（换装换姿势）_2004274214813270018.json, 图片生成/图生图/54.tonnie-2509+eigen 全能图片V1（改风格效果不好）_2007964677136982018.json, 图片生成/图生图/万能图片去水印 右键选择打开遮罩编辑器选择需要去除水印+全节点注释_2055170365499944962.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_133

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/18A_2035893292444950529.json、图片生成/图生图/39.tonnie-Qwen edit最正确的用法（加一致性lora）_2004243538080657409.json、图片生成/图生图/42.tonnie-Qwen Edit Plus图像编辑升级版（换装换姿势）_2004274214813270018.json、图片生成/图生图/54.tonnie-2509+eigen 全能图片V1（改风格效果不好）_2007964677136982018.json、图片生成/图生图/万能图片去水印 右键选择打开遮罩编辑器选择需要去除水印+全节点注释_2055170365499944962.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `PreviewImage` —— 2/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `DrawMaskOnImage` —— 1/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `MaskBlur+` —— 1/5 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
