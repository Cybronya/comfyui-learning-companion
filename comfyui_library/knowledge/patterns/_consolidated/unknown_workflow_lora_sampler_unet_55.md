---
name: unknown_workflow_lora_sampler_unet_55
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.964727
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1957714879070437378.json, 图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1988873891172986882.json, 图片生成/图生图/Qwen FP8 图像风格一键转绘_2015764180116185090.json, 图片生成/图生图/Qwen 单图片多视角转换_1961711028679675905.json, 图片生成/图生图/Qwen-Edit白模转材质效果图_1985594354335199233.json, 图片生成/图生图/Qwen-image-Edit去除猫咪_1958036285367758849.json, 图片生成/图生图/Qwen-image-edit单图编辑_1958178171315240962.json, 图片生成/图生图/Qwen-image-edit图片编辑基础工作流_1958527856827645953.json, 图片生成/图生图/图片扩充-竖转横专用工作流（Qwen-edit）_1961234314279239681.json, 图片生成/文生图/Qwen 单张图片多角度视图视角转换_1976907729967190018.json, 平台全量/千问图像编辑工具_Qwen-image-edit_原版工作流_1966256780827422721.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_55

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1957714879070437378.json、图片生成/图生图/Aiwood-Qwen-image-edit基础工作流_1988873891172986882.json、图片生成/图生图/Qwen FP8 图像风格一键转绘_2015764180116185090.json、图片生成/图生图/Qwen 单图片多视角转换_1961711028679675905.json、图片生成/图生图/Qwen-Edit白模转材质效果图_1985594354335199233.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 9/11 个有
- `GetImageSize` —— 9/11 个有
- `ImageConcanate` —— 7/11 个有
- `ImageScaleToMegapixels` —— 7/11 个有
- `CLIPTextEncode` —— 2/11 个有
- `FluxKontextImageScale` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `CM_IntBinaryOperation` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `LayerUtility: ExtendCanvas` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 11 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 32% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，11 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
