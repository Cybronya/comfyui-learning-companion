---
name: unknown_workflow_video_lora_sampler_522
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.703
common_nodes: [ImpactSwitch, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_NODE, ShowText|pysssss, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1954023918736855041.json, 视频生成/图生视频/1952256556761034753.json, 视频生成/图生视频/1972595555933302785.json, 视频生成/文生视频/1953992083726225410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_522

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1954023918736855041.json、视频生成/图生视频/1952256556761034753.json、视频生成/图生视频/1972595555933302785.json、视频生成/文生视频/1953992083726225410.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `ImpactSwitch`
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
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `WanVideoImageToVideoEncode` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `DF_Int_to_Float` —— 2/4 个有
- `FloatToSigmas` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `StringToFloatList` —— 2/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoClipVisionEncode` —— 1/4 个有
- `WanVideoEmptyEmbeds` —— 1/4 个有
- `WanVideoLoraSelectMulti` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
