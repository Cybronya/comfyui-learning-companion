---
name: unknown_workflow_video_lora_sampler_107
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.447929
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2077357335839854594.json, 视频生成/图生视频/2077460288709947393.json, 视频生成/图生视频/2077288214603329538.json, 视频生成/图生视频/2077324573078548481.json, 视频生成/图生视频/2070484357101473794.json, 视频生成/图生视频/2079863299176484866.json, 视频生成/图生视频/2071782259115511810.json, 视频生成/图生视频/2071786306396573698.json, 视频生成/图生视频/Scail  2 双人互动替换_2066357363409510402.json, 视频生成/图生视频/2067529633486168065.json, 视频生成/图生视频/scail 2 单人电商带货 人物产品替换_2067503598057123841.json, 视频生成/图生视频/scail 2 单人电商带货 人物产品替换自动版_2067564547317264386.json, 视频生成/图生视频/2067087693439397890.json, 视频生成/图生视频/2067282833252634625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2077357335839854594.json、视频生成/图生视频/2077460288709947393.json、视频生成/图生视频/2077288214603329538.json、视频生成/图生视频/2077324573078548481.json、视频生成/图生视频/2070484357101473794.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 13/14 个有
- `DiffusionModelLoaderKJ` —— 13/14 个有
- `PrimitiveInt` —— 13/14 个有
- `EmptyImage` —— 10/14 个有
- `GetImageSize` —— 10/14 个有
- `ImageCompositeMasked` —— 10/14 个有
- `PreviewAny` —— 10/14 个有
- `SAM3_TrackToMask` —— 10/14 个有
- `TensorLoopClose` —— 10/14 个有
- `TensorLoopOpen` —— 10/14 个有
- `DownloadAndLoadGIMMVFIModel` —— 9/14 个有
- `GIMMVFI_interpolate` —— 9/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `Text` —— 7/14 个有
- `VHS_VideoInfoSource` —— 7/14 个有
- `easy imageCount` —— 7/14 个有
- `easy showAnything` —— 7/14 个有
- `JWInteger` —— 6/14 个有
- `RH_Captioner` —— 6/14 个有
- `easy indexAnything` —— 5/14 个有
- `DrawMaskOnImage` —— 4/14 个有
- `Fast Groups Bypasser (rgthree)` —— 4/14 个有
- `ImageConcatMulti` —— 4/14 个有
- `Int` —— 4/14 个有
- `InvertMask` —— 4/14 个有
- `RH_RhartImageG2OfficialImageToImage` —— 4/14 个有
- `ResizeImageMaskNode` —— 4/14 个有
- `TextConcatenate_UTK` —— 4/14 个有
- `WanChunkFeedForward` —— 4/14 个有
- `1hew_MaskMathOps` —— 2/14 个有
- `ColorPickerMW` —— 2/14 个有
- `FillMaskWithColor` —— 2/14 个有
- `JjkText` —— 2/14 个有
- `Switch` —— 2/14 个有
- `Text Multiline` —— 2/14 个有
- `easy mathInt` —— 2/14 个有
- `Bjornulf_ShowInt` —— 1/14 个有
- `CR Text` —— 1/14 个有
- `FL_RIFE` —— 1/14 个有
- `ImageFromBatch` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `PointsEditor` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/14 个有
- `RH_Translator` —— 1/14 个有
- `SeCModelLoader` —— 1/14 个有
- `SeCVideoSegmentation` —— 1/14 个有
- `ShowAnything|Mie` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `UNETLoader` —— 1/14 个有
- `VHS_VideoInfo` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
