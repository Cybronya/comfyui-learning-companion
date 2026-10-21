---
name: unknown_workflow_video_lora_sampler_302
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.776571
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2007804749827022850.json, 视频生成/图生视频/1969431253688721410.json, 视频生成/图生视频/1984675339228102657.json, 视频生成/图生视频/2007798909330001921.json, 视频生成/图生视频/2014643345397653506.json, 视频生成/图生视频/2001621659876507649.json, 视频生成/图生视频/2050200100416311298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_302

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2007804749827022850.json、视频生成/图生视频/1969431253688721410.json、视频生成/图生视频/1984675339228102657.json、视频生成/图生视频/2007798909330001921.json、视频生成/图生视频/2014643345397653506.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
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
- `AudioCrop` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `JWInteger` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `JWFloat` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `ToInt` —— 4/7 个有
- `Display Int (rgthree)` —— 3/7 个有
- `Float` —— 3/7 个有
- `Int` —— 3/7 个有
- `SoundFlow_GetLength` —— 3/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `Audio Cut (mtb)` —— 1/7 个有
- `Audio Duration (mtb)` —— 1/7 个有
- `CM_FloatToInt` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RH_GetAudioDuration` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有
- `VHS_LoadAudioUpload` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
