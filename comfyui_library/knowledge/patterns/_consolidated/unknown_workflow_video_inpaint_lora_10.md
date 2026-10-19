---
name: unknown_workflow_video_inpaint_lora_10
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9205
common_nodes: [BatchCount+, BlendInpaint, BlockifyMask, CFGGuider, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, CreateVideo, DrawMaskOnImage, EmptyFlux2LatentImage, Flux2Scheduler, GrowMaskWithBlur, Image Filter Adjustments, ImageAndMaskPreview, ImageBatch, ImageFromBatch, ImageScale, ImageToMask, KSamplerSelect, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, MathExpression|pysssss, PreviewImage, RandomNoise, ReferenceLatent, RepeatImageBatch, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_DuplicateMasks, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy imageSize, easy int, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/视频去水印丨Flux2 Klein＋Wan2.2丨遮罩区域修复_2099795887701712898.json, 视频生成/图生视频/1956274392068182017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频去水印丨Flux2 Klein＋Wan2.2丨遮罩区域修复_2099795887701712898.json、视频生成/图生视频/1956274392068182017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchCount+`
- `BlendInpaint`
- `BlockifyMask`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `CreateVideo`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `Image Filter Adjustments`
- `ImageAndMaskPreview`
- `ImageBatch`
- `ImageFromBatch`
- `ImageScale`
- `ImageToMask`
- `KSamplerSelect`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_DuplicateMasks`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `HAIGC_VideoRelay` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
