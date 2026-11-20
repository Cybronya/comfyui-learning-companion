---
name: unknown_workflow_video_lora_sampler_140
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.861
common_nodes: [INTConstant, ImageResize+, JWInteger, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json, 图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json, 图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json, 数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2033734899114446849.json, 数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json, 视频生成/图生视频/(KJ FPS16版)WAN2.2首尾帧FLF2V超级加速版工作流V1_1952002049745563650.json, 视频生成/图生视频/(KJ版稳定态FPS16)WAN2.2 INP最强自动预测首尾帧极速版V1_1956601025757151233.json, 视频生成/图生视频/(KJ版高动态FPS24)WAN2.2 INP最强自动预测首尾帧极速版V1_1956583088841261058.json, 视频生成/图生视频/(KJ高动态版FPS24)WAN2.2目前最强首尾帧超级加速版工作流V1_1952012888850509826.json, 视频生成/图生视频/WAN2.2 INP最强自动预测首尾帧极速版V1 浮云（次用）_1996851492734869506.json, 视频生成/图生视频/WAN2.2图生视频KJ8步_1952320153679794177.json, 视频生成/图生视频/WAN2.2首尾帧_1963913944572248066.json, 视频生成/文生视频/02 Wan2.2 Smooth Mix I2V首尾帧生视频+全节点注释_2055549969884565506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_140

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json、图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json、图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json、数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2033734899114446849.json、数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `INTConstant`
- `ImageResize+`
- `JWInteger`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
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
- `LayerUtility: PurgeVRAM` —— 11/13 个有
- `CR Prompt Text` —— 8/13 个有
- `CreateCFGScheduleFloatList` —— 8/13 个有
- `LoadImage` —— 8/13 个有
- `AddLabel` —— 6/13 个有
- `EmptyImage` —— 6/13 个有
- `GetImageSizeAndCount` —— 6/13 个有
- `ImageConcatMulti` —— 6/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/13 个有
- `GetNode` —— 5/13 个有
- `ImageLoader` —— 5/13 个有
- `SetNode` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `PrimitiveBoolean` —— 1/13 个有
- `easy ifElse` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
