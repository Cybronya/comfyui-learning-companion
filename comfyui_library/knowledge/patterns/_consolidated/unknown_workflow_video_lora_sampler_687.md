---
name: unknown_workflow_video_lora_sampler_687
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.726667
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageFromBatch+, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, PreviewImage, SetNode, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoExtraModelSelect, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/03-10-08-WAN2.1-数字人-Lynx-免训练一致性ID+InfiniteTalk_1989939301351911425.json, 视频生成/文生视频/Lynx跨模态音频ID一致性数字人视频V1（横版）_1975450428768956418.json, 视频生成/文生视频/Lynx跨模态音频ID一致性数字人视频V1（竖版）_1975546329931845634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_687

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/03-10-08-WAN2.1-数字人-Lynx-免训练一致性ID+InfiniteTalk_1989939301351911425.json、视频生成/文生视频/Lynx跨模态音频ID一致性数字人视频V1（横版）_1975450428768956418.json、视频生成/文生视频/Lynx跨模态音频ID一致性数字人视频V1（竖版）_1975546329931845634.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoExtraModelSelect`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `WanVideoTextEncodeCached` —— 2/3 个有
- `easy downloadIndexTTSAndLoadModel` —— 2/3 个有
- `easy indexTTSGenerateSimple` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Audio Duration (mtb)` —— 1/3 个有
- `AudioCrop` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `JWIntegerToString` —— 1/3 个有
- `LoadWanVideoT5TextEncoder` —— 1/3 个有
- `WanVideoTextEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
