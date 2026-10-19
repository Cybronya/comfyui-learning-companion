---
name: unknown_workflow_video_lora_sampler_693
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.676333
common_nodes: [CreateCFGScheduleFloatList, GetNode, HuMoEmbeds, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: [CR Prompt Text]
members: [视频生成/文生视频/1968587379978186753.json, 视频生成/文生视频/1966946187645476866.json, 视频生成/文生视频/1967497065762840577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_693

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1968587379978186753.json、视频生成/文生视频/1966946187645476866.json、视频生成/文生视频/1967497065762840577.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetNode`
- `HuMoEmbeds`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `JWInteger` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
