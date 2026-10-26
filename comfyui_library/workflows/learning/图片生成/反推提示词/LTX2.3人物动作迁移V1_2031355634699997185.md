---
key: 图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json
name: LTX2.3人物动作迁移V1_2031355634699997185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json
hash: 4607ad7a799abd86
coverage: 0.949153
learned_at: 2026-10-26 01:45:32
nodes: [PrimitiveStringMultiline, ModelPatchTorchSettings, LTXVChunkFeedForward, VAEDecodeTiled, LTXVCropGuides, RandomNoise, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, easy convertAnything, PathchSageAttentionKJ, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, easy imageSizeBySide, MathExpression|pysssss, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTX2_NAG, ResizeImagesByLongerEdge, LTXVPreprocess, SolidMask, LTXVConditioning, SetLatentNoiseMask, LTXVImgToVideoConditionOnly, LTXVAudioVAEEncode, VHS_VideoInfoLoaded, PrimitiveInt, ResizeImageMaskNode, ShowText|pysssss, easy indexTTSGenerateSimple, easy indexTTSEmotionAudio, CR Text, PreviewAudio, VHS_VideoCombine, ResizeImageMaskNode, easy cleanGpuUsed, llama_cpp_model_loader, LoadAudio, VHS_LoadVideo, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, DWPreprocessor, LTXICLoRALoaderModelOnly, MelBandRoFormerSampler, ManualSigmas, ManualSigmas, LoadImage, LTXAddVideoICLoRAGuide, MelBandRoFormerModelLoader, GetImageSize, ResizeImageMaskNode, llama_cpp_instruct_adv, easy downloadIndexTTSAndLoadModel]
patterns: []
missing: []
---

# 图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `PrimitiveStringMultiline`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `easy convertAnything`
- `PathchSageAttentionKJ`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `easy imageSizeBySide`
- `MathExpression|pysssss`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SolidMask`
- `LTXVConditioning`
- `SetLatentNoiseMask`
- `LTXVImgToVideoConditionOnly`
- `LTXVAudioVAEEncode` ★核心
- `VHS_VideoInfoLoaded`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `ShowText|pysssss`
- `easy indexTTSGenerateSimple`
- `easy indexTTSEmotionAudio`
- `CR Text`
- `PreviewAudio`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `easy cleanGpuUsed`
- `llama_cpp_model_loader`
- `LoadAudio`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `DWPreprocessor`
- `LTXICLoRALoaderModelOnly` ★核心
- `MelBandRoFormerSampler` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `LoadImage`
- `LTXAddVideoICLoRAGuide`
- `MelBandRoFormerModelLoader`
- `GetImageSize`
- `ResizeImageMaskNode`
- `llama_cpp_instruct_adv`
- `easy downloadIndexTTSAndLoadModel`

## 知识

覆盖率 **95%**（56/59）

**有卡**：`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`VAEDecodeTiled`、`LTXVCropGuides`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`easy convertAnything`、`PathchSageAttentionKJ`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`easy imageSizeBySide`、`MathExpression|pysssss`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`SolidMask`、`LTXVConditioning`、`SetLatentNoiseMask`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEEncode`、`VHS_VideoInfoLoaded`、`ResizeImageMaskNode`、`easy indexTTSGenerateSimple`、`easy indexTTSEmotionAudio`、`CR Text`、`PreviewAudio`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`LoadAudio`、`VHS_LoadVideo`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`DWPreprocessor`、`LTXICLoRALoaderModelOnly`、`MelBandRoFormerSampler`、`LoadImage`、`LTXAddVideoICLoRAGuide`、`MelBandRoFormerModelLoader`、`GetImageSize`、`llama_cpp_instruct_adv`、`easy downloadIndexTTSAndLoadModel`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent
