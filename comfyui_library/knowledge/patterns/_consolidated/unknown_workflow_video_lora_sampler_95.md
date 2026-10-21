---
name: unknown_workflow_video_lora_sampler_95
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.699313
common_nodes: [LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [ImageFromBatch+, CR Prompt Text, GPENO Face Restoration, CR Text, FancyTimerNode]
members: [视频生成/图生视频/1977229583860801538.json, 视频生成/文生视频/1975435330138542082.json, 视频生成/文生视频/1975438784533762049.json, 视频生成/文生视频/1975446783209902081.json, 视频生成/文生视频/1975835025436487681.json, 视频生成/文生视频/1975850238516793345.json, 视频生成/文生视频/1975858725598662658.json, 视频生成/文生视频/1975861201806692353.json, 视频生成/文生视频/1975861887592214529.json, 视频生成/文生视频/1975939269380452353.json, 视频生成/文生视频/1976584449313869825.json, 视频生成/文生视频/1976840032592052226.json, 视频生成/文生视频/lynx-VACE-ID一致性图生视频_2072999522797920256.json, 视频生成/文生视频/lynx-VACE-ID一致性图生视频（独立垫图）_2072999522294603776.json, 视频生成/文生视频/lynx-VACE-ID一致性首尾帧_2072999521757732864.json, 视频生成/文生视频/lynx-VACE-ID换脸后图生视频_2072999521283776512.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/1977229583860801538.json、视频生成/文生视频/1975435330138542082.json、视频生成/文生视频/1975438784533762049.json、视频生成/文生视频/1975446783209902081.json、视频生成/文生视频/1975835025436487681.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 16 个 workflow 都包含：
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 13/16 个有
- `GetImageSizeAndCount` —— 11/16 个有
- `RH_Captioner` —— 9/16 个有
- `easy showAnything` —— 9/16 个有
- `INTConstant` —— 8/16 个有
- `ImageResizeKJ` —— 8/16 个有
- `WanVideoVACEEncode` —— 8/16 个有
- `WanVideoVACEModelSelect` —— 8/16 个有
- `WanVideoVACEStartToEndFrame` —— 8/16 个有
- `GetNode` —— 7/16 个有
- `SetNode` —— 7/16 个有
- `ImageConcatMulti` —— 6/16 个有
- `CR Prompt Text` —— 3/16 个有
- `CR Text` —— 3/16 个有
- `ImageFromBatch+` —— 3/16 个有
- `GPENO Face Restoration` —— 2/16 个有
- `ReActorFaceSwap` —— 2/16 个有
- `FancyTimerNode` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、CR Prompt Text、GPENO Face Restoration、CR Text、FancyTimerNode
