---
name: unknown_workflow_video_lora_sampler_347
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.957
common_nodes: [ApplyFaceProcessor, CR Prompt Text, FaceProcessorLoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VideoInputPreprocessor, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
members: [视频生成/图生视频/1956898077279969282.json, 视频生成/图生视频/1960243766210801666.json, 视频生成/图生视频/1956781749314228225.json, 视频生成/图生视频/1959190374550024194.json, 视频生成/图生视频/1958204271017791490.json, 视频生成/文生视频/1956898077279969282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_347

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1956898077279969282.json、视频生成/图生视频/1960243766210801666.json、视频生成/图生视频/1956781749314228225.json、视频生成/图生视频/1959190374550024194.json、视频生成/图生视频/1958204271017791490.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyFaceProcessor`
- `CR Prompt Text`
- `FaceProcessorLoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VideoInputPreprocessor`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `VHS_VideoInfo` —— 5/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `LatentLoaderAdvanced` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `SaveLatent` —— 3/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `FaceOnlyModeSwitch` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `ReActorFaceSwap` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `VHS_VideoInfoLoaded` —— 1/6 个有
- `VideoBackgroundRestorer` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、CR Prompt Text
