---
name: unknown_workflow_video_sampler_vae_180
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.679333
common_nodes: [BlockifyMask, FaceAnalysisModels, FaceBoundingBox, GetNode, GrowMask, ImageConcanate, ImageResizeKJv2, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview+, MochaEmbeds, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1 Mocha视频人物一键替换_1981739348041310210.json, 平台全量/人物替换 2.0  MoCha 自动替换版_1982713428726947841.json, 视频生成/图生视频/Wan2.1 Mocha视频人物一键替换_1982423394660564994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_180

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan2.1 Mocha视频人物一键替换_1981739348041310210.json、平台全量/人物替换 2.0  MoCha 自动替换版_1982713428726947841.json、视频生成/图生视频/Wan2.1 Mocha视频人物一键替换_1982423394660564994.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `GetNode`
- `GrowMask`
- `ImageConcanate`
- `ImageResizeKJv2`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview+`
- `MochaEmbeds`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PDIMAGE_LongerSize` —— 2/3 个有
- `VHS_VideoInfoSource` —— 2/3 个有
- `WanVideoLoraSelectMulti` —— 2/3 个有
- `WanVideoSetBlockSwap` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
