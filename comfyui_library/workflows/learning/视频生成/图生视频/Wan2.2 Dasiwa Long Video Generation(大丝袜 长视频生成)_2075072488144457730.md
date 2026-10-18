---
key: 视频生成/图生视频/Wan2.2 Dasiwa Long Video Generation(大丝袜 长视频生成)_2075072488144457730.json
name: Wan2.2 Dasiwa Long Video Generation(大丝袜 长视频生成)_2075072488144457730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Dasiwa Long Video Generation(大丝袜 长视频生成)_2075072488144457730.json
hash: 702477e46a32a11d
coverage: 0.454976
learned_at: 2026-10-15 22:41:21
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, SetNode, GetNode, CLIPTextEncode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, ScheduledCFGGuidance, DisableNoise, WanImageToVideoSVIPro, SetNode, PathchSageAttentionKJ, ModelSamplingSD3, Note, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, ModelPatchTorchSettings, ModelPatchTorchSettings, SetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, GetNode, GetNode, GetNode, ScheduledCFGGuidance, GetNode, GetNode, SamplerCustomAdvanced, GetImagesFromBatchIndexed, SetNode, SplitSigmas, SetNode, VAEEncode, SetNode, GetNode, GetNode, SetNode, KSamplerSelect, easy int, SetNode, Note, SetNode, VAELoader, Fast Groups Bypasser (rgthree), SetNode, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ScheduledCFGGuidance, DisableNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, ScheduledCFGGuidance, GetNode, GetNode, GetNode, SamplerCustomAdvanced, GetImagesFromBatchIndexed, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, VAEDecode, SetNode, ScheduledCFGGuidance, DisableNoise, LoraLoaderModelOnly, GetNode, GetNode, GetNode, ScheduledCFGGuidance, GetNode, SamplerCustomAdvanced, GetImagesFromBatchIndexed, PreviewImage, GetNode, GetNode, VAEDecode, ScheduledCFGGuidance, DisableNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, ScheduledCFGGuidance, GetNode, GetNode, GetNode, SamplerCustomAdvanced, GetImagesFromBatchIndexed, PreviewImage, GetNode, GetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, ImageBatchExtendWithOverlap, VAEDecode, ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, BasicScheduler, UnetLoaderGGUF, UNETLoader, UNETLoader, UnetLoaderGGUF, GetNode, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, VHS_VideoCombine, ShowText|pysssss, WanImageToVideoSVIPro, WanImageToVideoSVIPro, WanImageToVideoSVIPro, CLIPTextEncode, SetNode, VHS_VideoCombine, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, easy cleanGpuUsed, GetNode, SimpleMath+, ImageScaleBy, StringReplace, StringReplace, StringReplace, StringReplace, Fast Groups Bypasser (rgthree), AILab_QwenVL, ShowText|pysssss, PrimitiveStringMultiline, ShowText|pysssss, ColorMatch, VAEDecode, LoraLoaderModelOnly, GetNode, GetNode, ShowText|pysssss, AILab_QwenVL, RandomNoise, Note, RandomNoise, AILab_QwenVL, SetNode, RandomNoise, RandomNoise, PrimitiveFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, GetNode, ImageBatchExtendWithOverlap, PrimitiveStringMultiline, AILab_QwenVL, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, FL_FILM, PrimitiveInt, LoadImage, SaveImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Dasiwa Long Video Generation(大丝袜 长视频生成)_2075072488144457730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075072488144457730.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（211 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ScheduledCFGGuidance`
- `DisableNoise`
- `WanImageToVideoSVIPro`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Note`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetImagesFromBatchIndexed`
- `SetNode`
- `SplitSigmas`
- `SetNode`
- `VAEEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `easy int`
- `SetNode`
- `Note`
- `SetNode`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ScheduledCFGGuidance`
- `DisableNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `ScheduledCFGGuidance`
- `DisableNoise`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ScheduledCFGGuidance`
- `DisableNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `BasicScheduler`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `SimpleMath+`
- `ImageScaleBy`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `Fast Groups Bypasser (rgthree)`
- `AILab_QwenVL`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `ColorMatch`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `AILab_QwenVL`
- `RandomNoise`
- `Note`
- `RandomNoise`
- `AILab_QwenVL`
- `SetNode`
- `RandomNoise`
- `RandomNoise`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `PrimitiveStringMultiline`
- `AILab_QwenVL`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `FL_FILM`
- `PrimitiveInt`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **45%**（96/211）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`ScheduledCFGGuidance`、`DisableNoise`、`WanImageToVideoSVIPro`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`GetImagesFromBatchIndexed`、`SplitSigmas`、`VAEEncode`、`KSamplerSelect`、`easy int`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageBatchExtendWithOverlap`、`VHS_VideoCombine`、`BasicScheduler`、`UnetLoaderGGUF`、`UNETLoader`、`easy cleanGpuUsed`、`SimpleMath+`、`ImageScaleBy`、`StringReplace`、`AILab_QwenVL`、`ColorMatch`、`RandomNoise`、`LoadImage`、`FL_FILM`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect
