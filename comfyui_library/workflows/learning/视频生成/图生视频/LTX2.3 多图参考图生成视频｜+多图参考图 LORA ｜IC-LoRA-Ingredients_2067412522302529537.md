---
key: 视频生成/图生视频/LTX2.3 多图参考图生成视频｜+多图参考图 LORA ｜IC-LoRA-Ingredients_2067412522302529537.json
name: LTX2.3 多图参考图生成视频｜+多图参考图 LORA ｜IC-LoRA-Ingredients_2067412522302529537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067412522302529537.json
hash: 829aaeb0af3c5ba9
coverage: 0.785714
learned_at: 2026-10-15 22:40:01
nodes: [SamplerCustomAdvanced, LTXVSeparateAVLatent, GetVideoComponents, ResizeImageMaskNode, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXVPreprocess, GetImageSize, RepeatImageBatch, CreateVideo, LTXFloatToInt, LoadImage, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXAddVideoICLoRAGuide, CFGGuider, KSamplerSelect, RandomNoise, LTXVAudioVAEDecode, LTXVCropGuides, CreateVideo, LTXVTiledVAEDecode, ManualSigmas, SaveVideo, Note, CLIPTextEncode, Note, Note, easy showAnything, PrimitiveFloat, PrimitiveFloat, Note, Note, SimpleCalculatorKJ, CLIPTextEncode, LTXVConditioning, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3 多图参考图生成视频｜+多图参考图 LORA ｜IC-LoRA-Ingredients_2067412522302529537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067412522302529537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetVideoComponents`
- `ResizeImageMaskNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXVPreprocess`
- `GetImageSize`
- `RepeatImageBatch`
- `CreateVideo`
- `LTXFloatToInt`
- `LoadImage`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXAddVideoICLoRAGuide`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `CreateVideo`
- `LTXVTiledVAEDecode` ★核心
- `ManualSigmas`
- `SaveVideo`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `easy showAnything`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Note`
- `Note`
- `SimpleCalculatorKJ`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`GetVideoComponents`、`ResizeImageMaskNode`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVPreprocess`、`GetImageSize`、`RepeatImageBatch`、`CreateVideo`、`LTXFloatToInt`、`LoadImage`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXVTiledVAEDecode`、`ManualSigmas`、`SaveVideo`、`CLIPTextEncode`、`SimpleCalculatorKJ`、`LTXVConditioning`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
