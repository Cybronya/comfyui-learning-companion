---
name: unknown_workflow_video_lora_sampler_348
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.731
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadAudio, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: [ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple, CR Prompt Text]
members: [视频生成/图生视频/1975546329931845634.json, 视频生成/文生视频/(Pro Max版)完爆OVI文生视频带配音数字人无限时长工作流--48G版_1975469825285820418.json, 视频生成/文生视频/(Pro高质量)跨模态仿OVI无限时长文生视频含配音数字人工作流V1（支持中文）_1975180560664498177.json, 视频生成/文生视频/03-10-08-WAN2.1-数字人-Lynx-免训练一致性ID+InfiniteTalk_1989939301351911425.json, 视频生成/文生视频/1975450428768956418.json, 视频生成/文生视频/1975546329931845634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_348

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1975546329931845634.json、视频生成/文生视频/(Pro Max版)完爆OVI文生视频带配音数字人无限时长工作流--48G版_1975469825285820418.json、视频生成/文生视频/(Pro高质量)跨模态仿OVI无限时长文生视频含配音数字人工作流V1（支持中文）_1975180560664498177.json、视频生成/文生视频/03-10-08-WAN2.1-数字人-Lynx-免训练一致性ID+InfiniteTalk_1989939301351911425.json、视频生成/文生视频/1975450428768956418.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `ImageFromBatch+` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `SaveAudio` —— 5/6 个有
- `WanVideoTextEncodeCached` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `easy downloadIndexTTSAndLoadModel` —— 5/6 个有
- `easy indexTTSGenerateSimple` —— 5/6 个有
- `LoadLynxResampler` —— 4/6 个有
- `LynxEncodeFaceIP` —— 4/6 个有
- `LynxInsightFaceCrop` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `WanVideoAddLynxEmbeds` —— 4/6 个有
- `WanVideoExtraModelSelect` —— 4/6 个有
- `WanVideoLoraSelectMulti` —— 4/6 个有
- `INTConstant` —— 3/6 个有
- `LoadWanVideoT5TextEncoder` —— 3/6 个有
- `WanVideoTextEncode` —— 3/6 个有
- `CreateCFGScheduleFloatList` —— 2/6 个有
- `Float` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `WanVideoScheduler` —— 2/6 个有
- `WanVideoSigmaToStep` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `AudioCrop` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、LayerUtility: PurgeVRAM V2、MathExpression|pysssss
