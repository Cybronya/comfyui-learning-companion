---
name: unknown_workflow_video_lora_sampler_878
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.988667
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Multitalk--唱歌数字人_1936361924722593793.json, 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json, 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V2.0_1968840482644217858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_878

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Multitalk--唱歌数字人_1936361924722593793.json、视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json、视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V2.0_1968840482644217858.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ImageFromBatch+` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoBlockSwap` —— 2/3 个有
- `WanVideoImageToVideoMultiTalk` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CreateCFGScheduleFloatList` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `JWIntegerToString` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `WanVideoImageToVideoEncode` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
