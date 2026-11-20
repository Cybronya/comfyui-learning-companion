---
name: unknown_workflow_sampler_clip_unet_278
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.821
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Seedream 5 单图双图多图多功能编辑 +增加细节+高清放大  去除AI塑料感 Flux2 K_2028027785586937858.json, 平台全量/Seedream 5.0+Flux2-klein-9B  图像编辑 服饰换装 换装换脸 风格统一_2031177319376756738.json, 平台全量/flux2_klein_图片编辑&文生图（6G显存可用）_2074037656283082753.json, 平台全量/gemini-3.1 全能图片2.0+图片修复添加细节_2027922023896326146.json, 平台全量/产品换背景 光影重绘 图片换场景 F2 klein 9B_2067073912286040065.json, 平台全量/全能图片2.0 gemini-3.1 +图片修复添加细节 一图生多角度_2027920063872897026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_278

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Seedream 5 单图双图多图多功能编辑 +增加细节+高清放大  去除AI塑料感 Flux2 K_2028027785586937858.json、平台全量/Seedream 5.0+Flux2-klein-9B  图像编辑 服饰换装 换装换脸 风格统一_2031177319376756738.json、平台全量/flux2_klein_图片编辑&文生图（6G显存可用）_2074037656283082753.json、平台全量/gemini-3.1 全能图片2.0+图片修复添加细节_2027922023896326146.json、平台全量/产品换背景 光影重绘 图片换场景 F2 klein 9B_2067073912286040065.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
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
- `CR Text` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `DifferentialDiffusion` —— 3/6 个有
- `GetImageSize` —— 3/6 个有
- `GrowMaskWithBlur` —— 3/6 个有
- `LayerUtility: ImageReel` —— 3/6 个有
- `LayerUtility: ImageReelComposit` —— 3/6 个有
- `Repeater|pysssss` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `Int` —— 2/6 个有
- `MuyeTextEditOutput` —— 2/6 个有
- `RH_Jimeng4_Image2Image` —— 2/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `easy imageScaleDownToSize` —— 2/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
