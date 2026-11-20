---
key: 视频生成/视频生视频/LTX 2.5 Alpha Gen Beta_2107891131768991745.json
name: LTX 2.5 Alpha Gen Beta_2107891131768991745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/视频生视频/LTX 2.5 Alpha Gen Beta_2107891131768991745.json
hash: 04528cd21fb48c57
coverage: 0.65625
learned_at: 2026-11-14 02:59:37
nodes: [PrimitiveStringMultiline, PreviewAny, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, Note, SamplerCustomAdvanced, LTXVCropGuides, VAELoader, VAELoader, UNETLoader, Reroute, CLIPLoader, CLIPLoader, ComfyNotNode, CLIPTextEncode, PrimitiveBoolean, TextGenerateLTX2Prompt, CLIPTextEncode, StringContains, LTXVConditioning, ComfySwitchNode, ComfySwitchNode, GemmaAPITextEncode, GemmaAPITextEncode, GetNode, ImageConcatMulti, ImageConcatMulti, SetNode, SetNode, ImageScaleBy, GetNode, GetNode, GetNode, SetNode, GetNode, PixaromaRunTimer, ImageToMask, GetNode, GetNode, GetNode, GetNode, EmptyImage, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, JoinImageWithAlpha, ImageBlend, PrimitiveStringMultiline, Label (rgthree), Label (rgthree), VHS_VideoCombine, VHS_VideoCombine, Label (rgthree), Label (rgthree), GetNode, ImageCompositeMasked, VHS_VideoCombine, GetImageSize, SetNode, SetNode, VHS_VideoInfo, GetNode, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), CreateVideo, GetVideoComponents, ResizeImageMaskNode, GetImageSize, LTXVConditioning, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ComfySwitchNode, LTXVAudioVAEDecode, VAEDecodeTiled, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, CreateVideo, LTXVSeparateAVLatent, MarkdownNote, LTXICLoRALoaderModelOnly, SetNode, VHS_VideoCombine, VHS_VideoCombine, PrimitiveInt, ResizeImageMaskNode, VHS_LoadVideo, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 145}
---

# 视频生成/视频生视频/LTX 2.5 Alpha Gen Beta_2107891131768991745.json

> 来源文件 `comfyui_library/workflows/视频生成/视频生视频/LTX 2.5 Alpha Gen Beta_2107891131768991745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（96 个）：
- `PrimitiveStringMultiline`
- `PreviewAny`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Reroute`
- `CLIPLoader`
- `CLIPLoader`
- `ComfyNotNode`
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `CLIPTextEncode` ★核心
- `StringContains`
- `LTXVConditioning`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GemmaAPITextEncode`
- `GemmaAPITextEncode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `SetNode`
- `ImageScaleBy`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PixaromaRunTimer`
- `ImageToMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `JoinImageWithAlpha`
- `ImageBlend`
- `PrimitiveStringMultiline`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `ImageCompositeMasked`
- `VHS_VideoCombine`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `GetNode`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `CreateVideo`
- `GetVideoComponents`
- `ResizeImageMaskNode`
- `GetImageSize`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ComfySwitchNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `VHS_LoadVideo`
- `PrimitiveInt`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（63/96）

**有卡**：`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`ComfyNotNode`、`CLIPTextEncode`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`StringContains`、`LTXVConditioning`、`GemmaAPITextEncode`、`ImageConcatMulti`、`ImageScaleBy`、`PixaromaRunTimer`、`ImageToMask`、`EmptyImage`、`JoinImageWithAlpha`、`ImageBlend`、`Label (rgthree)`、`VHS_VideoCombine`、`ImageCompositeMasked`、`GetImageSize`、`VHS_VideoInfo`、`CreateVideo`、`GetVideoComponents`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXICLoRALoaderModelOnly`、`VHS_LoadVideo`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
