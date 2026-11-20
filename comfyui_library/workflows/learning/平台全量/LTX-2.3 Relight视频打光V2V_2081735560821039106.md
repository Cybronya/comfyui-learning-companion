---
key: 平台全量/LTX-2.3 Relight视频打光V2V_2081735560821039106.json
name: LTX-2.3 Relight视频打光V2V_2081735560821039106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3 Relight视频打光V2V_2081735560821039106.json
hash: e4cbabeca9d4ef71
coverage: 0.901961
learned_at: 2026-11-14 00:36:51
nodes: [LTXVConcatAVLatent, PrimitiveString, CFGGuider, KSamplerSelect, LTXVAudioVAEDecode, LTXAddVideoICLoRAGuide, SamplerCustomAdvanced, ManualSigmas, RandomNoise, LTXVAudioVAELoader, LTXFloatToInt, GemmaAPITextEncode, GemmaAPITextEncode, ImageScale, LTXVTiledVAEDecode, LTXVPreprocess, LTXVSeparateAVLatent, LTXVCropGuides, ImageConcanate, EmptyLTXVLatentVideo, CreateVideo, SaveVideo, Video Slice, PrimitiveFloat, LTXVConditioning, Note, Note, LTXICLoRALoaderModelOnly, CLIPTextEncode, CLIPTextEncode, CreateVideo, CheckpointLoaderSimple, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadVideo, SphereLightNode, ResizeImageMaskNode, ImageScale, LTXAVTextEncoderLoader, CreateVideo, LTXVEmptyLatentAudio, PrimitiveInt, ImageCompositeMasked, GetImageSize, GetVideoComponents, VHS_GetImageCount, Int, Int, SaveVideo, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 平台全量/LTX-2.3 Relight视频打光V2V_2081735560821039106.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3 Relight视频打光V2V_2081735560821039106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `LTXVConcatAVLatent`
- `PrimitiveString`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXAddVideoICLoRAGuide`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LTXVAudioVAELoader`
- `LTXFloatToInt`
- `GemmaAPITextEncode`
- `GemmaAPITextEncode`
- `ImageScale`
- `LTXVTiledVAEDecode` ★核心
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `ImageConcanate`
- `EmptyLTXVLatentVideo`
- `CreateVideo`
- `SaveVideo`
- `Video Slice`
- `PrimitiveFloat`
- `LTXVConditioning`
- `Note`
- `Note`
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadVideo`
- `SphereLightNode`
- `ResizeImageMaskNode`
- `ImageScale`
- `LTXAVTextEncoderLoader`
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveInt`
- `ImageCompositeMasked`
- `GetImageSize`
- `GetVideoComponents`
- `VHS_GetImageCount`
- `Int`
- `Int`
- `SaveVideo`
- `SaveVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（46/51）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`ManualSigmas`、`RandomNoise`、`LTXVAudioVAELoader`、`LTXFloatToInt`、`GemmaAPITextEncode`、`ImageScale`、`LTXVTiledVAEDecode`、`LTXVPreprocess`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`ImageConcanate`、`EmptyLTXVLatentVideo`、`CreateVideo`、`SaveVideo`、`Video Slice`、`LTXVConditioning`、`LTXICLoRALoaderModelOnly`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LoadVideo`、`SphereLightNode`、`ResizeImageMaskNode`、`LTXAVTextEncoderLoader`、`LTXVEmptyLatentAudio`、`ImageCompositeMasked`、`GetImageSize`、`GetVideoComponents`、`VHS_GetImageCount`、`Int`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、GemmaAPITextEncode
