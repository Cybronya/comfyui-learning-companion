---
name: unknown_workflow_lora_sampler_unet_88
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.843
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux 2 Klein 9B 无缝扩图｜急速加强版｜指定图像比例｜指定扩图大小_2065271405024989185.json, 图片生成/图生图/[小志Jason] 一致性编辑 Klein 9B_2038069295363657729.json, 图片生成/图生图/klein模型提示词改车色_2063839522978361346.json, 图片生成/图生图/一键无缝融图---flux klein 9b_2049854541050458113.json, 图片生成/图生图/一键无缝融图——Klein_2090612316843896833.json, 图片生成/图生图/一键无缝融图——Klein_2090628254876131329.json, 图片生成/图生图/仅精修车身光影_2061258794776227841.json, 图片生成/图生图/压暗车窗_2064320626726363138.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_88

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux 2 Klein 9B 无缝扩图｜急速加强版｜指定图像比例｜指定扩图大小_2065271405024989185.json、图片生成/图生图/[小志Jason] 一致性编辑 Klein 9B_2038069295363657729.json、图片生成/图生图/klein模型提示词改车色_2063839522978361346.json、图片生成/图生图/一键无缝融图---flux klein 9b_2049854541050458113.json、图片生成/图生图/一键无缝融图——Klein_2090612316843896833.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 7/8 个有
- `CropWithPadInfo_EditUtils` —— 6/8 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `Text` —— 6/8 个有
- `AdaptiveLongestEdge_EditUtils` —— 4/8 个有
- `DF_Get_image_size` —— 4/8 个有
- `GetImageSize` —— 4/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `CheckpointLoaderSimple` —— 3/8 个有
- `InpaintCropImproved` —— 3/8 个有
- `InpaintStitchImproved` —— 3/8 个有
- `RH_Translator` —— 3/8 个有
- `SAM3_Detect` —— 3/8 个有
- `easy promptReplace` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `Int` —— 2/8 个有
- `LayerMask: MaskPreview` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `DapaoImagePadDirectionNode` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
