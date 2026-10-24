---
name: unknown_workflow_sampler_clip_unet_81
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.926818
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein扩图工作流_2052313109414592514.json, 图片生成/图生图/Flux2-Klein扩图工作流_2085318245518766082.json, 图片生成/图生图/Flux2-Klein照片扩图_2105520911993626625.json, 图片生成/图生图/Flux2-klein 一次性多图 电商产品迁移_2046045595718131714.json, 图片生成/图生图/Flux2-klein-4b 蒸馏版图像编辑_2013422354910679042.json, 图片生成/图生图/Flux2-klein-4b 蒸馏版图像编辑_2013484628786552834.json, 图片生成/图生图/Flux2-klein-4b 风格复刻图像编辑_2013505089197056002.json, 图片生成/图生图/Flux2-klein-4b 风格迁移_2013521620928831490.json, 图片生成/图生图/Flux2-klein单图+双图编辑工作流_2015971779197542401.json, 图片生成/图生图/Flux2.Klein图像编辑与扩图重绘_2014617059883225089.json, 图片生成/图生图/flux2 klein扩图工作流_2016349875780194305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_81

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein扩图工作流_2052313109414592514.json、图片生成/图生图/Flux2-Klein扩图工作流_2085318245518766082.json、图片生成/图生图/Flux2-Klein照片扩图_2105520911993626625.json、图片生成/图生图/Flux2-klein 一次性多图 电商产品迁移_2046045595718131714.json、图片生成/图生图/Flux2-klein-4b 蒸馏版图像编辑_2013422354910679042.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetImageSize`
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
- `Image Comparer (rgthree)` —— 9/11 个有
- `EmptyFlux2LatentImage` —— 8/11 个有
- `ConditioningZeroOut` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 7/11 个有
- `ImagePadForOutpaint` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/11 个有
- `easy imageScaleDownToSize` —— 4/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `DrawMaskOnImage` —— 2/11 个有
- `Anything Everywhere` —— 1/11 个有
- `ColorMatch` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `ImpactGaussianBlurMask` —— 1/11 个有
- `ImpactMakeAnyList` —— 1/11 个有
- `MaskPreview+` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `easy imageConcat` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
