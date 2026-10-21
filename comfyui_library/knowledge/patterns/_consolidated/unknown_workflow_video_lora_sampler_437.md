---
name: unknown_workflow_video_lora_sampler_437
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8108
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Primitive integer [Crystools], RH_LLMAPI_NODE, StringReplace, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy anythingIndexSwitch, easy showAnything]
problems: []
missing: [MathExpression|pysssss, Primitive integer [Crystools], Text Multiline, easy anythingIndexSwitch]
members: [视频生成/图生视频/1989534940729626625.json, 视频生成/图生视频/1989309256367304706.json, 视频生成/图生视频/1950590406721490945.json, 视频生成/文生视频/1971495513445089282.json, 视频生成/文生视频/1950544574634708994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_437

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1989534940729626625.json、视频生成/图生视频/1989309256367304706.json、视频生成/图生视频/1950590406721490945.json、视频生成/文生视频/1971495513445089282.json、视频生成/文生视频/1950544574634708994.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `RH_LLMAPI_NODE`
- `StringReplace`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/5 个有
- `WanVideoImageToVideoEncode` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `WanVideoEmptyEmbeds` —— 2/5 个有
- `CR Upscale Image` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、Primitive integer [Crystools]、Text Multiline、easy anythingIndexSwitch
