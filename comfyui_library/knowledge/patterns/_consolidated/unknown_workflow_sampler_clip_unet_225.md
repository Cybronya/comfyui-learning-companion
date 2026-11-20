---
name: unknown_workflow_sampler_clip_unet_225
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【Flux2+Klein】+双图编辑（可切换出图方式版）_2013780423263920130.json, 图片生成/图生图/【flux2-klein】动漫人物转真人_2018492884374261761.json, 图片生成/图生图/【flux2-klein】手绘漫画风格_2018497479477567489.json, 图片生成/图生图/万物转动漫极速_2026648982881046530.json, 图片生成/图生图/图生图  姿态，深度，线稿，一键参考 Klein 9b_2073945500046417922.json, 图片生成/图生图/姿势参考 深度参考 线稿参考 Klein9B_2073931120416219137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_225

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【Flux2+Klein】+双图编辑（可切换出图方式版）_2013780423263920130.json、图片生成/图生图/【flux2-klein】动漫人物转真人_2018492884374261761.json、图片生成/图生图/【flux2-klein】手绘漫画风格_2018497479477567489.json、图片生成/图生图/万物转动漫极速_2026648982881046530.json、图片生成/图生图/图生图  姿态，深度，线稿，一键参考 Klein 9b_2073945500046417922.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
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
- `LoraLoaderModelOnly` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `Int` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `ImpactSwitch` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `easy imageConcat` —— 2/6 个有
- `DuckHideNode` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `Switch` —— 1/6 个有
- `TT_img_enc_v2` —— 1/6 个有
- `VRAMReserver` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy imageColorMatch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
