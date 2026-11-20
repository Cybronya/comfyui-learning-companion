---
name: unknown_workflow_video_lora_sampler_531
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.68975
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, CreateCFGScheduleFloatList, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/04-07-01-WAN2.2-数字人-InfiniteTalk-单人_1990969342198226945.json, 数字人/数字人/04-07-02-WAN2.2-数字人-InfiniteiTalk+UNI3C_1990969387870003201.json, 视频生成/图生视频/MultiTalk+Wan2.2（高低噪）加速版数字人V1（人物不动版UNI3C运镜）_1955533790640836610.json, 视频生成/图生视频/MultiTalk单人+Wan2.2(低)+Sigma调度KJ加速V4（全身动态版UNI3C运镜）_1955521619805421569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_531

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/04-07-01-WAN2.2-数字人-InfiniteTalk-单人_1990969342198226945.json、数字人/数字人/04-07-02-WAN2.2-数字人-InfiniteiTalk+UNI3C_1990969387870003201.json、视频生成/图生视频/MultiTalk+Wan2.2（高低噪）加速版数字人V1（人物不动版UNI3C运镜）_1955533790640836610.json、视频生成/图生视频/MultiTalk单人+Wan2.2(低)+Sigma调度KJ加速V4（全身动态版UNI3C运镜）_1955521619805421569.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/4 个有
- `WanVideoUni3C_embeds` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `Anything Everywhere` —— 2/4 个有
- `EmptyImage` —— 2/4 个有
- `FloatConstant` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `JWIntegerToString` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `Primitive string [Crystools]` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `FloatToSigmas` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `StringToFloatList` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
