---
key: 视频生成/图生视频/ltx2.3多模态参考玩法（多图参考+音频参考+视频运镜参考）_2081402967902744578.json
name: ltx2.3多模态参考玩法（多图参考+音频参考+视频运镜参考）_2081402967902744578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2081402967902744578.json
hash: 2316509b0715d477
coverage: 0.84375
learned_at: 2026-10-15 22:42:22
nodes: [ManualSigmas, CLIPLoader, SamplerCustomAdvanced, VAELoader, UNETLoader, LTXAVTextEncoderLoader, CFGGuider, LTXVConditioning, LTXVAudioVAELoader, LTXFloatToInt, VAEEncode, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, Flux2Scheduler, EmptySD3LatentImage, KSamplerSelect, CFGGuider, RandomNoise, ConditioningZeroOut, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, easy showAnything, SetLatentNoiseMask, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, RandomNoise, easy showAnything, easy showAnything, LoraLoaderModelOnly, ReferenceLatent, LTXVImgToVideoConditionOnly, LTXVCropGuides, LoraLoaderModelOnly, VHS_VideoInfoLoaded, easy showAnything, ImageResizeKJv2, AspectRatio, easy showAnything, easy showAnything, easy imageRemBg, SolidMask, LTXVAudioVAEEncode, easy showAnything, MultiplicationNode, PrimitiveFloat, PrimitiveInt, easy showAnything, ComfySwitchNode, LTXIdentityOverlapConditioning, LTXVTiledVAEDecode, LTXVAudioVAEDecode, CreateVideo, ImageResizeKJv2, easy imageRemBg, ImageResizeKJv2, SimpleMath+, ImageConcatMulti, TrimAudioDuration, PreviewAudio, easy showAnything, SimpleMath+, ResizeLongestToNode, easy showAnything, VHS_VideoCombine, Int, ResizeImageMaskNode, ImageResizeKJv2, easy showAnything, LTXVPreprocess, ImageResizeKJv2, ImageFromBatch+, GetImageSize, Fast Bypasser (rgthree), LTXICLoRALoaderModelOnly, LTXAddVideoICLoRAGuide, PrimitiveBoolean, Qwen3_VQA_Plus, workflow>提示词组和, easy showAnything, Float, LoadImage, LoadImage, LoadImage, LoadAudio, VHS_LoadVideo, SaveVideo, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/ltx2.3多模态参考玩法（多图参考+音频参考+视频运镜参考）_2081402967902744578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081402967902744578.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
- `ManualSigmas`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `LTXVConditioning`
- `LTXVAudioVAELoader`
- `LTXFloatToInt`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Flux2Scheduler`
- `EmptySD3LatentImage`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `EmptyLTXVLatentVideo`
- `KSamplerSelect` ★核心
- `easy showAnything`
- `SetLatentNoiseMask`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `easy showAnything`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `ImageResizeKJv2`
- `AspectRatio`
- `easy showAnything`
- `easy showAnything`
- `easy imageRemBg`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `easy showAnything`
- `MultiplicationNode`
- `PrimitiveFloat`
- `PrimitiveInt`
- `easy showAnything`
- `ComfySwitchNode`
- `LTXIdentityOverlapConditioning`
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `ImageResizeKJv2`
- `SimpleMath+`
- `ImageConcatMulti`
- `TrimAudioDuration`
- `PreviewAudio`
- `easy showAnything`
- `SimpleMath+`
- `ResizeLongestToNode`
- `easy showAnything`
- `VHS_VideoCombine`
- `Int`
- `ResizeImageMaskNode`
- `ImageResizeKJv2`
- `easy showAnything`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `GetImageSize`
- `Fast Bypasser (rgthree)`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAddVideoICLoRAGuide`
- `PrimitiveBoolean`
- `Qwen3_VQA_Plus`
- `workflow>提示词组和`
- `easy showAnything`
- `Float`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `VHS_LoadVideo`
- `SaveVideo`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（81/96）

**有卡**：`ManualSigmas`、`CLIPLoader`、`SamplerCustomAdvanced`、`VAELoader`、`UNETLoader`、`LTXAVTextEncoderLoader`、`CFGGuider`、`LTXVConditioning`、`LTXVAudioVAELoader`、`LTXFloatToInt`、`VAEEncode`、`ReferenceLatent`、`Flux2Scheduler`、`EmptySD3LatentImage`、`KSamplerSelect`、`RandomNoise`、`ConditioningZeroOut`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVImgToVideoConditionOnly`、`LTXVCropGuides`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`AspectRatio`、`easy imageRemBg`、`SolidMask`、`LTXVAudioVAEEncode`、`MultiplicationNode`、`LTXIdentityOverlapConditioning`、`LTXVTiledVAEDecode`、`LTXVAudioVAEDecode`、`CreateVideo`、`SimpleMath+`、`ImageConcatMulti`、`TrimAudioDuration`、`PreviewAudio`、`ResizeLongestToNode`、`VHS_VideoCombine`、`Int`、`ResizeImageMaskNode`、`LTXVPreprocess`、`ImageFromBatch+`、`GetImageSize`、`Fast Bypasser (rgthree)`、`LTXICLoRALoaderModelOnly`、`LTXAddVideoICLoRAGuide`、`PrimitiveBoolean`、`Qwen3_VQA_Plus`、`workflow>提示词组和`、`Float`、`LoadImage`、`LoadAudio`、`VHS_LoadVideo`、`SaveVideo`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
