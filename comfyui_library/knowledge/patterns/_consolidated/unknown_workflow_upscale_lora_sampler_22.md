---
name: unknown_workflow_upscale_lora_sampler_22
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.907111
common_nodes: [CLIPLoader, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【糖画】【通用】Qwen-Image-Edit 图生图_2030851176635310082.json, 图片生成/图生图/千问多图编辑工作流_2005899370761515009.json, 图片生成/图生图/千问编辑模型plus工作流_2009538104188739585.json, 图片生成/图生图/图像编辑-电商专用Qwenedit_2074079359077535746.json, 图片生成/图生图/最强Qwen-image图片编辑工作流_2097570896465719298.json, 图片生成/图生图/最新版千问图片编辑（支持多图参考）_1981575735313874946.json, 图片生成/文生图/千问Qwen-edit编辑模型工作流_1988616324257636353.json, 图片生成/文生图/千问（qwen）图片编辑+放大_1991788437487431681.json, 数字人/数字人/千问编辑模型-田_2014545397749911554.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/【糖画】【通用】Qwen-Image-Edit 图生图_2030851176635310082.json、图片生成/图生图/千问多图编辑工作流_2005899370761515009.json、图片生成/图生图/千问编辑模型plus工作流_2009538104188739585.json、图片生成/图生图/图像编辑-电商专用Qwenedit_2074079359077535746.json、图片生成/图生图/最强Qwen-image图片编辑工作流_2097570896465719298.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `EmptyLatentImage` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 5/9 个有
- `PreviewImage` —— 4/9 个有
- `UnetLoaderGGUF` —— 4/9 个有
- `CFGNorm` —— 3/9 个有
- `FluxKontextImageScale` —— 3/9 个有
- `TextEncodeQwenImageEditPlus` —— 3/9 个有
- `CR Text` —— 1/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `PainterQwenImageEditPlus` —— 1/9 个有
- `easy positive` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 35 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler_ancestral | - | 9 | 67% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1804 | 896 - 2048 | 8 | 73% |
| 高度 | 1536 | 1080 - 2880 | 8 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 35，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1804，观测区间 896 - 2048，8 个样本
- 高度 中位数 1536，观测区间 1080 - 2880，8 个样本
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
