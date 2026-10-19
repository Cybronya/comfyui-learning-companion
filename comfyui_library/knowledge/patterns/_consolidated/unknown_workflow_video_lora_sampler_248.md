---
name: unknown_workflow_video_lora_sampler_248
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.883
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, ImageToMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddTTMLatents, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1990441820280807425.json, 视频生成/图生视频/1991157733022085121.json, 视频生成/图生视频/1990244516261228546.json, 视频生成/图生视频/1990327033626587137.json, 视频生成/图生视频/1990969622830718977.json, 视频生成/图生视频/1991333399692685313.json, 视频生成/图生视频/1990459550644002818.json, 视频生成/图生视频/1999381454922579970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_248

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1990441820280807425.json、视频生成/图生视频/1991157733022085121.json、视频生成/图生视频/1990244516261228546.json、视频生成/图生视频/1990327033626587137.json、视频生成/图生视频/1990969622830718977.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageToMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddTTMLatents`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `CLIPLoader` —— 1/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `VHS_SelectImages` —— 1/8 个有
- `WanVideoImageToVideoEncode_v2` —— 1/8 个有
- `WanVideoTextEmbedBridge` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
