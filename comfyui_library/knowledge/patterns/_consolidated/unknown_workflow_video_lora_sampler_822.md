---
name: unknown_workflow_video_lora_sampler_822
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.627
common_nodes: [Bjornulf_ShowStringText, CLIPLoader, CR Text, CreateCFGScheduleFloatList, GetNode, INTConstant, ImageResizeKJv2, Int2Any_AS, LoadImage, LoadWanVideoT5TextEncoder, RH_LLMAPI_NODE, SetNode, ShowText, SimpleCondition+, SimpleMath+, String, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/1952150601243283457.json, 视频生成/图生视频/1950148993163640833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_822

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1952150601243283457.json、视频生成/图生视频/1950148993163640833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowStringText`
- `CLIPLoader`
- `CR Text`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `Int2Any_AS`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RH_LLMAPI_NODE`
- `SetNode`
- `ShowText`
- `SimpleCondition+`
- `SimpleMath+`
- `String`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LoadWanVideoClipTextEncoder` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
