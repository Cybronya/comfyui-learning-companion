---
name: text_to_image_lora_sampler_clip_33
type: Text To Image
frequency: 21
level: strong
coverage: 0.833048
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Integer, EmptyLatentImage, Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/8K高清放大｜图生图无损提升分辨率细节看得清_2101554995991760898.json, 图片生成/图生图/万物高清放大修复｜seedVR2分块不改变原细节_2094911365621305345.json, 图片生成/图生图/万能图片去水印加高清 支持上传遮罩图精准处理_2109021264206716929.json, 图片生成/图生图/万能图片去水印加高清支持上传遮罩图处理工具_2100305309117018114.json, 图片生成/图生图/万能图片去水印加高清支持上传遮罩图，图生图去水印高清修复工具_2105758871070531586.json, 图片生成/图生图/万能图片去水印加高清支持遮罩图生图处理工具_2101743658600062977.json, 图片生成/图生图/万能图片去水印加高清，支持遮罩图精准擦除水印痕迹_2112648650630455297.json, 图片生成/图生图/万能图片去水印加高清｜支持上传遮罩图处理_2092384278859575298.json, 图片生成/图生图/万能图片去水印加高清｜支持上传遮罩图精准处理_2094861540045443074.json, 图片生成/图生图/万能图片去水印加高清｜支持上传遮罩图精准处理_2101573701710999554.json, 图片生成/图生图/万能图片去水印加高清｜支持上传遮罩图精准擦除｜水印再多也不怕_2102580823512932353.json, 图片生成/图生图/万能图片去水印并高清修复，支持自定义遮罩图上传的图生图工具_2102814648360857602.json, 图片生成/图生图/万能图片去水印并高清修复，支持自定义遮罩图上传的图生图工具_2106556652001521665.json, 图片生成/图生图/万能图片去水印高清工作流｜支持遮罩图智能画质修复_2097411370491932674.json, 图片生成/图生图/万能图片处理｜去水印加高清支持遮罩图生成_2090873698050985985.json, 图片生成/图生图/分块seedVR2放大修复｜万物高清细节原样保留_2095099392045961218.json, 图片生成/图生图/去水印加高清｜万能图片处理支持上传遮罩图_2093793932093251585.json, 图片生成/图生图/支持上传遮罩图去水印加高清｜万能图片图生图其他创意工作流_2088384656562544641.json, 图片生成/图生图/支持上传遮罩图｜万能图片去水印加高清图生图处理_2095076890104123394.json, 图片生成/图生图/支持上传遮罩图｜万能图片去水印加高清处理_2094016965957472258.json, 图片生成/图生图/支持遮罩图的万能去水印方案 图片同步高清修复_2104288990701641730.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/8K高清放大｜图生图无损提升分辨率细节看得清_2101554995991760898.json、图片生成/图生图/万物高清放大修复｜seedVR2分块不改变原细节_2094911365621305345.json、图片生成/图生图/万能图片去水印加高清 支持上传遮罩图精准处理_2109021264206716929.json、图片生成/图生图/万能图片去水印加高清支持上传遮罩图处理工具_2100305309117018114.json、图片生成/图生图/万能图片去水印加高清支持上传遮罩图，图生图去水印高清修复工具_2105758871070531586.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `EmptyLatentImage`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 20/21 个有
- `SetNode` —— 20/21 个有
- `孤海注释` —— 20/21 个有
- `CFGNorm` —— 18/21 个有
- `ConditioningZeroOut` —— 18/21 个有
- `DrawMaskOnImage` —— 18/21 个有
- `ImageUpscaleWithModel` —— 18/21 个有
- `LayerMask: MaskPreview` —— 18/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/21 个有
- `LoadImageMask` —— 18/21 个有
- `MaskBlur+` —— 18/21 个有
- `MaskFillHoles` —— 18/21 个有
- `ModelSamplingAuraFlow` —— 18/21 个有
- `RunningHub Deepcleaner` —— 18/21 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 18/21 个有
- `UpscaleModelLoader` —— 18/21 个有
- `VAEEncode` —— 18/21 个有
- `Image Comparer (rgthree)` —— 3/21 个有
- `GetNode` —— 2/21 个有
- `EmptyImage` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 39/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（39/21 个样本）：Steps较低可能导致细节不足
