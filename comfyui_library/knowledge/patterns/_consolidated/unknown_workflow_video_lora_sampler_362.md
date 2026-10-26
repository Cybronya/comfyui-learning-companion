---
name: unknown_workflow_video_lora_sampler_362
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.905143
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2 Upskirt_1964201625864818690.json, 视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json, 视频生成/图生视频/WAN2.2-8-12极速图生视频自用（三川V：yanshao1888）_1955263438596423682.json, 视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json, 视频生成/图生视频/WAN2.2图生视频（KJ8步+可做数据集）_1958716775745667074.json, 视频生成/图生视频/WAN2.2跨镜头切换_1963945783164850177.json, 视频生成/文生视频/(KJ版)Wan2.2图生视频超级加速版V3（大幅度提高速度）_1950046289267441666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_362

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/WAN2.2 Upskirt_1964201625864818690.json、视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json、视频生成/图生视频/WAN2.2-8-12极速图生视频自用（三川V：yanshao1888）_1955263438596423682.json、视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json、视频生成/图生视频/WAN2.2图生视频（KJ8步+可做数据集）_1958716775745667074.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `WanVideoEnhanceAVideo` —— 3/7 个有
- `WanVideoSLG` —— 3/7 个有
- `easy positive` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `ImageFromBatch+` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `easy humanSegmentation` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
