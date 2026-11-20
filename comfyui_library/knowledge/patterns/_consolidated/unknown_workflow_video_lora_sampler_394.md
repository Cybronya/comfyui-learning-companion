---
name: unknown_workflow_video_lora_sampler_394
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.969125
common_nodes: [CreateCFGScheduleFloatList, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2_图生视频工作流  加速版_1962439638365376514.json, 视频生成/图生视频/【橘子AI】Wan 图生视频工作流 -KJ_1978004936166363137.json, 视频生成/图生视频/图生视频---Wan2.2首尾帧Kijai版_2044685944468541441.json, 视频生成/图生视频/图生视频---Wan2.2首尾帧Kijai版_2053674429732929538.json, 视频生成/图生视频/图转视频-Wan2.2首尾帧Kijai版好用_1965310259709493249.json, 视频生成/图生视频/自己用：Wan2.2首尾帧_1955902508302520321.json, 视频生成/图生视频/首尾帧图片_生成视频（wan2.2最新版本）_1952744719957880834.json, 视频生成/文生视频/Wan2.2文生视频-告别PPT式电视剧_1950553795895939073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_394

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/wan2.2_图生视频工作流  加速版_1962439638365376514.json、视频生成/图生视频/【橘子AI】Wan 图生视频工作流 -KJ_1978004936166363137.json、视频生成/图生视频/图生视频---Wan2.2首尾帧Kijai版_2044685944468541441.json、视频生成/图生视频/图生视频---Wan2.2首尾帧Kijai版_2053674429732929538.json、视频生成/图生视频/图转视频-Wan2.2首尾帧Kijai版好用_1965310259709493249.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `LoadWanVideoT5TextEncoder` —— 7/8 个有
- `WanVideoImageToVideoEncode` —— 7/8 个有
- `WanVideoTextEncode` —— 7/8 个有
- `CLIPLoader` —— 3/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `WanVideoTextEmbedBridge` —— 3/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `SimpleMath+` —— 1/8 个有
- `WanVideoEmptyEmbeds` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
