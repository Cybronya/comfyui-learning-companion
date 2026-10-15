---
key: 视频生成/文生视频/LTX-2.3_双角色设定集参考 + 自定义音频 视频生成工作流_2064203596383735809.json
name: LTX-2.3_双角色设定集参考 + 自定义音频 视频生成工作流_2064203596383735809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3_双角色设定集参考 + 自定义音频 视频生成工作流_2064203596383735809.json
hash: 406d142c33cf668a
coverage: 0.506024
learned_at: 2026-10-15 22:44:42
nodes: [LTXVCropGuides, LTXVConditioning, GetNode, GetNode, SolidMask, GetNode, SetNode, SetNode, PathchSageAttentionKJ, SetNode, SetNode, LTXVConcatAVLatent, GetNode, SetLatentNoiseMask, SetNode, Any Switch (rgthree), GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), GetNode, LTXAddVideoICLoRAGuide, GetNode, GetNode, SetNode, PrimitiveInt, SetNode, CR Float To Integer, PrimitiveFloat, GetNode, SetNode, EmptyLTXVLatentVideo, SetNode, GetImageSize, ResizeImageMaskNode, KSamplerSelect, SamplerCustomAdvanced, CFGGuider, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecode, MathExpression|pysssss, LiconMSR, ResizeImageMaskNode, SetNode, SetNode, RandomNoise, PrimitiveInt, ResizeImageMaskNode, VHS_VideoCombine, GetNode, CLIPTextEncode, SetNode, SetNode, SetNode, LTXVAudioVAEEncode, VHS_LoadAudio, PromptRelayEncode, VAELoader, LTXVAudioVAELoader, DualCLIPLoader, LTXVEmptyLatentAudio, GetNode, LoadImage, LoadImage, LoadImage, Note, ManualSigmas, Note, GetNode, GetImageSize, GetNode, GetNode, ComfyNumberConvert, Note, Note, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadAudio, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 505}
---

# 视频生成/文生视频/LTX-2.3_双角色设定集参考 + 自定义音频 视频生成工作流_2064203596383735809.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3_双角色设定集参考 + 自定义音频 视频生成工作流_2064203596383735809.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（83 个）：
- `LTXVCropGuides`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetLatentNoiseMask`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `CR Float To Integer`
- `PrimitiveFloat`
- `GetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetImageSize`
- `ResizeImageMaskNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `MathExpression|pysssss`
- `LiconMSR`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `VHS_VideoCombine`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `VHS_LoadAudio`
- `PromptRelayEncode`
- `VAELoader`
- `LTXVAudioVAELoader`
- `DualCLIPLoader`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `ManualSigmas`
- `Note`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `ComfyNumberConvert`
- `Note`
- `Note`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `505`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **51%**（42/83）

**有卡**：`LTXVCropGuides`、`LTXVConditioning`、`SolidMask`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LTXAddVideoICLoRAGuide`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`GetImageSize`、`ResizeImageMaskNode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`MathExpression|pysssss`、`LiconMSR`、`RandomNoise`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`VHS_LoadAudio`、`PromptRelayEncode`、`VAELoader`、`LTXVAudioVAELoader`、`DualCLIPLoader`、`LTXVEmptyLatentAudio`、`LoadImage`、`ManualSigmas`、`ComfyNumberConvert`、`LoadAudio`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
