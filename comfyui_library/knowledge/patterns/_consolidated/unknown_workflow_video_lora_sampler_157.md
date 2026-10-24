---
name: unknown_workflow_video_lora_sampler_157
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.799
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/(KJ版)Wan2.2 文生视频加速版V1（高级镜头运动）_1950219384603197442.json, 图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json, 视频生成/图生视频/(KJ版)Wan2.2 文生视频加速版V1（色调）_1950186803727876098.json, 视频生成/图生视频/(KJ版)Wan2.2 文生视频加速版V1（运动能力）_1950195066095714306.json, 视频生成/图生视频/DNR-WAN2.2 KJ 图生视频_1951706628657721345.json, 视频生成/图生视频/HeGenAI-N8N-Wan2.2图生视频加速版_1968577373975261186.json, 视频生成/图生视频/KJ wan2.2首尾帧+Lightx4step lora_2015424489110118402.json, 视频生成/图生视频/KJ-Wan2.2-6步加速图生视频_1949986819199909890.json, 视频生成/图生视频/KJ-Wan2.2-6步加速文生视频_1950060354116214786.json, 视频生成/图生视频/SP500-图生视频（wan2.2_KJ优化版） 最新开源wan2.2视频模型，高质量视频生成，_1950560356596961282.json, 视频生成/图生视频/最新WAN2.2 KJ版 图生视频加速版工作流_1976954244421046273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_157

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/(KJ版)Wan2.2 文生视频加速版V1（高级镜头运动）_1950219384603197442.json、图片生成/文生图/DNR-wan2.2文生视频-KJ版_1950229173782667265.json、视频生成/图生视频/(KJ版)Wan2.2 文生视频加速版V1（色调）_1950186803727876098.json、视频生成/图生视频/(KJ版)Wan2.2 文生视频加速版V1（运动能力）_1950195066095714306.json、视频生成/图生视频/DNR-WAN2.2 KJ 图生视频_1951706628657721345.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 10/11 个有
- `INTConstant` —— 9/11 个有
- `GetImageSizeAndCount` —— 8/11 个有
- `LoadImage` —— 7/11 个有
- `CR Prompt Text` —— 6/11 个有
- `ImageResizeKJv2` —— 6/11 个有
- `JWInteger` —— 6/11 个有
- `WanVideoImageToVideoEncode` —— 6/11 个有
- `WanVideoEmptyEmbeds` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `GetNode` —— 4/11 个有
- `SetNode` —— 4/11 个有
- `MathExpression|pysssss` —— 3/11 个有
- `WanVideoEasyCache` —— 3/11 个有
- `Int` —— 2/11 个有
- `Primitive integer [Crystools]` —— 2/11 个有
- `Text Multiline` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `Seed_` —— 1/11 个有
- `easy bookmark` —— 1/11 个有
- `easy imageSize` —— 1/11 个有
- `easy positive` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
