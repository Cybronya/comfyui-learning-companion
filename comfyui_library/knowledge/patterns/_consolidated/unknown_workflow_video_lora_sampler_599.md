---
name: unknown_workflow_video_lora_sampler_599
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9224
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VideoInputPreprocessor, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/最强视频换脸 wan stand in vace 版_1958711325885100034.json, 数字人/数字人/最强视频换脸 wan stand in_1958073826179428353.json, 视频生成/图生视频/Stand In Face Swap换脸_1960243766210801666.json, 视频生成/图生视频/（自用）Stand In Face Swap视频换脸V2（背景洗图版）_1958204271017791490.json, 视频生成/文生视频/（自用）Stand In Face Swap视频换脸V2_1956898077279969282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_599

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/最强视频换脸 wan stand in vace 版_1958711325885100034.json、数字人/数字人/最强视频换脸 wan stand in_1958073826179428353.json、视频生成/图生视频/Stand In Face Swap换脸_1960243766210801666.json、视频生成/图生视频/（自用）Stand In Face Swap视频换脸V2（背景洗图版）_1958204271017791490.json、视频生成/文生视频/（自用）Stand In Face Swap视频换脸V2_1956898077279969282.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VideoInputPreprocessor`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `WanVideoEmptyEmbeds` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `LatentLoaderAdvanced` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `SaveLatent` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `TrimVideoLatent` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有
- `WanVideoVACEEncode` —— 1/5 个有
- `WanVideoVACEModelSelect` —— 1/5 个有
- `WanVideoVACEStartToEndFrame` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
