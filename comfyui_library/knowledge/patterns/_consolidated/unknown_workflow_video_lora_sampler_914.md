---
name: unknown_workflow_video_lora_sampler_914
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.88
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, CreateCFGScheduleFloatList, DownloadAndLoadWav2VecModel, Float, GetImageRangeFromBatch, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadAudio, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SaveAudio, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTextEncodeCached, WanVideoVAELoader, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple]
problems: []
missing: []
members: [视频生成/文生视频/(Pro Max版)完爆OVI文生视频带配音数字人无限时长工作流--48G版_1975469825285820418.json, 视频生成/文生视频/(Pro高质量)跨模态仿OVI无限时长文生视频含配音数字人工作流V1（支持中文）_1975180560664498177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_914

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/(Pro Max版)完爆OVI文生视频带配音数字人无限时长工作流--48G版_1975469825285820418.json、视频生成/文生视频/(Pro高质量)跨模态仿OVI无限时长文生视频含配音数字人工作流V1（支持中文）_1975180560664498177.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadWav2VecModel`
- `Float`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SaveAudio`
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
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSGenerateSimple`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
