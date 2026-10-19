---
name: unknown_workflow_video_lora_sampler_692
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.760333
common_nodes: [CR Text, GetImageSizeAndCount, ImageFromBatch+, LoadWanVideoT5TextEncoder, PrimitiveInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: [CR Text, ImageFromBatch+, easy cleanGpuUsed]
members: [视频生成/文生视频/1950074509607002113.json, 视频生成/文生视频/1974458847702200321.json, 视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_692

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1950074509607002113.json、视频生成/文生视频/1974458847702200321.json、视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `Wan_video_prompt_generator` —— 2/3 个有
- `AILab_MiniCPM_4_V_Advanced` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `ShellAgentPluginOutputText` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `WanVideoImageToVideoEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、ImageFromBatch+、easy cleanGpuUsed
