---
name: unknown_workflow_lora_sampler_unet_145
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8942
common_nodes: [CLIPLoader, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit一句话P图工作流_1958949445201244162.json, 图片生成/图生图/Qwen_image_Edit千问图片编辑2509版_1970667844893614081.json, 图片生成/图生图/Qwen_image_Edit千问图片编辑2511版-双图_2003739271418814465.json, 图片生成/图生图/Qwen_图像外扩（扩图）_1970475614409007105.json, 图片生成/文生图/Qwen-2509-动作迁移，人物一致性，衣服场景随意换_1979932270746308610.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_145

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit一句话P图工作流_1958949445201244162.json、图片生成/图生图/Qwen_image_Edit千问图片编辑2509版_1970667844893614081.json、图片生成/图生图/Qwen_image_Edit千问图片编辑2511版-双图_2003739271418814465.json、图片生成/图生图/Qwen_图像外扩（扩图）_1970475614409007105.json、图片生成/文生图/Qwen-2509-动作迁移，人物一致性，衣服场景随意换_1979932270746308610.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/5 个有
- `ImageStitch` —— 4/5 个有
- `TextEncodeQwenImageEditPlus` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `TextEncodeQwenImageEdit` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `GetImageSize+` —— 2/5 个有
- `DWPreprocessor` —— 1/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerColor: ColorAdapter` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RMBG` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
