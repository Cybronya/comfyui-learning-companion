---
name: unknown_workflow_sampler_clip_unet_140
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.914125
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/3.扩展图片_2050623451928510466.json, 图片生成/图生图/360-全景照片地图编辑查看_2042620819846733826.json, 图片生成/图生图/FLUX2-Klein Flux-2-Klein-9B 多图编辑  电商产品场景 万能迁移 光影一致_2025034756479524865.json, 图片生成/图生图/FLUX2-Klein扩图_2044259641374281729.json, 图片生成/图生图/FLUX2Klein 单图编辑_2026497012299993090.json, 图片生成/图生图/FLUX2Klein一次性批量扩图_2053020098847354882.json, 图片生成/图生图/flux 2 klein 无缝扩图+局部重绘_2017924280838791170.json, 图片生成/图生图/一键扩图工作流_2095410279856300033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_140

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/3.扩展图片_2050623451928510466.json、图片生成/图生图/360-全景照片地图编辑查看_2042620819846733826.json、图片生成/图生图/FLUX2-Klein Flux-2-Klein-9B 多图编辑  电商产品场景 万能迁移 光影一致_2025034756479524865.json、图片生成/图生图/FLUX2-Klein扩图_2044259641374281729.json、图片生成/图生图/FLUX2Klein 单图编辑_2026497012299993090.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `EmptyFlux2LatentImage` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `ImagePadForOutpaint` —— 6/8 个有
- `ColorMatch` —— 4/8 个有
- `DrawMaskOnImage` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `easy seed` —— 2/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `CustomAddLabel` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `ImpactMakeAnyList` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `ResizeImagesByLongerEdge` —— 1/8 个有
- `TY360Pasteback` —— 1/8 个有
- `TY360Preview` —— 1/8 个有
- `TY360Roundtrip` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
