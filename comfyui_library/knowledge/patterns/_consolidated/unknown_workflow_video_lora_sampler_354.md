---
name: unknown_workflow_video_lora_sampler_354
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9275
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2 Upskirt_1964201625864818690.json, 视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json, 视频生成/图生视频/WAN2.2-8-12极速图生视频自用（三川V：yanshao1888）_1955263438596423682.json, 视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json, 视频生成/图生视频/WAN2.2跨镜头切换_1963945783164850177.json, 视频生成/图生视频/Wan2.2 Kj-图生视频工作流_1956914143121039362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_354

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/WAN2.2 Upskirt_1964201625864818690.json、视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json、视频生成/图生视频/WAN2.2-8-12极速图生视频自用（三川V：yanshao1888）_1955263438596423682.json、视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json、视频生成/图生视频/WAN2.2跨镜头切换_1963945783164850177.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `WanVideoSLG` —— 3/6 个有
- `easy positive` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `easy humanSegmentation` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
