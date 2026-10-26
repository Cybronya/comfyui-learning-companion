---
name: unknown_workflow_video_lora_sampler_126
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.681357
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_2014641499442515970.json, 数字人/数字人/Infinitetalk视频对口型_1998680361062293506.json, 数字人/数字人/infiniteTalk单人v2v_2005939130049724418.json, 数字人/数字人/infiniteTalk多人图单人说话_2008829722586783746.json, 数字人/数字人/zy1736_2015662602763898882.json, 数字人/数字人/zy_2014586051662192641.json, 数字人/数字人/改进版KJ-Infinitetalk视频对口型工作流_1959936098648666113.json, 数字人/数字人/最新Infinitetalk优化版视频数字人_1958342598316474369.json, 数字人/数字人/视频对口型 1_2080489097541537793.json, 数字人/数字人/视频对口型_2032501393390571522.json, 数字人/数字人/视频对口型_2036369932333617153.json, 数字人/数字人/🌙最强视频对口型数字人 infinitetalk 真王炸  ⭐_1977899307464622081.json, 数字人/数字人/🥳infinitetalk地表最强数字人 视频对口型 真王炸🐟_1968680206921814017.json, 数字人/数字人/🥳真人视频对口型数字人🐟_2069607155229093890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_126

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_2014641499442515970.json、数字人/数字人/Infinitetalk视频对口型_1998680361062293506.json、数字人/数字人/infiniteTalk单人v2v_2005939130049724418.json、数字人/数字人/infiniteTalk多人图单人说话_2008829722586783746.json、数字人/数字人/zy1736_2015662602763898882.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadWav2VecModel` —— 13/14 个有
- `AudioSeparation` —— 12/14 个有
- `LoadAudio` —— 12/14 个有
- `SimpleMath+` —— 12/14 个有
- `WanVideoTorchCompileSettings` —— 12/14 个有
- `PreviewAny` —— 11/14 个有
- `AudioCrop` —— 10/14 个有
- `Display Int (rgthree)` —— 9/14 个有
- `SoundFlow_GetLength` —— 9/14 个有
- `ToInt` —— 9/14 个有
- `easy int` —— 9/14 个有
- `ImageBatchMulti` —— 8/14 个有
- `ReverseImageBatch` —— 8/14 个有
- `ImageConcatMulti` —— 7/14 个有
- `CR Text` —— 6/14 个有
- `ImpactInt` —— 6/14 个有
- `INTConstant` —— 5/14 个有
- `JWIntegerToString` —— 5/14 个有
- `VHS_LoadAudioUpload` —— 2/14 个有
- `VHS_VideoInfo` —— 2/14 个有
- `Wav2VecModelLoader` —— 2/14 个有
- `image_scale_pixel_v2` —— 2/14 个有
- `Bjornulf_ShowInt` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `GetAudioDurationFromAudio` —— 1/14 个有
- `Int` —— 1/14 个有
- `JjkText` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `LoadImage` —— 1/14 个有
- `MaskPreview` —— 1/14 个有
- `Sa2VANodeTpl` —— 1/14 个有
- `SaveAudioMP3` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `easy mathInt` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
