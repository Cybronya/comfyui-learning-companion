---
name: unknown_workflow_lora_sampler_unet_47
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9612
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1957714879070437378.json, 图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1988873891172986882.json, 图片生成/图生图/Qwen FP8 图像风格一键转绘_2015764180116185090.json, 图片生成/图生图/Qwen 单图片多视角转换_1961711028679675905.json, 图片生成/图生图/Qwen-Edit白模转材质效果图_1985594354335199233.json, 图片生成/图生图/Qwen-image-Edit去除猫咪_1958036285367758849.json, 图片生成/图生图/Qwen-image-edit单图编辑_1958178171315240962.json, 图片生成/图生图/Qwen-image-edit图片编辑基础工作流_1958527856827645953.json, 图片生成/图生图/图片扩充-竖转横专用工作流（Qwen-edit）_1961234314279239681.json, 图片生成/文生图/Qwen 单张图片多角度视图视角转换_1976907729967190018.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1957714879070437378.json、图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1988873891172986882.json、图片生成/图生图/Qwen FP8 图像风格一键转绘_2015764180116185090.json、图片生成/图生图/Qwen 单图片多视角转换_1961711028679675905.json、图片生成/图生图/Qwen-Edit白模转材质效果图_1985594354335199233.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/10 个有
- `GetImageSize` —— 8/10 个有
- `ImageConcanate` —— 6/10 个有
- `ImageScaleToMegapixels` —— 6/10 个有
- `CLIPTextEncode` —— 2/10 个有
- `FluxKontextImageScale` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `CM_IntBinaryOperation` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `LayerUtility: ExtendCanvas` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `Text Multiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 10 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，10 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足
