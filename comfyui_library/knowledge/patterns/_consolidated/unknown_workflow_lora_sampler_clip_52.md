---
name: unknown_workflow_lora_sampler_clip_52
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.965
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 光源方向控制（重新打光）_2077753659827507201.json, 图片生成/图生图/Klein 漫画线稿参考上色_2077376538961604609.json, 图片生成/图生图/Klein 真实细节_2051257646812020737.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2074742796711448578.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2096041251173912578.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2096156283039735810.json, 图片生成/图生图/万物转动漫极速_2026648982881046530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Klein 光源方向控制（重新打光）_2077753659827507201.json、图片生成/图生图/Klein 漫画线稿参考上色_2077376538961604609.json、图片生成/图生图/Klein 真实细节_2051257646812020737.json、图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json、图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2074742796711448578.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `SaveImage` —— 7/8 个有
- `SphereLightNode` —— 5/8 个有
- `easy imageColorMatch` —— 5/8 个有
- `DF_Integer` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `ImageResize+` —— 4/8 个有
- `RHHiddenNodes` —— 4/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `CompressImages` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `VRAMReserver` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
