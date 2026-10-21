---
name: unknown_workflow_video_lora_sampler_81
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.909941
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1974850739472306178.json, 视频生成/图生视频/1960977035327934465.json, 视频生成/图生视频/2014248439579676673.json, 视频生成/图生视频/2013862124266721282.json, 视频生成/图生视频/2013162152139431937.json, 视频生成/图生视频/1953644450683736065.json, 视频生成/图生视频/1972187694434545666.json, 视频生成/图生视频/2048571694041800706.json, 视频生成/图生视频/2048653140999806977.json, 视频生成/图生视频/2048940040620875778.json, 视频生成/图生视频/2069594425340284930.json, 视频生成/图生视频/2022682129682931714.json, 视频生成/图生视频/2018548235928870914.json, 视频生成/文生视频/02 Wan2.2 Smooth Mix I2V首尾帧生视频+全节点注释_2055549969884565506.json, 视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json, 视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json, 视频生成/文生视频/首尾帧视频-WAN2.2高质量版_1980937502708158465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/1974850739472306178.json、视频生成/图生视频/1960977035327934465.json、视频生成/图生视频/2014248439579676673.json、视频生成/图生视频/2013862124266721282.json、视频生成/图生视频/2013162152139431937.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
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
- `INTConstant` —— 16/17 个有
- `JWInteger` —— 16/17 个有
- `WanVideoClipVisionEncode` —— 16/17 个有
- `WanVideoSetLoRAs` —— 16/17 个有
- `ImageResize+` —— 15/17 个有
- `LoadWanVideoClipTextEncoder` —— 15/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/17 个有
- `LayerUtility: PurgeVRAM` —— 11/17 个有
- `SetNode` —— 10/17 个有
- `GetNode` —— 9/17 个有
- `ImageLoader` —— 9/17 个有
- `LoadImage` —— 8/17 个有
- `CreateCFGScheduleFloatList` —— 7/17 个有
- `CR Prompt Text` —— 5/17 个有
- `GetImageSizeAndCount` —— 3/17 个有
- `SimpleMath+` —— 3/17 个有
- `CLIPVisionLoader` —— 1/17 个有
- `Int` —— 1/17 个有
- `MathExpression|pysssss` —— 1/17 个有
- `TrimVideoLatent` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有
- `easy seed` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
