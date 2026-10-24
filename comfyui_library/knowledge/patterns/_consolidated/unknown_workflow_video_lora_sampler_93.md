---
name: unknown_workflow_video_lora_sampler_93
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.906062
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 图生视频工作量_1974850739472306178.json, 视频生成/图生视频/wan2.2 图生视频，kj版8步加速_1960977035327934465.json, 视频生成/图生视频/wan2.2-首尾帧_2014248439579676673.json, 视频生成/图生视频/wan2.2Pro首尾帧生成视频工作流_2013862124266721282.json, 视频生成/图生视频/wan2.2首尾帧视频工作流_2013162152139431937.json, 视频生成/图生视频/wan2.2首尾帧，kj加速版_1953644450683736065.json, 视频生成/图生视频/【Wan2.2首尾帧】最新万相14B FLF2V 首尾帧视频加速版 图生视频_1972187694434545666.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048571694041800706.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048653140999806977.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048940040620875778.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2069594425340284930.json, 视频生成/图生视频/建筑-wan2.2单帧视频工作流_2022682129682931714.json, 视频生成/图生视频/首尾帧视频 wan2.2_2018548235928870914.json, 视频生成/文生视频/02 Wan2.2 Smooth Mix I2V首尾帧生视频+全节点注释_2055549969884565506.json, 视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json, 视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_93

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/wan2.2 图生视频工作量_1974850739472306178.json、视频生成/图生视频/wan2.2 图生视频，kj版8步加速_1960977035327934465.json、视频生成/图生视频/wan2.2-首尾帧_2014248439579676673.json、视频生成/图生视频/wan2.2Pro首尾帧生成视频工作流_2013862124266721282.json、视频生成/图生视频/wan2.2首尾帧视频工作流_2013162152139431937.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 16 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 15/16 个有
- `JWInteger` —— 15/16 个有
- `WanVideoClipVisionEncode` —— 15/16 个有
- `WanVideoSetLoRAs` —— 15/16 个有
- `ImageResize+` —— 14/16 个有
- `LoadWanVideoClipTextEncoder` —— 14/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/16 个有
- `LayerUtility: PurgeVRAM` —— 10/16 个有
- `SetNode` —— 10/16 个有
- `GetNode` —— 9/16 个有
- `ImageLoader` —— 9/16 个有
- `LoadImage` —— 7/16 个有
- `CreateCFGScheduleFloatList` —— 6/16 个有
- `CR Prompt Text` —— 4/16 个有
- `GetImageSizeAndCount` —— 3/16 个有
- `SimpleMath+` —— 2/16 个有
- `CLIPVisionLoader` —— 1/16 个有
- `Int` —— 1/16 个有
- `MathExpression|pysssss` —— 1/16 个有
- `TrimVideoLatent` —— 1/16 个有
- `easy seed` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
