---
name: text_to_image_lora_sampler_clip_373
type: Text To Image
frequency: 5
level: strong
coverage: 0.886
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein 9B一键提取服装白底图，图生图电商服装抠图工具_2103984244711313410.json, 图片生成/图生图/Flux2 Klein去除卡片工作流，图生图精准移除图片中卡片元素工具_2103909515577094145.json, 图片生成/图生图/flux2klein去除主体教程｜照片多余路人杂物一键消失_2103731555385569281.json, 图片生成/图生图/flux2klein去除卡片利器｜图片多余元素一键抹干净_2103710390667538433.json, 图片生成/图生图/flux2klein添加主体工具｜往照片里加人加物毫无违和感_2103708896031498241.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_373

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 9B一键提取服装白底图，图生图电商服装抠图工具_2103984244711313410.json、图片生成/图生图/Flux2 Klein去除卡片工作流，图生图精准移除图片中卡片元素工具_2103909515577094145.json、图片生成/图生图/flux2klein去除主体教程｜照片多余路人杂物一键消失_2103731555385569281.json、图片生成/图生图/flux2klein去除卡片利器｜图片多余元素一键抹干净_2103710390667538433.json、图片生成/图生图/flux2klein添加主体工具｜往照片里加人加物毫无违和感_2103708896031498241.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageToMask` —— 2/5 个有
- `PixaromaInpaintCrop` —— 2/5 个有
- `PixaromaUncrop` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `AILab_ImageResize` —— 1/5 个有
- `CFGGuider` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `Qwen3VL_Chat` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
