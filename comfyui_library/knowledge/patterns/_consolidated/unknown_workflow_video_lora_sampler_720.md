---
name: unknown_workflow_video_lora_sampler_720
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.715
common_nodes: [ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_NODE, ShowText|pysssss, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2+14B 4步加速图生视频KJ_1954023918736855041.json, 视频生成/图生视频/【KJ版】Wan2.2加速图生视频-提示词智能扩写_1952256556761034753.json, 视频生成/图生视频/【KJ版】Wan2.2最强图生视频+智能扩写提示词_1972595555933302785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_720

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2+14B 4步加速图生视频KJ_1954023918736855041.json、视频生成/图生视频/【KJ版】Wan2.2加速图生视频-提示词智能扩写_1952256556761034753.json、视频生成/图生视频/【KJ版】Wan2.2最强图生视频+智能扩写提示词_1972595555933302785.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `DF_Int_to_Float` —— 1/3 个有
- `FloatToSigmas` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `StringToFloatList` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
