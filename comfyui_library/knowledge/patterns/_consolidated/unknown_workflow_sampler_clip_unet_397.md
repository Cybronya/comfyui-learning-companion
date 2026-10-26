---
name: unknown_workflow_sampler_clip_unet_397
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.852667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/danotebook-flux2-klein-9b_2062427994236481537.json, 图片生成/文生图/klein_文生图+图像编辑_2042538360702509058.json, 图片生成/文生图/klein_文生图+图像编辑【雄舟天文馆版】_2047099039581216770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_397

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/danotebook-flux2-klein-9b_2062427994236481537.json、图片生成/文生图/klein_文生图+图像编辑_2042538360702509058.json、图片生成/文生图/klein_文生图+图像编辑【雄舟天文馆版】_2047099039581216770.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `InversionDemoLazySwitch` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `StringCompare` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
