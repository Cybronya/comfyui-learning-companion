---
name: unknown_workflow_sampler_clip_unet_74
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.89325
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2‑Klein(黑兽)极速换头换脸完美方案｜极速生成｜完美还原_2090937605646012417.json, 图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092081597083381762.json, 图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092527185998467073.json, 图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092612491082821634.json, 图片生成/图生图/Flux2转换角度_2015006159463256065.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2041822266979262465.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2067227622874107905.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器图生图局部重绘！Flux2！_2082102047633141761.json, 图片生成/图生图/Klein BFS 换脸换头加强版生成器！Flux2！_2041743908442476546.json, 图片生成/图生图/Klein BFS 换脸换头！加强版！Flux2_2041514830745571329.json, 图片生成/图生图/WH-AI-Studio电商图片高清放大增强细节提高真实感（皮肤、服装材质放大器）_2022619703398633474.json, 图片生成/图生图/WH-AI-Studio电商换装-服装迁移-flux2-klein(材质增强版)(超越原图材质)_2022631112878592002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux2‑Klein(黑兽)极速换头换脸完美方案｜极速生成｜完美还原_2090937605646012417.json、图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092081597083381762.json、图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092527185998467073.json、图片生成/图生图/Flux2‑Klein极速换头换脸完美方案｜极速生成｜完美还原_2092612491082821634.json、图片生成/图生图/Flux2转换角度_2015006159463256065.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 11/12 个有
- `ConditioningZeroOut` —— 10/12 个有
- `Image Crop Face` —— 9/12 个有
- `LayerUtility: PurgeVRAM V2` —— 9/12 个有
- `GetNode` —— 6/12 个有
- `Image Comparer (rgthree)` —— 6/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/12 个有
- `SetNode` —— 6/12 个有
- `LayerUtility: ImageReel` —— 5/12 个有
- `LayerUtility: ImageReelComposit` —— 5/12 个有
- `ImpactInt` —— 4/12 个有
- `MuyeTextEditOutput` —— 4/12 个有
- `Anything Everywhere` —— 2/12 个有
- `Image Blending Mode` —— 2/12 个有
- `LayerColor: ColorAdapter` —— 2/12 个有
- `PainterFluxImageEdit` —— 1/12 个有
- `QwenMultiangleCameraNode` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有
- `easy positive` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
