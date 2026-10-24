---
name: unknown_workflow_upscale_lora_sampler_51
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.948
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ImageScaleBy, ImageScaleToTotalPixels, LoadImage, LoraLoaderModelOnly, RHHiddenNodes, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/老孙AI 一键OK 老照片修复_2088443376889847809.json, 图片生成/图生图/老孙AI多功能  老照片修复、去水印、偏色曝光_2088834155399442434.json, 图片生成/图生图/老照片修复 模糊变清晰_2052034476519243778.json, 图片生成/图生图/老郑一键老照片修复_2088421738475515906.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/老孙AI 一键OK 老照片修复_2088443376889847809.json、图片生成/图生图/老孙AI多功能  老照片修复、去水印、偏色曝光_2088834155399442434.json、图片生成/图生图/老照片修复 模糊变清晰_2052034476519243778.json、图片生成/图生图/老郑一键老照片修复_2088421738475515906.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHHiddenNodes`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `Float` —— 2/4 个有
- `easy getNode` —— 2/4 个有
- `easy setNode` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
