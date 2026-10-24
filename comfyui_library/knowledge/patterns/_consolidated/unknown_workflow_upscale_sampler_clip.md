---
name: unknown_workflow_upscale_sampler_clip
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.920667
common_nodes: [BasicGuider, CLIPLoader_Any, CLIPTextEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/4宫格拆分并放大_2075110008823566338.json, 图片生成/图生图/4宫格拆分并放大_2075385138648797186.json, 图片生成/图生图/AI换衣服去脏-自己解决版_2096106167410974722.json, 图片生成/图生图/flux2-klein-TTP分块-胶片级高清修复放大-6400万像素_2062516408864559105.json, 图片生成/图生图/flux2-klein-TTP分块放大_2089694393820340226.json, 图片生成/图生图/flux2-klein-TTP分块放大_轻量版_2087436012850081793.json, 图片生成/图生图/flux2-klein-TTP分块放大_轻量版_2092448589174886402.json, 图片生成/图生图/flux2kleinTTP分块胶片级高清修复放大6000万像素_2066095518450798593.json, 图片生成/图生图/flux2kleinTTP分块胶片级高清修复放大6400万像素_2066702884049342465.json, 图片生成/图生图/全能图片G生图去噪点 Image2.5去脏_2100479016217169921.json, 图片生成/图生图/去噪点去脏_2107761045216514049.json, 图片生成/图生图/去噪点去脏_2109597941571874818.json, 图片生成/图生图/沙发产品    正常版_2077027637486243842.json, 图片生成/图生图/沙发产品   分开式_2077026599085625346.json, 图片生成/图生图/沙发产品   暗图版_2077027335349559298.json, 图片生成/图生图/沙发产品 seedream-v5-pro_2084627713939296257.json, 图片生成/图生图/沙发产品 seedream-v5-pro_2084635101186576386.json, 图片生成/图生图/沙发产品 seedream-v5-pro_2095136946577297409.json, 图片生成/图生图/沙发产品 洗图与裂变【暗图恢复版】_2073073229408858113.json, 图片生成/图生图/沙发产品 洗图与裂变【正常明度稳定版】_2072347712078569474.json, 视频生成/图生视频/沙发产品 分开式_2074158653199970305.json, 视频生成/图生视频/沙发产品 暗图版_2074158159417135105.json, 视频生成/图生视频/沙发产品 正常版_2073770723931418626.json, 视频生成/图生视频/沙发产品 裂变 暗图恢复 多视图 宣传视频 _ 分开式合集_2073280704120709122.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/4宫格拆分并放大_2075110008823566338.json、图片生成/图生图/4宫格拆分并放大_2075385138648797186.json、图片生成/图生图/AI换衣服去脏-自己解决版_2096106167410974722.json、图片生成/图生图/flux2-klein-TTP分块-胶片级高清修复放大-6400万像素_2062516408864559105.json、图片生成/图生图/flux2-klein-TTP分块放大_2089694393820340226.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 23/24 个有
- `KSamplerSelect` —— 23/24 个有
- `Image Comparer (rgthree)` —— 18/24 个有
- `SaveImage` —— 18/24 个有
- `PreviewImage` —— 16/24 个有
- `ImageGridSplitNode` —— 14/24 个有
- `Int` —— 14/24 个有
- `easy imageInsetCrop` —— 14/24 个有
- `easy imagesSplitImage` —— 14/24 个有
- `JjkText` —— 12/24 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 12/24 个有
- `RH_RhartImageG2ImageToImage` —— 12/24 个有
- `Fast Bypasser (rgthree)` —— 9/24 个有
- `Mute / Bypass Repeater (rgthree)` —— 9/24 个有
- `RH_Captioner_Pro` —— 9/24 个有
- `RH_RhartVideoSparkvideo20MiniImageToVideo` —— 9/24 个有
- `SaveVideo` —— 9/24 个有
- `easy showAnything` —— 9/24 个有
- `kkMergeVideos` —— 9/24 个有
- `LoraLoaderModelOnly` —— 8/24 个有
- `SaveImageJPG_GH` —— 8/24 个有
- `Switch image [Crystools]` —— 6/24 个有
- `LayerFilter: FilmV2` —— 4/24 个有
- `RH_SeedreamV5ProImageToImage` —— 4/24 个有
- `easy float` —— 4/24 个有
- `孤海注释` —— 3/24 个有
- `FilmGrain` —— 2/24 个有
- `ImageScaleBy` —— 2/24 个有
- `LayerColor: Color of Shadow & Highlight` —— 2/24 个有
- `workflow>采样` —— 2/24 个有
- `INTConstant` —— 1/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
