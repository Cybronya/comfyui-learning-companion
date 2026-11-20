---
name: unknown_workflow_video_lora_sampler_115
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.575063
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetNode, ImageResizeKJv2, LoadImage, SetNode, Textbox, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【CQ808】去掉多余的人，替换元素_2116141027512905730.json, 图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json, 图片生成/图生图/视频去水印去字幕_2042494499506626561.json, 平台全量/【CQ808】去掉多余的人，替换元素_2042078246400958466.json, 平台全量/一次性去掉视频的字幕和水印wan2.2animate 不限制时长 24秒测试成功_1972495184342740993.json, 平台全量/一次性去掉视频的字幕和水印wan2.2animate_1972256984982614018.json, 平台全量/万能视频去水印-支持所有水印，（包括全能视频S2，Seedance 2.0 等）去字幕效果无敌好_2009539023521452033.json, 平台全量/去掉多余的人_2051139856813830145.json, 平台全量/去水印-帧数对齐版_2036745765598535681.json, 平台全量/去水印6（z）_2101950450865098753.json, 平台全量/手动遮罩视频去水印视频去字幕wan2.1 animate模型_2061065474384945153.json, 平台全量/视频去水印+去字幕+去除物体+去人的工作流_2027655892136628225.json, 平台全量/视频去水印_2036401771924430850.json, 平台全量/视频去水印_2041451595581362177.json, 平台全量/视频去水印视频去字幕去除指定物品工作流基于wan2.2 animate_1978289406870183937.json, 平台全量/视频去水印（不少帧版）_2049793804554776578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_115

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/【CQ808】去掉多余的人，替换元素_2116141027512905730.json、图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json、图片生成/图生图/视频去水印去字幕_2042494499506626561.json、平台全量/【CQ808】去掉多余的人，替换元素_2042078246400958466.json、平台全量/一次性去掉视频的字幕和水印wan2.2animate 不限制时长 24秒测试成功_1972495184342740993.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 16 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `Textbox`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 15/16 个有
- `PreviewImage` —— 15/16 个有
- `RH_Translator` —— 15/16 个有
- `WanVideoTextEncodeCached` —— 15/16 个有
- `easy showAnything` —— 15/16 个有
- `Frame Select` —— 14/16 个有
- `VHS_VideoInfo` —— 14/16 个有
- `DownloadAndLoadGIMMVFIModel` —— 13/16 个有
- `GIMMVFI_interpolate` —— 13/16 个有
- `ImageConcatMulti` —— 13/16 个有
- `easy showTensorShape` —— 13/16 个有
- `DF_Get_image_size` —— 10/16 个有
- `INTConstant` —— 10/16 个有
- `PointsEditor` —— 8/16 个有
- `Sam2Segmentation` —— 8/16 个有
- `DownloadAndLoadSAM2Model` —— 7/16 个有
- `AILab_MaskPreview` —— 6/16 个有
- `Bookmark (rgthree)` —— 6/16 个有
- `OnnxDetectionModelLoader` —— 5/16 个有
- `LoadImageMask` —— 3/16 个有
- `RHHiddenNodes` —— 3/16 个有
- `FL_ImageAddToBatch` —— 2/16 个有
- `ImageBatchCopy` —— 2/16 个有
- `ImageFromBatch+` —— 2/16 个有
- `PreviewBridge` —— 2/16 个有
- `SimpleMath+` —— 2/16 个有
- `ImageToMask` —— 1/16 个有
- `Int` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `LayerUtility: PurgeVRAM V2` —— 1/16 个有
- `Primitive integer [Crystools]` —— 1/16 个有
- `PrimitiveInt` —— 1/16 个有
- `ShowAnything|Mie` —— 1/16 个有
- `VHS_GetImageCount` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
