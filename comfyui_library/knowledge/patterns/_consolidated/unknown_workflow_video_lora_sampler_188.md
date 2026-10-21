---
name: unknown_workflow_video_lora_sampler_188
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9114
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2017911981818253314.json, 视频生成/图生视频/2046206194833952769.json, 视频生成/图生视频/2014217620324618242.json, 视频生成/图生视频/1963873192061521922.json, 视频生成/图生视频/1949391348926971905.json, 视频生成/图生视频/1951564039392579586.json, 视频生成/图生视频/1950383603089891330.json, 视频生成/图生视频/1956914143121039362.json, 视频生成/图生视频/2032825101573431298.json, 视频生成/图生视频/1950400282711736322.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_188

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2017911981818253314.json、视频生成/图生视频/2046206194833952769.json、视频生成/图生视频/2014217620324618242.json、视频生成/图生视频/1963873192061521922.json、视频生成/图生视频/1949391348926971905.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `WanVideoSetBlockSwap` —— 7/10 个有
- `WanVideoSetLoRAs` —— 7/10 个有
- `GetImageSizeAndCount` —— 6/10 个有
- `INTConstant` —— 4/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `ImageResize+` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `CLIPVisionLoader` —— 1/10 个有
- `DF_Integer` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `SeargePromptText` —— 1/10 个有
- `ShowText` —— 1/10 个有
- `WanVideoLoraSelectMulti` —— 1/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
