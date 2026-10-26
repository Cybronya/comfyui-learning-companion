---
name: unknown_workflow_video_lora_sampler_278
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.569625
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetNode, ImageResizeKJv2, LoadImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json, 图片生成/图生图/视频去水印去字幕_2042494499506626561.json, 数字人/数字人/WanAnimate-KJ流遮罩自动获取版_1970211323026022401.json, 数字人/数字人/动作迁移人物替换WanAnimate2.2_1990379558673289217.json, 数字人/数字人/舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346.json, 视频生成/图生视频/自用动作模仿动作迁移_2013906240371429377.json, 视频生成/图生视频/舞蹈克隆改变原图背景_Wan2.2_2062169414258221058.json, 视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_278

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json、图片生成/图生图/视频去水印去字幕_2042494499506626561.json、数字人/数字人/WanAnimate-KJ流遮罩自动获取版_1970211323026022401.json、数字人/数字人/动作迁移人物替换WanAnimate2.2_1990379558673289217.json、数字人/数字人/舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 7/8 个有
- `GIMMVFI_interpolate` —— 7/8 个有
- `GetImageSizeAndCount` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `OnnxDetectionModelLoader` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `DrawViTPose` —— 6/8 个有
- `GrowMask` —— 6/8 个有
- `ImageBlend` —— 6/8 个有
- `Int` —— 6/8 个有
- `PoseAndFaceDetection` —— 6/8 个有
- `MathExpression|pysssss` —— 5/8 个有
- `CR Text` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `Frame Select` —— 2/8 个有
- `PointsEditor` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `SaveLatent` —— 2/8 个有
- `TT_img_enc_v2` —— 2/8 个有
- `Textbox` —— 2/8 个有
- `VHS_VideoInfo` —— 2/8 个有
- `WanVideoEncode` —— 2/8 个有
- `AILab_MaskPreview` —— 1/8 个有
- `Bookmark (rgthree)` —— 1/8 个有
- `DF_Get_image_size` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `easy showAnything` —— 1/8 个有
- `easy showTensorShape` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
