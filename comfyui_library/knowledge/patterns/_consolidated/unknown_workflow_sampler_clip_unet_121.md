---
name: unknown_workflow_sampler_clip_unet_121
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.856889
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2_Klein_9B模特换脸工作流_2019648494549602305.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091354005774622721.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091821134911201281.json, 图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2092610607378944002.json, 图片生成/图生图/Flux2‑Klein(黑兽)极速换头换脸完美方案｜极速生成｜完美还原_2090937605646012417.json, 图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092081597083381762.json, 图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092527185998467073.json, 图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092612491082821634.json, 图片生成/图生图/flux2 klein一键无损放大+细节增强_2082363830050578433.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_121

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2_Klein_9B模特换脸工作流_2019648494549602305.json、图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091354005774622721.json、图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2091821134911201281.json、图片生成/图生图/Flux2_Sun_Direction_LoRA_精确控制‌图片光影_2092610607378944002.json、图片生成/图生图/Flux2‑Klein(黑兽)极速换头换脸完美方案｜极速生成｜完美还原_2090937605646012417.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `GetNode` —— 5/9 个有
- `LayerUtility: PurgeVRAM V2` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `Image Crop Face` —— 4/9 个有
- `ImpactInt` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `MuyeTextEditOutput` —— 4/9 个有
- `SphereLightNode` —— 3/9 个有
- `ImageStitch` —— 2/9 个有
- `DifferentialDiffusion` —— 1/9 个有
- `ImageLoader` —— 1/9 个有
- `JWImageResizeByLongerSide` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `TTP_text_mix` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
