---
name: unknown_workflow_video_lora_sampler_95
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8846
common_nodes: [INTConstant, ImageResize+, JWInteger, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json, 图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json, 图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json, 图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json, 图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json, 图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json, 视频生成/图生视频/(KJ FPS16版)WAN2.2首尾帧FLF2V超级加速版工作流V1_1952002049745563650.json, 视频生成/图生视频/(KJ版稳定态FPS16)WAN2.2 INP最强自动预测首尾帧极速版V1_1956601025757151233.json, 视频生成/图生视频/(KJ版高动态FPS24)WAN2.2 INP最强自动预测首尾帧极速版V1_1956583088841261058.json, 视频生成/图生视频/(KJ高动态版FPS24)WAN2.2目前最强首尾帧超级加速版工作流V1_1952012888850509826.json, 视频生成/图生视频/WAN2.2 INP最强自动预测首尾帧极速版V1 浮云（次用）_1996851492734869506.json, 视频生成/图生视频/WAN2.2-首尾帧视频工作流_1981935370910744577.json, 视频生成/图生视频/WAN2.2图生视频KJ8步_1952320153679794177.json, 视频生成/图生视频/WAN2.2毛茸茸首尾帧动画_1978297110992969730.json, 视频生成/图生视频/WAN2.2首尾帧_1963913944572248066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Wan2.2首尾帧KJ8步_1952288273785933825.json、图片生成/图生图/首尾帧-wan2.2-kj版_1988497426770214913.json、图片生成/图生图/首尾帧-wan2.2-kj版_2029756695303430145.json、图片生成/图生图/首尾帧-wan2.2版工作流_2033445320134238210.json、图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
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
- `LayerUtility: PurgeVRAM` —— 14/15 个有
- `CR Prompt Text` —— 12/15 个有
- `CreateCFGScheduleFloatList` —— 12/15 个有
- `LoadImage` —— 12/15 个有
- `AddLabel` —— 6/15 个有
- `EmptyImage` —— 6/15 个有
- `GetImageSizeAndCount` —— 6/15 个有
- `ImageConcatMulti` —— 6/15 个有
- `GetNode` —— 4/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/15 个有
- `SetNode` —— 4/15 个有
- `SimpleMath+` —— 4/15 个有
- `easy cleanGpuUsed` —— 4/15 个有
- `ImageLoader` —— 3/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `Float` —— 1/15 个有
- `MathExpression|pysssss` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `PrimitiveBoolean` —— 1/15 个有
- `easy ifElse` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
