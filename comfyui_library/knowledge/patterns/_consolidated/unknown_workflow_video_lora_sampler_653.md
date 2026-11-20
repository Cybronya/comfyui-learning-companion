---
name: unknown_workflow_video_lora_sampler_653
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.863
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VideoInputPreprocessor, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/03-12-03-WAN2.1-视频转绘-噪波重绘_1989933993594417154.json, 平台全量/视频洗图 Stand In Face Swap_1957447920905809921.json, 视频生成/图生视频/Stand In Face Swap视频换脸V2（背景洗图版）_1956781749314228225.json, 视频生成/图生视频/stand in 视频换脸+视频高清放大V1_1959190374550024194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_653

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/03-12-03-WAN2.1-视频转绘-噪波重绘_1989933993594417154.json、平台全量/视频洗图 Stand In Face Swap_1957447920905809921.json、视频生成/图生视频/Stand In Face Swap视频换脸V2（背景洗图版）_1956781749314228225.json、视频生成/图生视频/stand in 视频换脸+视频高清放大V1_1959190374550024194.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `CR Prompt Text` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `FaceOnlyModeSwitch` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `ReActorFaceSwap` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveLatent` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `VideoBackgroundRestorer` —— 1/4 个有
- `WanVideoVACEModelSelect` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
