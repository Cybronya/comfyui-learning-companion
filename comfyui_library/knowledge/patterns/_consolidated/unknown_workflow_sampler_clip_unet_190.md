---
name: unknown_workflow_sampler_clip_unet_190
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.935286
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, ImageConcanate, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein-9B-产品迁移完美细节多图编辑+放大_2012088188105400322.json, 图片生成/图生图/Flux2 Klein-多图编辑-4B加速版_2012124773035286530.json, 图片生成/图生图/Flux2-Klein+产品精修_2017042202211389442.json, 图片生成/图生图/Flux2-Klein+模特换姿势_2012147180743692290.json, 图片生成/图生图/Flux2-Klein+模特换装_2012142481311277058.json, 图片生成/图生图/Flux2-Klein-9b(仅启用图片编辑，可转角度重打光）_2012726330126766082.json, 图片生成/图生图/klein单图编辑——修改版_2033387043891449857.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_190

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein-9B-产品迁移完美细节多图编辑+放大_2012088188105400322.json、图片生成/图生图/Flux2 Klein-多图编辑-4B加速版_2012124773035286530.json、图片生成/图生图/Flux2-Klein+产品精修_2017042202211389442.json、图片生成/图生图/Flux2-Klein+模特换姿势_2012147180743692290.json、图片生成/图生图/Flux2-Klein+模特换装_2012142481311277058.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ImageScaleToTotalPixels` —— 6/7 个有
- `GetImageSize` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageUpscaleWithModel` —— 2/7 个有
- `JWFloat` —— 2/7 个有
- `UpscaleModelLoader` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ConstrainImage|pysssss` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `QwenMultiangleCameraNode` —— 1/7 个有
- `QwenMultiangleLightningNode` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
