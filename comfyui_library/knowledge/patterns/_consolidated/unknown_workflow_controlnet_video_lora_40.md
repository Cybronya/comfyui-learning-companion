---
name: unknown_workflow_controlnet_video_lora_40
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7635
common_nodes: [AIO_Preprocessor, AddLabel, ApplyFBCacheOnModel, BasicGuider, BasicScheduler, CLIPTextEncode, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptyImage, Fast Groups Bypasser (rgthree), Florence2Run, FluxGuidance, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBlend, ImageConcanate, ImageConcatMulti, ImagePadKJ, ImageResizeKJ, KSamplerSelect, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, PreviewImage, Primitive integer [Crystools], RH_Captioner, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/0603_1926867767645904898.json, 视频生成/图生视频/多种流行视频风格Wan2.1转绘(吉卜力_线稿_唐风等)_1925208307319906306.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_40

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/0603_1926867767645904898.json、视频生成/图生视频/多种流行视频风格Wan2.1转绘(吉卜力_线稿_唐风等)_1925208307319906306.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `ApplyFBCacheOnModel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `FluxGuidance`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBlend`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 1/2 个有
- `Bjornulf_ShowInt` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
