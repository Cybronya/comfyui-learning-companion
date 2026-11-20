---
name: unknown_workflow_video_lora_sampler_171
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.683692
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json, 平台全量/Chinese_to_English_V2V_中英文视频翻译_2110251637825695746.json, 平台全量/Chinese_to_English_V2V_中英文视频翻译_2110256769690849282.json, 平台全量/Chinese_to_English_V2V_翻译口型同步_2109910499432423426.json, 平台全量/InfiniteTalk视频+音频对口型OK（优化版）_1958839912986521602.json, 平台全量/InfiniteTalk视频+音频对口型（优化版）_1958761510673805314.json, 平台全量/Infinitetalk视频对口型工作流-kj版（忠于视频）_2006233076115972097.json, 平台全量/KJ-Infinitetalk视频对口型工作流_2017043758298173441.json, 平台全量/视频编辑 视频对口型 音频驱动生视频 数字人+视频重绘 唱歌跳舞_2088442497033920514.json, 数字人/数字人/251229001.001🥳infinitetalk视频对口型_2005196834035433474.json, 数字人/数字人/Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1958282916373676034.json, 数字人/数字人/Infinitetalk视频对口型工作流-kj版_2004517190860767233.json, 数字人/数字人/视频对口型_2036369932333617153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_171

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json、平台全量/Chinese_to_English_V2V_中英文视频翻译_2110251637825695746.json、平台全量/Chinese_to_English_V2V_中英文视频翻译_2110256769690849282.json、平台全量/Chinese_to_English_V2V_翻译口型同步_2109910499432423426.json、平台全量/InfiniteTalk视频+音频对口型OK（优化版）_1958839912986521602.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 12/13 个有
- `ImageConcatMulti` —— 11/13 个有
- `ImageResizeKJv2` —— 11/13 个有
- `AudioCrop` —— 10/13 个有
- `AudioSeparation` —— 10/13 个有
- `Display Int (rgthree)` —— 9/13 个有
- `ImageBatchMulti` —— 9/13 个有
- `ReverseImageBatch` —— 9/13 个有
- `SimpleMath+` —— 9/13 个有
- `SoundFlow_GetLength` —— 9/13 个有
- `easy int` —— 9/13 个有
- `INTConstant` —— 8/13 个有
- `ToInt` —— 8/13 个有
- `MelBandRoFormerModelLoader` —— 4/13 个有
- `MelBandRoFormerSampler` —— 4/13 个有
- `Wav2VecModelLoader` —— 4/13 个有
- `ImpactInt` —— 3/13 个有
- `JWIntegerToString` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `LoadImage` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `ResizeAndPadImage` —— 2/13 个有
- `ttN int` —— 2/13 个有
- `Fast Bypasser (rgthree)` —— 1/13 个有
- `Int` —— 1/13 个有
- `JWFloatToInteger` —— 1/13 个有
- `PreviewAudio` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `SaveAudio` —— 1/13 个有
- `easy positive` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
