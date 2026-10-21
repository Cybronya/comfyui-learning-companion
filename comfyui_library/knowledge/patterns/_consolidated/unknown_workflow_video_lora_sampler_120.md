---
name: unknown_workflow_video_lora_sampler_120
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.635231
common_nodes: [GetNode, ImageConcatMulti, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, SetNode, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [CR Text, ImageFromBatch+, MathExpression|pysssss, Text Concatenate]
members: [图片生成/文生图/AI大宗主人物一致性文生视频_2013973664265408514.json, 视频生成/图生视频/1975446783209902081.json, 视频生成/图生视频/1976624751336660994.json, 视频生成/图生视频/1977298137419272194.json, 视频生成/图生视频/1975848455060983809.json, 视频生成/图生视频/1977061045816709121.json, 视频生成/图生视频/1980064272694808577.json, 视频生成/图生视频/1978799084448419842.json, 视频生成/文生视频/1976486490379296769.json, 视频生成/文生视频/1976851496895758338.json, 视频生成/文生视频/1977715877644750849.json, 视频生成/文生视频/Wan2.1_T2V_lynx文生视频人物一致性_2070426739108564994.json, 视频生成/文生视频/文加图生视频人物一致性（超还原）Wan2.1_T2V_2032378252462919682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/AI大宗主人物一致性文生视频_2013973664265408514.json、视频生成/图生视频/1975446783209902081.json、视频生成/图生视频/1976624751336660994.json、视频生成/图生视频/1977298137419272194.json、视频生成/图生视频/1975848455060983809.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 13 个 workflow 都包含：
- `GetNode`
- `ImageConcatMulti`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `SetNode`
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
- `PreviewImage` —— 12/13 个有
- `ImageFromBatch+` —— 8/13 个有
- `WanVideoTorchCompileSettings` —— 8/13 个有
- `CR Text` —— 7/13 个有
- `ImpactSwitch` —— 7/13 个有
- `JWInteger` —— 7/13 个有
- `RH_LLMAPI_NODE` —— 7/13 个有
- `Text Concatenate` —— 7/13 个有
- `Wan22PromptSelector` —— 7/13 个有
- `MathExpression|pysssss` —— 6/13 个有
- `easy showAnything` —— 6/13 个有
- `CR Prompt Text` —— 2/13 个有
- `FancyTimerNode` —— 1/13 个有
- `GetImageSizeAndCount` —— 1/13 个有
- `JjkText` —— 1/13 个有
- `Joy_caption` —— 1/13 个有
- `Joy_caption_load` —— 1/13 个有
- `Primitive integer [Crystools]` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `SeedVR2` —— 1/13 个有
- `SeedVR2BlockSwap` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、ImageFromBatch+、MathExpression|pysssss、Text Concatenate
