---
name: unknown_workflow_sampler_clip_unet_289
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84075
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【Flux2+Klein】+双图编辑（可切换出图方式版）_2013780423263920130.json, 图片生成/图生图/一键生成婚纱照_2045753551078559745.json, 图片生成/图生图/图生图  姿态，深度，线稿，一键参考 Klein 9b_2073945500046417922.json, 图片生成/图生图/姿势参考 深度参考 线稿参考 Klein9B_2073931120416219137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_289

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【Flux2+Klein】+双图编辑（可切换出图方式版）_2013780423263920130.json、图片生成/图生图/一键生成婚纱照_2045753551078559745.json、图片生成/图生图/图生图  姿态，深度，线稿，一键参考 Klein 9b_2073945500046417922.json、图片生成/图生图/姿势参考 深度参考 线稿参考 Klein9B_2073931120416219137.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
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
- `GetImageSize` —— 3/4 个有
- `Int` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `DuckHideNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Multi Text Merge` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `Switch` —— 1/4 个有
- `TT_img_enc_v2` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
