---
name: unknown_workflow_sampler_clip_unet_178
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.930375
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, ImageConcanate, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein-9B-产品迁移完美细节多图编辑+放大_2012088188105400322.json, 图片生成/图生图/Flux2 Klein-多图编辑-4B加速版_2012124773035286530.json, 图片生成/图生图/Flux2-Klein+产品精修_2017042202211389442.json, 图片生成/图生图/Flux2-Klein+模特换姿势_2012147180743692290.json, 图片生成/图生图/Flux2-Klein+模特换装_2012142481311277058.json, 图片生成/图生图/Flux2-Klein-9b(仅启用图片编辑，可转角度重打光）_2012726330126766082.json, 图片生成/图生图/klein单图编辑——修改版_2033387043891449857.json, 平台全量/Klein编辑图片换脸换装服装迁移风格迁移_2036249839138250754.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_178

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein-9B-产品迁移完美细节多图编辑+放大_2012088188105400322.json、图片生成/图生图/Flux2 Klein-多图编辑-4B加速版_2012124773035286530.json、图片生成/图生图/Flux2-Klein+产品精修_2017042202211389442.json、图片生成/图生图/Flux2-Klein+模特换姿势_2012147180743692290.json、图片生成/图生图/Flux2-Klein+模特换装_2012142481311277058.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageConcanate`
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
- `ImageScaleToTotalPixels` —— 7/8 个有
- `GetImageSize` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `JWFloat` —— 2/8 个有
- `QwenMultiangleCameraNode` —— 2/8 个有
- `QwenMultiangleLightningNode` —— 2/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `easy imageSize` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ConstrainImage|pysssss` —— 1/8 个有
- `ImagePadForOutpaint` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `OpenposePreprocessor` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
