---
name: unknown_workflow_video_lora_sampler_36
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.915214
common_nodes: [INTConstant, ImageResize+, JWInteger, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json, 图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json, 图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json, 数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2033734899114446849.json, 数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json, 视频生成/图生视频/(KJ FPS16版)WAN2.2首尾帧FLF2V超级加速版工作流V1_1952002049745563650.json, 视频生成/图生视频/(KJ版稳定态FPS16)WAN2.2 INP最强自动预测首尾帧极速版V1_1956601025757151233.json, 视频生成/图生视频/(KJ版高动态FPS24)WAN2.2 INP最强自动预测首尾帧极速版V1_1956583088841261058.json, 视频生成/图生视频/(KJ高动态版FPS24)WAN2.2目前最强首尾帧超级加速版工作流V1_1952012888850509826.json, 视频生成/图生视频/WAN2.2 INP最强自动预测首尾帧极速版V1 浮云（次用）_1996851492734869506.json, 视频生成/图生视频/WAN2.2图生视频KJ8步_1952320153679794177.json, 视频生成/图生视频/WAN2.2首尾帧_1963913944572248066.json, 视频生成/图生视频/wan2.2-首尾帧_2014248439579676673.json, 视频生成/图生视频/wan2.2Pro首尾帧生成视频工作流_2013862124266721282.json, 视频生成/图生视频/【Wan2.2首尾帧】最新万相14B FLF2V 首尾帧视频加速版 图生视频_1972187694434545666.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048571694041800706.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048653140999806977.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048940040620875778.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2069594425340284930.json, 视频生成/图生视频/首尾帧 图生视频 加速版-wan2.2-kj版_2021050024263684097.json, 视频生成/图生视频/首尾帧 生视频 kj加速版 wan2.2万相4步加速视频 Rapid AllInOne 2图生视频_2033052828255657985.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2011275998205054977.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2013608630863536130.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2014220447117746178.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2020055419988746242.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2054450000423333890.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2068009866219835393.json, 视频生成/图生视频/首尾帧视频 wan2.2_2018548235928870914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json、图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json、图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json、数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2033734899114446849.json、数字人/数字人/首尾帧 图生视频 加速版-wan2.2-kj版_2037374410901954561.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 28 个 workflow 都包含：
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
- `LayerUtility: PurgeVRAM` —— 26/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 21/28 个有
- `GetNode` —— 20/28 个有
- `ImageLoader` —— 20/28 个有
- `SetNode` —— 20/28 个有
- `CR Prompt Text` —— 8/28 个有
- `CreateCFGScheduleFloatList` —— 8/28 个有
- `LoadImage` —— 8/28 个有
- `GetImageSizeAndCount` —— 7/28 个有
- `AddLabel` —— 6/28 个有
- `EmptyImage` —— 6/28 个有
- `ImageConcatMulti` —— 6/28 个有
- `MathExpression|pysssss` —— 2/28 个有
- `Fast Groups Bypasser (rgthree)` —— 1/28 个有
- `PreviewImage` —— 1/28 个有
- `PrimitiveBoolean` —— 1/28 个有
- `easy ifElse` —— 1/28 个有
- `easy int` —— 1/28 个有
- `easy seed` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
