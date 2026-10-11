---
key: 视频生成/文生视频/LTX2.3+-图生视频+15s超长时间+电商服装模特带货短视频+优化版_2052915059373953025.json
name: LTX2.3+-图生视频+15s超长时间+电商服装模特带货短视频+优化版_2052915059373953025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3+-图生视频+15s超长时间+电商服装模特带货短视频+优化版_2052915059373953025.json
hash: d866a7d41fcc7caf
coverage: 0.813559
learned_at: 2026-10-11 19:49:37
nodes: [CFGGuider, KSamplerSelect, KSamplerSelect, VAELoaderKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, DualCLIPLoader, PathchSageAttentionKJ, LTXVImgToVideoInplace, LTXVLatentUpsampler, ManualSigmas, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, easy mathInt, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXVAudioVAEDecode, RandomNoise, RandomNoise, easy imageSize, ResizeImagesByLongerEdge, VAEDecode, easy imageSize, VAELoaderKJ, ImageScaleBy, LTXVSeparateAVLatent, EmptyImage, LTXVCropGuides, UNETLoader, LoraLoaderModelOnly, ImageConcanate, easy ifElse, VAEDecode, ImageResizeKJv2, ImageResizeKJv2, easy ifElse, LTXVPreprocess, PreviewImage, ImageResizeKJv2, ImageResizeKJv2, Note, SamplerCustomAdvanced, GetImageSize, easy compare, easy promptConcat, easy showAnything, AILab_QwenVL, ManualSigmas, VHS_VideoCombine, VHS_VideoCombine, easy positive, LoadImage]
patterns: []
missing: [easy compare, easy mathInt, easy positive, easy imageSize, easy imageSize, easy promptConcat]
parameters: {"batch_size": 1, "height": 24, "width": 361}
discoveries: [次要节点 `easy compare` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3+-图生视频+15s超长时间+电商服装模特带货短视频+优化版_2052915059373953025.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3+-图生视频+15s超长时间+电商服装模特带货短视频+优化版_2052915059373953025.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `DualCLIPLoader`
- `PathchSageAttentionKJ`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `easy mathInt`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `RandomNoise`
- `easy imageSize`
- `ResizeImagesByLongerEdge`
- `VAEDecode` ★核心
- `easy imageSize`
- `VAELoaderKJ`
- `ImageScaleBy`
- `LTXVSeparateAVLatent`
- `EmptyImage`
- `LTXVCropGuides`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `easy ifElse`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy ifElse`
- `LTXVPreprocess`
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `easy compare`
- `easy promptConcat`
- `easy showAnything`
- `AILab_QwenVL`
- `ManualSigmas`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy positive`
- `LoadImage`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（48/59）

**有卡**：`CFGGuider`、`KSamplerSelect`、`VAELoaderKJ`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`ManualSigmas`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`RandomNoise`、`ResizeImagesByLongerEdge`、`VAEDecode`、`ImageScaleBy`、`EmptyImage`、`LTXVCropGuides`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageConcanate`、`ImageResizeKJv2`、`LTXVPreprocess`、`GetImageSize`、`AILab_QwenVL`、`VHS_VideoCombine`、`LoadImage`

**缺卡**（6）：`easy compare`、`easy mathInt`、`easy positive`、`easy imageSize`、`easy imageSize`、`easy promptConcat`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `easy compare` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
