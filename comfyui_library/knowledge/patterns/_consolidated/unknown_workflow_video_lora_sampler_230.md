---
name: unknown_workflow_video_lora_sampler_230
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.972556
common_nodes: [CreateCFGScheduleFloatList, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1962439638365376514.json, 视频生成/图生视频/1978004936166363137.json, 视频生成/图生视频/2044685944468541441.json, 视频生成/图生视频/2053674429732929538.json, 视频生成/图生视频/1965310259709493249.json, 视频生成/图生视频/1965415363951382530.json, 视频生成/图生视频/1955902508302520321.json, 视频生成/图生视频/1952744719957880834.json, 视频生成/文生视频/1950553795895939073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_230

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1962439638365376514.json、视频生成/图生视频/1978004936166363137.json、视频生成/图生视频/2044685944468541441.json、视频生成/图生视频/2053674429732929538.json、视频生成/图生视频/1965310259709493249.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 8/9 个有
- `INTConstant` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `LoadWanVideoT5TextEncoder` —— 8/9 个有
- `WanVideoImageToVideoEncode` —— 8/9 个有
- `WanVideoTextEncode` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `ImageResizeKJv2` —— 7/9 个有
- `CLIPLoader` —— 3/9 个有
- `CLIPTextEncode` —— 3/9 个有
- `WanVideoTextEmbedBridge` —— 3/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `WanVideoEmptyEmbeds` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
