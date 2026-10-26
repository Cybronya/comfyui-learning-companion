---
name: unknown_workflow_video_lora_sampler_384
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.740333
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json, 数字人/数字人/Infinitetalk视频对口型数字人_1958366624854261762.json, 数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json, 数字人/数字人/无限时长音乐数字人-InfiniteTalk单人视频到视频_1958187031639822338.json, 视频生成/图生视频/wan2.1-InfiniTetalk-音频+图像=数字人_1967501356460335105.json, 视频生成/图生视频/视频对口型_1971064636227391489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_384

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/wan2.1-InfiniTetalk  音频+视频=数字人_1967763738742984706.json、数字人/数字人/Infinitetalk视频对口型数字人_1958366624854261762.json、数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json、数字人/数字人/无限时长音乐数字人-InfiniteTalk单人视频到视频_1958187031639822338.json、视频生成/图生视频/wan2.1-InfiniTetalk-音频+图像=数字人_1967501356460335105.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 5/6 个有
- `AudioSeparation` —— 5/6 个有
- `GetImageRangeFromBatch` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `WanVideoEncode` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `MelBandRoFormerModelLoader` —— 3/6 个有
- `MelBandRoFormerSampler` —— 3/6 个有
- `PreviewAudio` —— 3/6 个有
- `Wav2VecModelLoader` —— 3/6 个有
- `Fast Bypasser (rgthree)` —— 2/6 个有
- `JWIntegerToString` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `Int` —— 1/6 个有
- `SoundFlow_GetLength` —— 1/6 个有
- `Switch any [Crystools]` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `easy convertAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
