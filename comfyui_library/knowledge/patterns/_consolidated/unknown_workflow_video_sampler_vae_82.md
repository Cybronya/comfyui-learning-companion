---
name: unknown_workflow_video_sampler_vae_82
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.697714
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, PixelPerfectResolution, PointsEditor, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, RMBG, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, UnloadModel, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [平台全量/万能手动遮罩2人以上视频中的替换人物或换脸换头换衣服+口播对口型短视频商业短视频_2060603003312369666.json, 平台全量/万能手动遮罩2人以上视频中的替换人物或换脸换头换衣服+口播对口型短视频商业短视频_2083918207328546817.json, 平台全量/指定人物替换-手动遮罩替换多人视频中的指定人物+WanAnimate_2025105397538885633.json, 平台全量/替换多人视频中的某个人 万能手动遮罩2人以上视频中的替换Z3_2025379505409368066.json, 平台全量/替换视频中的产品  适合手持的小产品，Plus模式_2044806098640707586.json, 视频生成/图生视频/指定人物替换-手动遮罩替换多人视频中的指定人物+WanAnimate_2064955834492342273.json, 视频生成/图生视频/电商带货 直播带货 短视频_2043943018939551745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_82

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/万能手动遮罩2人以上视频中的替换人物或换脸换头换衣服+口播对口型短视频商业短视频_2060603003312369666.json、平台全量/万能手动遮罩2人以上视频中的替换人物或换脸换头换衣服+口播对口型短视频商业短视频_2083918207328546817.json、平台全量/指定人物替换-手动遮罩替换多人视频中的指定人物+WanAnimate_2025105397538885633.json、平台全量/替换多人视频中的某个人 万能手动遮罩2人以上视频中的替换Z3_2025379505409368066.json、平台全量/替换视频中的产品  适合手持的小产品，Plus模式_2044806098640707586.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PixelPerfectResolution`
- `PointsEditor`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `RMBG`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UnloadModel`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoSetLoRAs` —— 6/7 个有
- `GrowMaskWithBlur` —— 5/7 个有
- `AudioCrop` —— 4/7 个有
- `JWIntegerToString` —— 4/7 个有
- `PreviewAudio` —— 4/7 个有
- `SeCModelLoader` —— 4/7 个有
- `SeCVideoSegmentation` —— 4/7 个有
- `WanVideoContextOptions` —— 4/7 个有
- `DWPreprocessor` —— 3/7 个有
- `WanVideoAnimateEmbeds` —— 3/7 个有
- `MultiTalkModelLoader` —— 2/7 个有
- `WanVideoEnhanceAVideo` —— 2/7 个有
- `WanVideoLoraSelectMulti` —— 2/7 个有
- `WanVideoSLG` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
