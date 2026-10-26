---
name: unknown_workflow_lora_sampler_clip_45
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.939444
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 光源方向控制（重新打光）_2077753659827507201.json, 图片生成/图生图/Klein 漫画线稿参考上色_2077376538961604609.json, 图片生成/图生图/Klein 真实细节_2051257646812020737.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2074742796711448578.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2096041251173912578.json, 图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2096156283039735810.json, 图片生成/图生图/flux2_klein_图生图-老照片修复_2057843818355052546.json, 图片生成/图生图/动漫到真人转换_2056398938592342018.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Klein 光源方向控制（重新打光）_2077753659827507201.json、图片生成/图生图/Klein 漫画线稿参考上色_2077376538961604609.json、图片生成/图生图/Klein 真实细节_2051257646812020737.json、图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2073950983855628289.json、图片生成/图生图/Klein+Sun_direction_LoRA可控打光_2074742796711448578.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
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
- `GetImageSize` —— 8/9 个有
- `SaveImage` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `SphereLightNode` —— 5/9 个有
- `DF_Integer` —— 4/9 个有
- `ImageResize+` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `easy imageColorMatch` —— 4/9 个有
- `ImageConcatMulti` —— 3/9 个有
- `Label (rgthree)` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `CompressImages` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `Int` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
