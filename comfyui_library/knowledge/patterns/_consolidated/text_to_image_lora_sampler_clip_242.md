---
name: text_to_image_lora_sampler_clip_242
type: Text To Image
frequency: 8
level: strong
coverage: 0.90025
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Flux2Scheduler, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein智能扩图｜图片外补全图生图工作流_2093112866625900545.json, 图片生成/图生图/Flux2Klein 4B加速版多图编辑 高效换头换脸_2098106416744722433.json, 图片生成/图生图/Flux2Klein多图编辑4B加速｜写实换头换脸图生图_2090541141182734337.json, 图片生成/图生图/Flux2Klein换内衣｜图生图服装替换_2089687838047694850.json, 图片生成/图生图/Klein 9B商业级光影融合工作流零偏移处理_2100306858379669505.json, 图片生成/图生图/PS级扩图无需参数，角色一致性图生图扩图方案_2110823025108148226.json, 图片生成/图生图/flux-2-klein-9b去文字利器｜图生图轻松抹除画面文字_2105226424310394881.json, 图片生成/图生图/皮带纹路质感优化 lora增强光感清晰度与细节_2098300203974619138.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_242

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein智能扩图｜图片外补全图生图工作流_2093112866625900545.json、图片生成/图生图/Flux2Klein 4B加速版多图编辑 高效换头换脸_2098106416744722433.json、图片生成/图生图/Flux2Klein多图编辑4B加速｜写实换头换脸图生图_2090541141182734337.json、图片生成/图生图/Flux2Klein换内衣｜图生图服装替换_2089687838047694850.json、图片生成/图生图/Klein 9B商业级光影融合工作流零偏移处理_2100306858379669505.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ConditioningZeroOut` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `GetImageSize` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `JWFloat` —— 3/8 个有
- `ImagePadForOutpaint` —— 2/8 个有
- `ImageSmartSharpen+` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `easy int` —— 2/8 个有
- `CR Text Input Switch (4 way)` —— 1/8 个有
- `DifferentialDiffusion` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `InpaintModelConditioning` —— 1/8 个有
- `InspyrenetRembg` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `ShowText` —— 1/8 个有
- `Text` —— 1/8 个有
- `TextCombinerTwo` —— 1/8 个有
- `easy imageColorMatch` —— 1/8 个有
- `easy imageScaleDownToSize` —— 1/8 个有
- `easy imageSize` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
