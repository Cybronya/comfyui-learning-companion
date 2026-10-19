---
name: unknown_workflow_video_lora_sampler_461
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.82475
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, GetImagesFromBatchIndexed, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageRemoveBackground+, ImageResizeKJ, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MatAnyoneVideoMatting, ModelSamplingFlux, PreviewImage, RIFE VFI, RandomNoise, SAMModelLoader (segment anything), SamplerCustomAdvanced, SaveImage, TransparentBGSession+, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEDecodeTiled, VAELoader, VHS_LoadVideoFFmpeg, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ, easy getNode, easy setNode]
problems: []
missing: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageRemoveBackground+, RIFE VFI, SAMModelLoader (segment anything), TransparentBGSession+, easy getNode, easy setNode]
members: [图片生成/文生图/1910346221037518849.json, 视频生成/图生视频/1910346221037518849.json, 视频生成/图生视频/2046766402748555265.json, 视频生成/图生视频/2047192826013818882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_461

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1910346221037518849.json、视频生成/图生视频/1910346221037518849.json、视频生成/图生视频/2046766402748555265.json、视频生成/图生视频/2047192826013818882.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GetImagesFromBatchIndexed`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageRemoveBackground+`
- `ImageResizeKJ`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MatAnyoneVideoMatting`
- `ModelSamplingFlux`
- `PreviewImage`
- `RIFE VFI`
- `RandomNoise`
- `SAMModelLoader (segment anything)`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TransparentBGSession+`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`
- `easy getNode`
- `easy setNode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：GroundingDinoModelLoader (segment anything)、GroundingDinoSAMSegment (segment anything)、ImageRemoveBackground+、RIFE VFI、SAMModelLoader (segment anything)
