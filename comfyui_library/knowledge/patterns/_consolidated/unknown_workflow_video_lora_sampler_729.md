---
name: unknown_workflow_video_lora_sampler_729
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6485
common_nodes: [AIO_Preprocessor, AddLabel, ColorMatch, DWPreprocessor, EmptyImage, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBlend, ImageConcatMulti, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, Primitive integer [Crystools], RH_Captioner, SetNode, ShowText|pysssss, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1929256563398316034.json, 视频生成/图生视频/1925046681505886210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_729

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1929256563398316034.json、视频生成/图生视频/1925046681505886210.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `ColorMatch`
- `DWPreprocessor`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBlend`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
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

**可变部分**（部分 workflow 才有）：
- `Compare` —— 1/2 个有
- `EasyControlGenerate` —— 1/2 个有
- `EasyControlLoadFlux` —— 1/2 个有
- `EasyControlLoadLora` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResizeTo8x` —— 1/2 个有
- `ImpactStringSelector` —— 1/2 个有
- `RH_ComfyFluxKontext` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RandomInt` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `String Replace (mtb)` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
