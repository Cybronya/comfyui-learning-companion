---
name: unknown_workflow_upscale_sampler_clip_2
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.782125
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Image Replication洗图姿势动作迁移 SeedVR+高清放大_2100745991401070594.json, 图片生成/图生图/Pose Transfer + krea2 + turbo （洗图）姿势动作迁移_2097150626210869250.json, 图片生成/图生图/Z-IMAGE去除人像AI感+高清放大+最新皮肤质感LORA_1995317634671554561.json, 图片生成/图生图/krea turbo洗图+seedvr2高清放大_2070375917419061249.json, 图片生成/图生图/krea turbo洗图+seedvr2高清放大_2070406276529614850.json, 图片生成/图生图/krea turbo洗图+seedvr2高清放大_2070423895731171330.json, 图片生成/图生图/krea turbo洗图+seedvr2高清放大_2083870836859166721.json, 图片生成/图生图/krea2 turbo + SeedVR 放大+图生图（洗图）=直出4K_2071475400043229185.json, 图片生成/图生图/krea2 turbo + SeedVR 放大+图生图（洗图）=直出4K_2071516612934586369.json, 图片生成/图生图/krea2 turbo SeedVR+高清放大+图生图（重绘洗图） 去油腻修复皮肤质感+高清放大修复_2074290818332061697.json, 图片生成/图生图/万物精修-一致性保持_klein精修工作流_2068396367621484545.json, 图片生成/图生图/图生图（洗图）姿势动作迁移 krea2 turbo SeedVR+高清放大+ 直出4K_2071766159808094209.json, 图片生成/图生图/姿态复制 姿势动作迁移 图生图（洗图） krea2 turbo SeedVR+高清放大+ 直出4K_2071776268462415874.json, 图片生成/图生图/开源参数猛兽FLUX2系列 — 多图组合生图_1993637280518782978.json, 图片生成/图生图/开源参数猛兽FLUX2系列 —— 单图生图片_1993627343866494977.json, 图片生成/文生图/开源参数猛兽FLUX2系列 —— 文字生图片_1993607069964107777.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Image Replication洗图姿势动作迁移 SeedVR+高清放大_2100745991401070594.json、图片生成/图生图/Pose Transfer + krea2 + turbo （洗图）姿势动作迁移_2097150626210869250.json、图片生成/图生图/Z-IMAGE去除人像AI感+高清放大+最新皮肤质感LORA_1995317634671554561.json、图片生成/图生图/krea turbo洗图+seedvr2高清放大_2070375917419061249.json、图片生成/图生图/krea turbo洗图+seedvr2高清放大_2070406276529614850.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 15/16 个有
- `VAEEncode` —— 15/16 个有
- `AILab_QwenVL` —— 12/16 个有
- `BasicScheduler` —— 12/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/16 个有
- `PrimitiveInt` —— 11/16 个有
- `Fast Groups Bypasser (rgthree)` —— 9/16 个有
- `Int` —— 7/16 个有
- `ImageScaleBy` —— 5/16 个有
- `EmptyFlux2LatentImage` —— 4/16 个有
- `Flux2Scheduler` —— 4/16 个有
- `LayerUtility: PurgeVRAM V2` —— 4/16 个有
- `CR Text` —— 3/16 个有
- `FluxGuidance` —— 3/16 个有
- `ImpactInt` —— 3/16 个有
- `ReferenceLatent` —— 3/16 个有
- `ImageScaleToTotalPixels` —— 2/16 个有
- `LoraLoaderModelOnly` —— 2/16 个有
- `GetImageSize` —— 1/16 个有
- `LyingSigmaSampler` —— 1/16 个有
- `PreviewAny` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
