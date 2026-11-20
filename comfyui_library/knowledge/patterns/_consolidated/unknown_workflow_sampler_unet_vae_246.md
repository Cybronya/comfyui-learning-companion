---
name: unknown_workflow_sampler_unet_vae_246
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.724
common_nodes: [CLIPLoader, ImageConcanate, KSampler, LoadImage, PainterFluxImageEdit, SaveImage, SolidMask, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux 2 Klein换头换脸_2017519628590784513.json, 图片生成/图生图/Flux2-Klein+极速换脸_2012141005570580481.json, 图片生成/图生图/Klein换图工作流_2021372321809829890.json, 图片生成/图生图/一键换头（无需多余操作）_2050550897880645634.json, 平台全量/高质量一键换脸--Flux 2 Klein_2025192120537059329.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_246

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux 2 Klein换头换脸_2017519628590784513.json、图片生成/图生图/Flux2-Klein+极速换脸_2012141005570580481.json、图片生成/图生图/Klein换图工作流_2021372321809829890.json、图片生成/图生图/一键换头（无需多余操作）_2050550897880645634.json、平台全量/高质量一键换脸--Flux 2 Klein_2025192120537059329.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `PainterFluxImageEdit`
- `SaveImage`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy imageRemBg` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `DapaoImageAspectRatioResizeNode` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `MaskPreview+` —— 2/5 个有
- `AutoCropFaces` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `JWStringMultiline` —— 1/5 个有
- `SDVN RGBA to RGB` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
