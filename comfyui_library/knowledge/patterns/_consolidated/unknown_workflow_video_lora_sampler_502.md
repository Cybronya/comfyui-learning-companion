---
name: unknown_workflow_video_lora_sampler_502
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92125
common_nodes: [GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddOneToAllPoseEmbeds, WanVideoAddOneToAllReferenceEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1998602211204718594.json, 视频生成/图生视频/1998598682582900738.json, 视频生成/图生视频/1998516871580278785.json, 视频生成/图生视频/1998992837641392130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_502

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1998602211204718594.json、视频生成/图生视频/1998598682582900738.json、视频生成/图生视频/1998516871580278785.json、视频生成/图生视频/1998992837641392130.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoAddOneToAllReferenceEmbeds`
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

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Int` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `WanVideoContextOptions` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
