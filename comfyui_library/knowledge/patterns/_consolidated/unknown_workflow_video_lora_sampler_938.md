---
name: unknown_workflow_video_lora_sampler_938
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8785
common_nodes: [ACE_AudioCrop, AudioSeparation, DWPreprocessor, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatch, ImageResizeKJv2, Int, JWInteger, LoadAudio, LoadImage, LoadLynxResampler, LoadWanVideoT5TextEncoder, LynxEncodeFaceIP, LynxInsightFaceCrop, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, SimpleMath+, String Literal, VHS_BatchManager, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, Wav2VecModelLoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy seed, floatToText _O]
problems: []
missing: [ACE_AudioCrop, MathExpression|pysssss, SimpleMath+, String Literal, easy batchAnything, easy forLoopEnd, easy forLoopStart, floatToText _O, easy seed]
members: [视频生成/文生视频/1976202797450428418.json, 视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_2072999512521875456.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_938

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1976202797450428418.json、视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_2072999512521875456.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_AudioCrop`
- `AudioSeparation`
- `DWPreprocessor`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatch`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `LoadAudio`
- `LoadImage`
- `LoadLynxResampler`
- `LoadWanVideoT5TextEncoder`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `SimpleMath+`
- `String Literal`
- `VHS_BatchManager`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`
- `floatToText _O`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ACE_AudioCrop、MathExpression|pysssss、SimpleMath+、String Literal、easy batchAnything
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
