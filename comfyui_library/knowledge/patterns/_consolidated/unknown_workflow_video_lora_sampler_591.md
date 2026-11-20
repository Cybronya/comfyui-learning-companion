---
name: unknown_workflow_video_lora_sampler_591
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9326
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk-超长时长数字人_1958367702521954306.json, 数字人/数字人/Infinitetalk_单人图片对口型_1961266591587614722.json, 数字人/数字人/Infinitetalk单人对口型数字人_1958118629235707906.json, 数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json, 视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_591

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/Infinitetalk-超长时长数字人_1958367702521954306.json、数字人/数字人/Infinitetalk_单人图片对口型_1961266591587614722.json、数字人/数字人/Infinitetalk单人对口型数字人_1958118629235707906.json、数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json、视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `CR Integer To String` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PreviewAudio` —— 3/5 个有
- `WanVideoImageToVideoMultiTalk` —— 3/5 个有
- `ttN int` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `CreateCFGScheduleFloatList` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `String Literal` —— 2/5 个有
- `WanVideoImageToVideoEncode` —— 2/5 个有
- `WanVideoSetBlockSwap` —— 2/5 个有
- `WanVideoSetLoRAs` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `Audio Duration (mtb)` —— 1/5 个有
- `Int` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SaveAudio` —— 1/5 个有
- `SaveLatent` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
