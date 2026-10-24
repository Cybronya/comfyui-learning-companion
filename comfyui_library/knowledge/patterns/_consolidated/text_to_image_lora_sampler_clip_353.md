---
name: text_to_image_lora_sampler_clip_353
type: Text To Image
frequency: 5
level: strong
coverage: 0.8986
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2klein去除主体教程｜照片多余路人杂物一键消失_2103731555385569281.json, 图片生成/图生图/flux2klein去除卡片利器｜图片多余元素一键抹干净_2103710390667538433.json, 图片生成/图生图/flux2klein添加主体工具｜往照片里加人加物毫无违和感_2103708896031498241.json, 图片生成/图生图/flux_klien3图像编辑，电商平面设计图生图_2111557914212257793.json, 图片生成/图生图/单图编辑FLUX3-Klein in 加速，电商图生图提速_2111607229198721025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_353

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux2klein去除主体教程｜照片多余路人杂物一键消失_2103731555385569281.json、图片生成/图生图/flux2klein去除卡片利器｜图片多余元素一键抹干净_2103710390667538433.json、图片生成/图生图/flux2klein添加主体工具｜往照片里加人加物毫无违和感_2103708896031498241.json、图片生成/图生图/flux_klien3图像编辑，电商平面设计图生图_2111557914212257793.json、图片生成/图生图/单图编辑FLUX3-Klein in 加速，电商图生图提速_2111607229198721025.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `Flux2Scheduler` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageToMask` —— 2/5 个有
- `ManualSigmas` —— 2/5 个有
- `PixaromaInpaintCrop` —— 2/5 个有
- `PixaromaUncrop` —— 2/5 个有
- `ImageConcanate` —— 1/5 个有
- `PDIMAGE_LongerSize` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ReferenceMultiLatent` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
