---
name: unknown_workflow_video_upscale_face_detailer
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.633
common_nodes: [AlignYourStepsScheduler, Any Switch (rgthree), Anything Everywhere, BNK_CLIPTextEncodeAdvanced, CLIPTextEncode, CheckpointLoaderSimple, DownloadAndLoadFlorence2Model, EmptyLatentImage, FaceDetailer, Fast Actions Button (rgthree), Fast Groups Muter (rgthree), Florence2Run, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageScale, ImageScaleBy, ImageUpscaleWithModel, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoRA Stacker, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Preview Chooser, PreviewImage, RescaleCFG, SamplerCustom, SaveImage, Seed Everywhere, SetNode, ShowText|pysssss, StringFunction|pysssss, TextInput_, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WD14Tagger|pysssss, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy loraStackApply]
problems: []
missing: [Fast Actions Button (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), StringFunction|pysssss, WD14Tagger|pysssss, LoRA Stacker, Preview Chooser, Seed Everywhere, easy loraStackApply]
members: [图片生成/文生图/1914682063172370433.json, 视频生成/图生视频/1914682063172370433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1914682063172370433.json、视频生成/图生视频/1914682063172370433.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `AlignYourStepsScheduler`
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DownloadAndLoadFlorence2Model`
- `EmptyLatentImage`
- `FaceDetailer`
- `Fast Actions Button (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoRA Stacker`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Preview Chooser`
- `PreviewImage`
- `RescaleCFG`
- `SamplerCustom`
- `SaveImage`
- `Seed Everywhere`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `TextInput_`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WD14Tagger|pysssss`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy loraStackApply`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Fast Actions Button (rgthree)、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、LayerUtility: PurgeVRAM V2、MathExpression|pysssss
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
