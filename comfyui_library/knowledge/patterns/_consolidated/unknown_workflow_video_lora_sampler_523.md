---
name: unknown_workflow_video_lora_sampler_523
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9335
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2 Upskirt_1964201625864818690.json, 视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json, 视频生成/图生视频/WAN2.2-8-12极速图生视频自用（三川V：yanshao1888）_1955263438596423682.json, 视频生成/图生视频/WAN2.2跨镜头切换_1963945783164850177.json, 视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json, 视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_523

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/WAN2.2 Upskirt_1964201625864818690.json、视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json、视频生成/图生视频/WAN2.2-8-12极速图生视频自用（三川V：yanshao1888）_1955263438596423682.json、视频生成/图生视频/WAN2.2跨镜头切换_1963945783164850177.json、视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json…）

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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 5/6 个有
- `WanVideoImageToVideoEncode` —— 5/6 个有
- `easy positive` —— 5/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `WanVideoSLG` —— 3/6 个有
- `SimpleMath+` —— 2/6 个有
- `easy seed` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `WanVideoEmptyEmbeds` —— 1/6 个有
- `easy humanSegmentation` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
