---
name: unknown_workflow_video_lora_sampler_767
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5975
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ColorTransfer, ComfyNumberConvert, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageFromBatch, ImageResizeKJv2, KSamplerSelect, LTXVAddGuideMulti, LTXVConcatAVLatent, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideo, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PreviewAny, PrimitiveInt, RTXVideoSuperResolution, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VRAM_Debug, Video_Fade]
problems: []
missing: []
members: [视频生成/图生视频/2070502148785393666.json, 视频生成/图生视频/2072296730909044737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_767

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2070502148785393666.json、视频生成/图生视频/2072296730909044737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ColorTransfer`
- `ComfyNumberConvert`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideo`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `Video_Fade`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `FrameInterpolate` —— 1/2 个有
- `FrameInterpolationModelLoader` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `LTXVAudioVAEDecode` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `TextGenerate` —— 1/2 个有
- `easy seed` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 137 | - | 2 | 59% |
| 高度 | 50 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 137，样本不足，未给区间，2 个样本
- 高度 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
