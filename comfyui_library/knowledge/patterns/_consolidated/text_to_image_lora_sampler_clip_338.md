---
name: text_to_image_lora_sampler_clip_338
type: Text To Image
frequency: 5
level: strong
coverage: 0.8836
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX3加速版图像编辑写真级｜上传图就改不动手修_2111338389898354689.json, 图片生成/图生图/Flux-3-Image-Klein多图编辑，图生图素材整合利器_2111560906680393729.json, 图片生成/图生图/Flux2 Klein去除卡片工作流，图生图精准移除图片中卡片元素工具_2103909515577094145.json, 图片生成/图生图/Flux2-Klein智能扩图｜图片外补全图生图工作流_2093112866625900545.json, 图片生成/图生图/flux-2-klein-9b去文字利器｜图生图轻松抹除画面文字_2105226424310394881.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_338

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX3加速版图像编辑写真级｜上传图就改不动手修_2111338389898354689.json、图片生成/图生图/Flux-3-Image-Klein多图编辑，图生图素材整合利器_2111560906680393729.json、图片生成/图生图/Flux2 Klein去除卡片工作流，图生图精准移除图片中卡片元素工具_2103909515577094145.json、图片生成/图生图/Flux2-Klein智能扩图｜图片外补全图生图工作流_2093112866625900545.json、图片生成/图生图/flux-2-klein-9b去文字利器｜图生图轻松抹除画面文字_2105226424310394881.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `BasicGuider` —— 3/5 个有
- `Flux2Scheduler` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `CFGGuider` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `ManualSigmas` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `InpaintModelConditioning` —— 1/5 个有
- `Latent Switch (JPS)` —— 1/5 个有
- `PDIMAGE_LongerSize` —— 1/5 个有
- `ReferenceMultiLatent` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有

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
