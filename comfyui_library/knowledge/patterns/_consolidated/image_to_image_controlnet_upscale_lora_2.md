---
name: image_to_image_controlnet_upscale_lora_2
type: Image To Image
frequency: 9
level: strong
coverage: 0.517889
common_nodes: [AILab_QwenVL, AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DWPreprocessor, GetImageSize, ImageResizeKJv2, ImageSmartSharpen+, ImpactSwitch, JWInteger, KSampler, LatentPixelScale, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, MuterSwitcher, RebatchLatents, RepeatLatentBatch, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy imageRemBg, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Controlnet 控制姿势_深度_线稿+Z-image图生图重绘工作流_2045842900344377345.json, 图片生成/图生图/ZImage+Controlnet-姿势-深度-线稿-重绘_2050001116250820610.json, 图片生成/图生图/pose参考 +全节点注释_2054138427507003394.json, 图片生成/图生图/姿势_深度_线稿_重绘 四合一 pose参考(Z-image Controlnet union )_2028740037910732801.json, 图片生成/图生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013939541400363009.json, 图片生成/文生图/姿势_深度_线稿_重绘 四合一邻家AI大女孩_2045509959374344194.json, 图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_1996350694477152257.json, 图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013930008091299841.json, 图片生成/文生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2041868489656373249.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Controlnet 控制姿势_深度_线稿+Z-image图生图重绘工作流_2045842900344377345.json、图片生成/图生图/ZImage+Controlnet-姿势-深度-线稿-重绘_2050001116250820610.json、图片生成/图生图/pose参考 +全节点注释_2054138427507003394.json、图片生成/图生图/姿势_深度_线稿_重绘 四合一 pose参考(Z-image Controlnet union )_2028740037910732801.json、图片生成/图生图/造相Z-image Controlnet union 姿势_深度_线稿_重绘 四合一 pose参考_2013939541400363009.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 9 个 workflow 都包含：
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `GetImageSize`
- `ImageResizeKJv2`
- `ImageSmartSharpen+`
- `ImpactSwitch`
- `JWInteger`
- `KSampler`
- `LatentPixelScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `MuterSwitcher`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy imageRemBg`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 8/9 个有
- `CR Prompt Text` —— 8/9 个有
- `GetNode` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `easy boolean` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `LayerUtility: PurgeVRAM V2` —— 7/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | heun | - | 9 | 78% |
| 调度器 | beta | - | 9 | 78% |
| 重绘幅度 | 1 | 0.5 - 1 | 9 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，9 个样本，一致性 78%
- 调度器 最常用 beta，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，9 个样本
- 高发问题（17/9 个样本）：Steps较低可能导致细节不足
