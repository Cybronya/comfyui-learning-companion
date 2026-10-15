---
key: 视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json
name: LTX2.3 电影级全向外扩视频工作流_2053375516647931906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json
hash: 3c062887d60ca44b
coverage: 0.92
learned_at: 2026-10-15 22:45:01
nodes: [LTXVConditioning, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVCropGuides, LTXVSeparateAVLatent, CM_FloatToInt, CFGGuider, RandomNoise, GemmaAPITextEncode, PrimitiveString, GemmaAPITextEncode, ManualSigmas, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVPreprocess, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVAudioVAEDecode, ImageConcanate, Switch image [Crystools], Color Correct (mtb), VAEDecodeTiled, CLIPTextEncode, LTXVAudioVAELoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, GetImageSize, Color Correct (mtb), GetImageSize+, ImageResizeKJv2, VHS_VideoCombine, Switch image [Crystools], Note, VHS_VideoCombine, PrimitiveBoolean, LTXICLoRALoaderModelOnly, LTXVImgToVideoConditionOnly, LoadImage, CLIPTextEncode, PrimitiveBoolean, VHS_VideoCombine, VHS_LoadVideo, ResizeAndPadImage, VHS_VideoInfo, PrimitiveNode, Int, easy showAnything, Float, FluxResolutionNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `CM_FloatToInt`
- `CFGGuider`
- `RandomNoise`
- `GemmaAPITextEncode`
- `PrimitiveString`
- `GemmaAPITextEncode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVPreprocess`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImageConcanate`
- `Switch image [Crystools]`
- `Color Correct (mtb)`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `Color Correct (mtb)`
- `GetImageSize+`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `Switch image [Crystools]`
- `Note`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVImgToVideoConditionOnly`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ResizeAndPadImage`
- `VHS_VideoInfo`
- `PrimitiveNode`
- `Int`
- `easy showAnything`
- `Float`
- `FluxResolutionNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（46/50）

**有卡**：`LTXVConditioning`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`CM_FloatToInt`、`CFGGuider`、`RandomNoise`、`GemmaAPITextEncode`、`ManualSigmas`、`KSamplerSelect`、`LTXAddVideoICLoRAGuide`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`ImageConcanate`、`Switch image [Crystools]`、`Color Correct (mtb)`、`VAEDecodeTiled`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`GetImageSize`、`GetImageSize+`、`ImageResizeKJv2`、`VHS_VideoCombine`、`PrimitiveBoolean`、`LTXICLoRALoaderModelOnly`、`LTXVImgToVideoConditionOnly`、`LoadImage`、`VHS_LoadVideo`、`ResizeAndPadImage`、`VHS_VideoInfo`、`Int`、`Float`、`FluxResolutionNode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
