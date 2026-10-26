---
name: unknown_workflow_video_lora_sampler_33
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.941462
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Qwen-VL图片反推-图生视频-kj工作流-wan2.2_1983525120713138178.json, 视频生成/图生视频/Qwen3VL首尾帧反推工作流-wan2.2-kj版_1983529460303601666.json, 视频生成/图生视频/Wan2.2首尾帧工作流—Kj加速版_1962882725575364609.json, 视频生成/图生视频/Wan2.2首尾帧工作流—课程使用_1972581199266906114.json, 视频生成/图生视频/wan2.2-首尾帧_2014248439579676673.json, 视频生成/图生视频/wan2.2Pro首尾帧生成视频工作流_2013862124266721282.json, 视频生成/图生视频/wan2.2首尾帧视频工作流_2013162152139431937.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048571694041800706.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048653140999806977.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2048940040620875778.json, 视频生成/图生视频/图生视频--首尾帧-wan2.2-kj版工作流_2069594425340284930.json, 视频生成/图生视频/建筑-wan2.2单帧视频工作流_2022682129682931714.json, 视频生成/图生视频/快速版动漫首尾帧控制_2016405301691420673.json, 视频生成/图生视频/首尾帧 图生视频 加速版-wan2.2-kj版_2021050024263684097.json, 视频生成/图生视频/首尾帧 生视频 kj加速版 wan2.2万相4步加速视频 Rapid AllInOne 2图生视频_2033052828255657985.json, 视频生成/图生视频/首尾帧-wan2.2-kj版_1993144269496057857.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2011275998205054977.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2013608630863536130.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2014220447117746178.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2020055419988746242.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2054450000423333890.json, 视频生成/图生视频/首尾帧-wan2.2-kj版工作流_2068009866219835393.json, 视频生成/图生视频/首尾帧视频 wan2.2_2018548235928870914.json, 视频生成/文生视频/Wan2.2首尾帧工作流—Kj加速版_1962914848373968898.json, 视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json, 视频生成/文生视频/首尾帧图生视频   wan2.2-kj版加速音画同步 全自动首尾帧视频_2016386248029511681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/Qwen-VL图片反推-图生视频-kj工作流-wan2.2_1983525120713138178.json、视频生成/图生视频/Qwen3VL首尾帧反推工作流-wan2.2-kj版_1983529460303601666.json、视频生成/图生视频/Wan2.2首尾帧工作流—Kj加速版_1962882725575364609.json、视频生成/图生视频/Wan2.2首尾帧工作流—课程使用_1972581199266906114.json、视频生成/图生视频/wan2.2-首尾帧_2014248439579676673.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 26 个 workflow 都包含：
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
- `INTConstant` —— 25/26 个有
- `ImageResize+` —— 25/26 个有
- `JWInteger` —— 25/26 个有
- `LoadWanVideoClipTextEncoder` —— 25/26 个有
- `WanVideoClipVisionEncode` —— 25/26 个有
- `LayerUtility: PurgeVRAM` —— 22/26 个有
- `ImageLoader` —— 21/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 21/26 个有
- `SetNode` —— 17/26 个有
- `GetNode` —— 16/26 个有
- `LoadImage` —— 5/26 个有
- `SimpleMath+` —— 3/26 个有
- `CreateCFGScheduleFloatList` —— 2/26 个有
- `MultiplePathsInput` —— 2/26 个有
- `Qwen3_VQA` —— 2/26 个有
- `WanVideoApplyNAG` —— 2/26 个有
- `easy showAnything` —— 2/26 个有
- `Fast Groups Bypasser (rgthree)` —— 1/26 个有
- `Int` —— 1/26 个有
- `RIFE VFI` —— 1/26 个有
- `easy cleanGpuUsed` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
