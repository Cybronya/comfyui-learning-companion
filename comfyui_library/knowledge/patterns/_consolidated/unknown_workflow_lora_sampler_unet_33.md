---
name: unknown_workflow_lora_sampler_unet_33
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.869462
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Image_Edit_2511图像编辑工作流_2021566239163817986.json, 图片生成/图生图/Qwen千问图像编辑工作流【加速 LoRA 提速版】：原版)_2024150471530778626.json, 图片生成/图生图/Qwen千问图像编辑工作流【加速 LoRA 提速版】：原版qwen_image_edit_2509_1986636154382516225.json, 图片生成/图生图/Qwen千问图像编辑工作流【加速 LoRA 提速版】：原版qwen_image_edit_2509_2002996055396478977.json, 图片生成/图生图/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_2012389576106582017.json, 图片生成/图生图/qwen 2511 单图编辑_2005278089867395074.json, 图片生成/图生图/qwen+image+2511双图编辑工作流_2016859064726200321.json, 图片生成/图生图/qwen-图像编辑_2079860798289170433.json, 图片生成/图生图/千问Qwen图生图 edit工作流基础款_1991849542488485889.json, 图片生成/图生图/千问图片编辑工作流_1980251429120225281.json, 图片生成/图生图/千问图片编辑教学_2009529082400215042.json, 图片生成/图生图/千问多功能工作流_1989535712292818946.json, 图片生成/图生图/最新qwen image2511双图编辑工作流_2013222102685454337.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_33

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen_Image_Edit_2511图像编辑工作流_2021566239163817986.json、图片生成/图生图/Qwen千问图像编辑工作流【加速 LoRA 提速版】：原版)_2024150471530778626.json、图片生成/图生图/Qwen千问图像编辑工作流【加速 LoRA 提速版】：原版qwen_image_edit_2509_1986636154382516225.json、图片生成/图生图/Qwen千问图像编辑工作流【加速 LoRA 提速版】：原版qwen_image_edit_2509_2002996055396478977.json、图片生成/图生图/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_2012389576106582017.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/13 个有
- `EmptyLatentImage` —— 12/13 个有
- `FluxKontextImageScale` —— 11/13 个有
- `ImageUpscaleWithModel` —— 11/13 个有
- `PreviewImage` —— 11/13 个有
- `UpscaleModelLoader` —— 11/13 个有
- `CFGNorm` —— 9/13 个有
- `TextEncodeQwenImageEditPlus` —— 9/13 个有
- `Image Comparer (rgthree)` —— 8/13 个有
- `CR Text` —— 5/13 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 5/13 个有
- `FluxResolutionNode` —— 3/13 个有
- `ImageConcanate` —— 3/13 个有
- `DWPreprocessor` —— 1/13 个有
- `ImageResize+` —— 1/13 个有
- `ModelSamplingAuraFlow` —— 1/13 个有
- `UnetLoaderGGUF` —— 1/13 个有
- `easy imageSave` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1560 | 12 | 66% |
| 高度 | 1536 | 512 - 1536 | 12 | 61% |
| 采样步数 | 8 | 4 - 15 | 13 | 64% |
| Prompt 约束强度(CFG) | 1 | 0.6 - 1 | 13 | 89% |
| 采样算法 | euler_ancestral | - | 13 | 62% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1560，12 个样本
- 高度 中位数 1536，观测区间 512 - 1536，12 个样本
- 采样步数 中位数 8，观测区间 4 - 15，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.6 - 1，13 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler_ancestral，13 个样本，一致性 62%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.6，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
