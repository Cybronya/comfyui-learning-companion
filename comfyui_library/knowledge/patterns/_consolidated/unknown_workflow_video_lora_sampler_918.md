---
name: unknown_workflow_video_lora_sampler_918
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.912
common_nodes: [ACE_ImageGetSize, CreateCFGScheduleFloatList, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Primitive integer [Crystools], ResizeLongestToNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950095043170361345.json, 视频生成/图生视频/1950059888082903042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_918

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1950095043170361345.json、视频生成/图生视频/1950059888082903042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_ImageGetSize`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `ResizeLongestToNode`
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
- `AddLabel` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `JWStringConcat` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextConcat` —— 1/2 个有
- `Wan22PromptSelector` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
