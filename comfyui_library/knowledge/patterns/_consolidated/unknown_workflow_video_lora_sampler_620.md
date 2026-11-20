---
name: unknown_workflow_video_lora_sampler_620
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9602
common_nodes: [CreateCFGScheduleFloatList, ImageResizeKJv2, LoadImage, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json, 视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json, 视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json, 视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json, 视频生成/图生视频/wan2.2图生视频_2037533224406093826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_620

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json、视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json、视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json、视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json、视频生成/图生视频/wan2.2图生视频_2037533224406093826.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `ImageResizeKJv2`
- `LoadImage`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `LoadWanVideoT5TextEncoder` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `WanVideoTextEncode` —— 4/5 个有
- `CLIPLoader` —— 3/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `WanVideoTextEmbedBridge` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `PreViewVideo` —— 2/5 个有
- `CLIPLoaderGGUF` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `ReActorFaceSwap` —— 1/5 个有
- `SaveVideo` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `VideoFrameExtractor` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
