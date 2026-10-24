---
name: unknown_workflow_video_lora_sampler_345
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.748667
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Infinite Talk-数字人对口型唱歌（无限时长+高动态）-上传图片+视频_2007804749827022850.json, 视频生成/图生视频/Infinite Talk数字人唱歌（无限时长+高动态）_1969431253688721410.json, 视频生成/图生视频/Infinite talk数字人动态加强高版（Lightx2v+Rcm多重注意力机制）_1984675339228102657.json, 视频生成/图生视频/Infinite+talk数字人动态加强版_2001621659876507649.json, 视频生成/图生视频/数字人对口型唱歌-Infinite Talk_2050200100416311298.json, 音频生成/音频生成/Infinite Talk-对口型说话+唱歌无限时长+高动态_2021031552670507010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_345

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Infinite Talk-数字人对口型唱歌（无限时长+高动态）-上传图片+视频_2007804749827022850.json、视频生成/图生视频/Infinite Talk数字人唱歌（无限时长+高动态）_1969431253688721410.json、视频生成/图生视频/Infinite talk数字人动态加强高版（Lightx2v+Rcm多重注意力机制）_1984675339228102657.json、视频生成/图生视频/Infinite+talk数字人动态加强版_2001621659876507649.json、视频生成/图生视频/数字人对口型唱歌-Infinite Talk_2050200100416311298.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `ToInt` —— 5/6 个有
- `Display Int (rgthree)` —— 4/6 个有
- `SoundFlow_GetLength` —— 4/6 个有
- `Float` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `Int` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `AddLabel` —— 2/6 个有
- `JWFloat` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `CM_FloatToInt` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RH_GetAudioDuration` —— 1/6 个有
- `TTResolutionSelector` —— 1/6 个有
- `VHS_LoadAudioUpload` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy mathInt` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
