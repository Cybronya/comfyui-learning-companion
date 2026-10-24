---
name: unknown_workflow_sampler_clip_unet_128
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.956111
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/效果图增强细节，软装色彩分析_2071601421786636290.json, 图片生成/图生图/效果图洗图_增强细节_真实感_2102679806793043970.json, 图片生成/图生图/效果图洗图_增强细节_真实感_2103373723498795010.json, 图片生成/图生图/效果图洗图_增强细节_真实感_零偏移_2062401252247564290.json, 图片生成/图生图/文字清除工作流333333333_2071422706821713921.json, 图片生成/图生图/漫画转欧美美女（解禁模型）：Flux2 Klein 9B_2055197694913720322.json, 图片生成/图生图/电商产品精修快速版_2044583021092802562.json, 图片生成/图生图/电商产品精修美化细节高清放大_2069464540449959937.json, 图片生成/图生图/老孙AI 产品精修_2090283355492413441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_128

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/效果图增强细节，软装色彩分析_2071601421786636290.json、图片生成/图生图/效果图洗图_增强细节_真实感_2102679806793043970.json、图片生成/图生图/效果图洗图_增强细节_真实感_2103373723498795010.json、图片生成/图生图/效果图洗图_增强细节_真实感_零偏移_2062401252247564290.json、图片生成/图生图/文字清除工作流333333333_2071422706821713921.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `GetImageSize` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `ConstrainImage|pysssss` —— 4/9 个有
- `LoraLoaderBypassModelOnly` —— 4/9 个有
- `ImageUpscaleWithModel` —— 2/9 个有
- `UpscaleModelLoader` —— 2/9 个有
- `Load Image From Url (mtb)` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `easy imageColorMatch` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
