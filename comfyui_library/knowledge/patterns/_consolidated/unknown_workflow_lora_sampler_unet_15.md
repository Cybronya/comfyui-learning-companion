---
name: unknown_workflow_lora_sampler_unet_15
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.914286
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AIGC特异点-最强抠图王_2045408571206148098.json, 图片生成/图生图/FLUX.2-klein 溶图打光（不偏移）_2046538388777476098.json, 图片生成/图生图/Flux-Klein-2 简约产品线稿图_2078260005668745217.json, 图片生成/图生图/Flux-Klein-2_简约产品线稿图_2079018113915506690.json, 图片生成/图生图/Flux-Klein-2_简约产品线稿图_2079401194891603969.json, 图片生成/图生图/Klein 9B一键光影重塑 专用LoRA_2043929620445143042.json, 图片生成/图生图/Klein 9B一键生成光影重塑 专用LoRA图生图_2053428960138145794.json, 图片生成/图生图/Klein 9B一键生成光影重塑 专用LoRA图生图_2054154663674564610.json, 图片生成/图生图/Klein 9B一键生成光影重塑 专用LoRA图生图_2101259024669962242.json, 图片生成/图生图/Klein 9B一键生成光影重塑 专用LoRA图生图_2101302359610712065.json, 图片生成/图生图/Klein 9B一键生成光影重塑 专用LoRA图生图_2107761228495024130.json, 图片生成/图生图/Klein 9B一键生成光影重塑 专用LoRA图生图_2107778250016641025.json, 图片生成/图生图/Klein 9B一键细节修复加笔触废土LoRA图生图-高级灰_2067887283566637058.json, 图片生成/图生图/Klein_9B一键光影重塑_专用LoRA_2062420907284590594.json, 图片生成/图生图/Klein_9B一键光影重塑_专用LoRA_2090074598116257793.json, 图片生成/图生图/Klein_9B一键光影重塑_专用LoRA_2096805023417196545.json, 图片生成/图生图/Klein_9B一键光影重塑_专用LoRA_2097150277370605569.json, 图片生成/图生图/Klein_9B一键溶图测试_2099506244464758785.json, 图片生成/图生图/Klein_光影重塑_2087365058488791041.json, 图片生成/图生图/Qwen_抠图王中王_2025655984181485569.json, 图片生成/图生图/抠图1_2044610260324847617.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_15

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/AIGC特异点-最强抠图王_2045408571206148098.json、图片生成/图生图/FLUX.2-klein 溶图打光（不偏移）_2046538388777476098.json、图片生成/图生图/Flux-Klein-2 简约产品线稿图_2078260005668745217.json、图片生成/图生图/Flux-Klein-2_简约产品线稿图_2079018113915506690.json、图片生成/图生图/Flux-Klein-2_简约产品线稿图_2079401194891603969.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PainterFluxImageEdit` —— 19/21 个有
- `GetImageSize+` —— 16/21 个有
- `ResizeImagesByLongerEdge` —— 16/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/21 个有
- `GrowMask` —— 3/21 个有
- `ImageToMask` —— 3/21 个有
- `LayerUtility: ImageCombineAlpha` —— 3/21 个有
- `easy int` —— 3/21 个有
- `ConditioningZeroOut` —— 2/21 个有
- `Easy_QwenEdit2509` —— 2/21 个有
- `Seed (rgthree)` —— 2/21 个有
- `TextInputNode` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 8 | 21 | 86% |
| Prompt 约束强度(CFG) | 0.7 | 0.5 - 1 | 21 | 82% |
| 采样算法 | euler | - | 21 | 95% |
| 调度器 | simple | - | 21 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 8，21 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 0.7，观测区间 0.5 - 1，21 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，21 个样本，一致性 95%
- 调度器 最常用 simple，21 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.5，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（21/21 个样本）：Steps较低可能导致细节不足
