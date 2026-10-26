---
name: unknown_workflow_video_lora_sampler_997
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9135
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Primitive integer [Crystools], VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/🦖KJ-Wan2.2-121帧高质量自动首尾帧_1950095043170361345.json, 视频生成/文生视频/通义万相wan2.2图生视频（kj加速版6步）  24G显卡可跑，2分钟5秒_1950433801442910210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_997

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/🦖KJ-Wan2.2-121帧高质量自动首尾帧_1950095043170361345.json、视频生成/文生视频/通义万相wan2.2图生视频（kj加速版6步）  24G显卡可跑，2分钟5秒_1950433801442910210.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_ImageGetSize` —— 1/2 个有
- `AddLabel` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ResizeLongestToNode` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
