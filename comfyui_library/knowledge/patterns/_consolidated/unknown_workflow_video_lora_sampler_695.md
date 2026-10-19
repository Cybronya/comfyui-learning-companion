---
name: unknown_workflow_video_lora_sampler_695
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.612
common_nodes: [GetNode, ImageConcatMulti, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, SetNode, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [ImageFromBatch+, MathExpression|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, CR Prompt Text, easy seed]
members: [视频生成/文生视频/1977371689770196993.json, 视频生成/文生视频/1977745156428496897.json, 视频生成/文生视频/2066055963360423936.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_695

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1977371689770196993.json、视频生成/文生视频/1977745156428496897.json、视频生成/文生视频/2066055963360423936.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `GetNode`
- `ImageConcatMulti`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
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
- `CR Prompt Text` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageFromBatch+` —— 2/3 个有
- `ImpactFloat` —— 2/3 个有
- `Int` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `QwenLoader` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `WanVideoPromptExtender` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `easy int` —— 2/3 个有
- `easy seed` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、MathExpression|pysssss、StringFunction|pysssss、easy anythingIndexSwitch、easy int
