---
name: unknown_workflow_upscale_lora_sampler_33
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.661333
common_nodes: [CLIPLoader, ConditioningZeroOut, Fast Groups Muter (rgthree), GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy loraStack, easy loraStackApply]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 klein 产品改色工作流_2053122385259311106.json, 图片生成/图生图/Flux2 klein 建筑图稿转设计图工作流_2053478078432722946.json, 图片生成/图生图/Flux2 klein 老照片高清修复工作流_2053482390542143489.json, 图片生成/图生图/Flux2 klein 设计线稿图转实物_2058728637213536257.json, 图片生成/图生图/Flux2klein设计线稿图转实物_2063617771497410562.json, 图片生成/图生图/超好用🔥建筑图稿线稿转设计图-描述词参数可按需调整_2054847570601627650.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2 klein 产品改色工作流_2053122385259311106.json、图片生成/图生图/Flux2 klein 建筑图稿转设计图工作流_2053478078432722946.json、图片生成/图生图/Flux2 klein 老照片高清修复工作流_2053482390542143489.json、图片生成/图生图/Flux2 klein 设计线稿图转实物_2058728637213536257.json、图片生成/图生图/Flux2klein设计线稿图转实物_2063617771497410562.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy loraStack`
- `easy loraStackApply`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `CR Text Concatenate` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
