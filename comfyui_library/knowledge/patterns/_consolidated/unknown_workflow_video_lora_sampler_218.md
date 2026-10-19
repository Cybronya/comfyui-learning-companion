---
name: unknown_workflow_video_lora_sampler_218
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.887667
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1999023790376017922.json, 视频生成/图生视频/2073246385209700353.json, 视频生成/图生视频/2073246674415349762.json, 视频生成/图生视频/2015681612746330114.json, 视频生成/图生视频/1984675339228102657.json, 视频生成/图生视频/2007798909330001921.json, 视频生成/图生视频/2014643345397653506.json, 视频生成/图生视频/2014949900475174914.json, 视频生成/图生视频/1984917641024454657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_218

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1999023790376017922.json、视频生成/图生视频/2073246385209700353.json、视频生成/图生视频/2073246674415349762.json、视频生成/图生视频/2015681612746330114.json、视频生成/图生视频/1984675339228102657.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/9 个有
- `CR Prompt Text` —— 8/9 个有
- `GetImageSizeAndCount` —— 7/9 个有
- `JWInteger` —— 7/9 个有
- `JWFloat` —— 5/9 个有
- `LoadWanVideoT5TextEncoder` —— 5/9 个有
- `PreviewAny` —— 5/9 个有
- `WanVideoTextEncode` —— 5/9 个有
- `WanVideoTextEncodeCached` —— 4/9 个有
- `Anything Everywhere` —— 3/9 个有
- `Audio Duration (mtb)` —— 3/9 个有
- `MathExpression|pysssss` —— 3/9 个有
- `RH_GetAudioDuration` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `CR String To Number` —— 2/9 个有
- `Float` —— 2/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `Int` —— 2/9 个有
- `WanVideoEncode` —— 2/9 个有
- `Audio Cut (mtb)` —— 1/9 个有
- `ImageBatchMulti` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `PreviewAudio` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `ReverseImageBatch` —— 1/9 个有
- `ToInt` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
