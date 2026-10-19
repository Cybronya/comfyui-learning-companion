---
name: unknown_workflow_video_lora_sampler_376
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.817833
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Primitive integer [Crystools], Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [MathExpression|pysssss, Primitive integer [Crystools], Text Multiline, easy anythingIndexSwitch]
members: [视频生成/图生视频/1989534940729626625.json, 视频生成/图生视频/1989309256367304706.json, 视频生成/图生视频/1950590406721490945.json, 视频生成/文生视频/1971495513445089282.json, 视频生成/文生视频/1950544574634708994.json, 视频生成/文生视频/1950433801442910210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_376

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1989534940729626625.json、视频生成/图生视频/1989309256367304706.json、视频生成/图生视频/1950590406721490945.json、视频生成/文生视频/1971495513445089282.json、视频生成/文生视频/1950544574634708994.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
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

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 5/6 个有
- `StringReplace` —— 5/6 个有
- `easy anythingIndexSwitch` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `WanVideoImageToVideoEncode` —— 4/6 个有
- `GetNode` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `WanVideoEmptyEmbeds` —— 2/6 个有
- `CR Upscale Image` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、Primitive integer [Crystools]、Text Multiline、easy anythingIndexSwitch
