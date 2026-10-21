---
name: unknown_workflow_video_lora_sampler_568
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.732333
common_nodes: [DownloadAndLoadWav2VecModel, GetNode, ImageConcatMulti, ImageFromBatch+, Int, JWInteger, LoadAudio, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, SetNode, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [CR Integer To String, CR Text, ImageFromBatch+, MathExpression|pysssss, Text Concatenate, easy cleanGpuUsed, ImageResize+]
members: [图片生成/文生图/1977182802045214722.json, 视频生成/文生视频/(生产力)-T2V+lynx+InfiniteTalk+脸部参考+超强一致性V2_1977531647312711681.json, 视频生成/文生视频/1977002957059301377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_568

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1977182802045214722.json、视频生成/文生视频/(生产力)-T2V+lynx+InfiniteTalk+脸部参考+超强一致性V2_1977531647312711681.json、视频生成/文生视频/1977002957059301377.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `Int`
- `JWInteger`
- `LoadAudio`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `AudioSeparation` —— 2/3 个有
- `CR Integer To String` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `SoundFlow_GetLength` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `ToInt` —— 2/3 个有
- `Wan22PromptSelector` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `VideoCombine_Adv` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Integer To String、CR Text、ImageFromBatch+、MathExpression|pysssss、Text Concatenate
