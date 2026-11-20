---
name: unknown_workflow_upscale_lora_sampler_20
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.895167
common_nodes: [CLIPLoader, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【糖画】【通用】Qwen-Image-Edit 图生图_2030851176635310082.json, 图片生成/图生图/千问多图编辑工作流_2005899370761515009.json, 图片生成/图生图/千问编辑模型plus工作流_2009538104188739585.json, 图片生成/图生图/图像编辑-电商专用Qwenedit_2074079359077535746.json, 图片生成/图生图/最强Qwen-image图片编辑工作流_2097570896465719298.json, 图片生成/图生图/最新版千问图片编辑（支持多图参考）_1981575735313874946.json, 图片生成/文生图/千问Qwen-edit编辑模型工作流_1988616324257636353.json, 图片生成/文生图/千问（qwen）图片编辑+放大_1991788437487431681.json, 平台全量/Qwen-edit 实现AI模特换装暨场景和角色动作控制-ComfyUI工作流_2022514668153081857.json, 平台全量/Qwen千问图片编辑工作流PLUS（Qwen-edit-plus）_1994656083052535809.json, 平台全量/工作流千问篇4-Qwen千问图像编辑模型-特别强强强_2022222471033790465.json, 数字人/数字人/千问编辑模型-田_2014545397749911554.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/【糖画】【通用】Qwen-Image-Edit 图生图_2030851176635310082.json、图片生成/图生图/千问多图编辑工作流_2005899370761515009.json、图片生成/图生图/千问编辑模型plus工作流_2009538104188739585.json、图片生成/图生图/图像编辑-电商专用Qwenedit_2074079359077535746.json、图片生成/图生图/最强Qwen-image图片编辑工作流_2097570896465719298.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 11/12 个有
- `EmptyLatentImage` —— 11/12 个有
- `Image Comparer (rgthree)` —— 11/12 个有
- `PreviewImage` —— 6/12 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 6/12 个有
- `CFGNorm` —— 5/12 个有
- `FluxKontextImageScale` —— 5/12 个有
- `TextEncodeQwenImageEditPlus` —— 5/12 个有
- `UnetLoaderGGUF` —— 5/12 个有
- `CR Text` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `PainterQwenImageEditPlus` —— 1/12 个有
- `easy positive` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 35 | 12 | 8% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler_ancestral | - | 12 | 67% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1624 | 896 - 2048 | 11 | 74% |
| 高度 | 1536 | 1080 - 2880 | 11 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 35，12 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1624，观测区间 896 - 2048，11 个样本
- 高度 中位数 1536，观测区间 1080 - 2880，11 个样本
- 高发问题（10/12 个样本）：Steps较低可能导致细节不足
