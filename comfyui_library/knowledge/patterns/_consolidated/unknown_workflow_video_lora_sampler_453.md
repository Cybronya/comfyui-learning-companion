---
name: unknown_workflow_video_lora_sampler_453
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8226
common_nodes: [DownloadAndLoadWav2VecModel, ImageFromBatch+, Int, JWInteger, LoadAudio, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, SetNode, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/T2V+lynx+InfiniteTalk+脸部参考+超强一致性_1977182802045214722.json, 数字人/数字人/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977645629725908994.json, 数字人/数字人/顶级唱歌演讲数字人T2V+lynx配合InfiniteTalk_1977047731871064066.json, 视频生成/文生视频/(生产力)-T2V+lynx+InfiniteTalk+脸部参考+超强一致性V2_1977531647312711681.json, 视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_453

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/T2V+lynx+InfiniteTalk+脸部参考+超强一致性_1977182802045214722.json、数字人/数字人/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977645629725908994.json、数字人/数字人/顶级唱歌演讲数字人T2V+lynx配合InfiniteTalk_1977047731871064066.json、视频生成/文生视频/(生产力)-T2V+lynx+InfiniteTalk+脸部参考+超强一致性V2_1977531647312711681.json、视频生成/文生视频/Wan2.1_T2V_lynx+InfiniteTalk数字人_1977002957059301377.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `DownloadAndLoadWav2VecModel`
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
- `AudioCrop` —— 4/5 个有
- `AudioSeparation` —— 4/5 个有
- `CR Integer To String` —— 4/5 个有
- `CR Text` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `ImageResize+` —— 4/5 个有
- `ImpactSwitch` —— 4/5 个有
- `RH_LLMAPI_NODE` —— 4/5 个有
- `SaveAudio` —— 4/5 个有
- `SoundFlow_GetLength` —— 4/5 个有
- `Text Concatenate` —— 4/5 个有
- `ToInt` —— 4/5 个有
- `Wan22PromptSelector` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `MelBandRoFormerModelLoader` —— 1/5 个有
- `MelBandRoFormerSampler` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `VideoCombine_Adv` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
