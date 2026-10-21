---
name: unknown_workflow_video_lora_sampler_525
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93625
common_nodes: [GetImageSizeAndCount, INTConstant, ImageResizeKJv2, Int, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1951969407968948225.json, 视频生成/图生视频/1951996290366427137.json, 视频生成/图生视频/1952913426868858882.json, 视频生成/图生视频/1952709897437777921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_525

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1951969407968948225.json、视频生成/图生视频/1951996290366427137.json、视频生成/图生视频/1952913426868858882.json、视频生成/图生视频/1952709897437777921.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `CreateCFGScheduleFloatList` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `Bjornulf_ShowStringText` —— 2/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `JjkConcat` —— 2/4 个有
- `LTXVPromptEnhancer` —— 2/4 个有
- `LTXVPromptEnhancerLoader` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `TTP_text_mix` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
