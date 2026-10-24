---
name: unknown_workflow_video_lora_sampler_703
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6295
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ColorTransfer, ComfyNumberConvert, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageFromBatch, ImageResizeKJv2, JjkText, JoinStrings, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideo, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, PrimitiveInt, RTXVideoSuperResolution, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, Text, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VRAM_Debug, Video_Fade, easy seed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/动态循环壁纸一键生成_2081926524151877634.json, 视频生成/图生视频/动态循环壁纸一键生成_2072296730909044737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_703

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/动态循环壁纸一键生成_2081926524151877634.json、视频生成/图生视频/动态循环壁纸一键生成_2072296730909044737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

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
- `JjkText`
- `JoinStrings`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideo`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `Video_Fade`
- `easy seed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 1/2 个有
- `Float to Int` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 193 | - | 2 | 100% |
| 高度 | 50 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 193，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
