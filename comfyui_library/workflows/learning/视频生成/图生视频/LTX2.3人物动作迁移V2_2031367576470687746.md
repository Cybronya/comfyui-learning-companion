---
key: 视频生成/图生视频/LTX2.3人物动作迁移V2_2031367576470687746.json
name: LTX2.3人物动作迁移V2_2031367576470687746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3人物动作迁移V2_2031367576470687746.json
hash: 2929a8877baf89ac
coverage: 0.918033
learned_at: 2026-10-15 22:35:31
nodes: [PrimitiveStringMultiline, VAEDecodeTiled, LTXVCropGuides, RandomNoise, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, easy convertAnything, LTXVAudioVAEDecode, ShowText|pysssss, Qwen3ASRLoader, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVConditioning, VHS_VideoCombine, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, PrimitiveInt, ResizeImageMaskNode, VHS_VideoInfoLoaded, ResizeImageMaskNode, ShowText|pysssss, LTXVPreprocess, LTXVPreprocess, LTXVAudioVAEEncode, SetLatentNoiseMask, ResizeImageMaskNode, GetImageSize, MathExpression|pysssss, EmptyLTXVLatentVideo, easy downloadIndexTTSAndLoadModel, SolidMask, PreviewAudio, Qwen3ASRTranscribe, MelBandRoFormerSampler, easy indexTTSGenerateSimple, easy indexTTSEmotionAudio, CR Text, easy ifElse, easy cleanGpuUsed, LoadAudio, VHS_LoadVideo, llama_cpp_instruct_adv, llama_cpp_model_loader, LoadImage, LoadImage, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, UNETLoader, MelBandRoFormerModelLoader, LTXVAddGuideMulti, ManualSigmas, ManualSigmas, LTX2_NAG]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3人物动作迁移V2_2031367576470687746.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031367576470687746.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `PrimitiveStringMultiline`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `easy convertAnything`
- `LTXVAudioVAEDecode` ★核心
- `ShowText|pysssss`
- `Qwen3ASRLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `VHS_VideoInfoLoaded`
- `ResizeImageMaskNode`
- `ShowText|pysssss`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `GetImageSize`
- `MathExpression|pysssss`
- `EmptyLTXVLatentVideo`
- `easy downloadIndexTTSAndLoadModel`
- `SolidMask`
- `PreviewAudio`
- `Qwen3ASRTranscribe`
- `MelBandRoFormerSampler` ★核心
- `easy indexTTSGenerateSimple`
- `easy indexTTSEmotionAudio`
- `CR Text`
- `easy ifElse`
- `easy cleanGpuUsed`
- `LoadAudio`
- `VHS_LoadVideo`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `LoadImage`
- `LoadImage`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `MelBandRoFormerModelLoader`
- `LTXVAddGuideMulti`
- `ManualSigmas`
- `ManualSigmas`
- `LTX2_NAG`

## 知识

覆盖率 **92%**（56/61）

**有卡**：`VAEDecodeTiled`、`LTXVCropGuides`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`easy convertAnything`、`LTXVAudioVAEDecode`、`Qwen3ASRLoader`、`CLIPTextEncode`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`VHS_VideoInfoLoaded`、`LTXVPreprocess`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`GetImageSize`、`MathExpression|pysssss`、`EmptyLTXVLatentVideo`、`easy downloadIndexTTSAndLoadModel`、`SolidMask`、`PreviewAudio`、`Qwen3ASRTranscribe`、`MelBandRoFormerSampler`、`easy indexTTSGenerateSimple`、`easy indexTTSEmotionAudio`、`CR Text`、`easy cleanGpuUsed`、`LoadAudio`、`VHS_LoadVideo`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`LoadImage`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`MelBandRoFormerModelLoader`、`LTXVAddGuideMulti`、`ManualSigmas`、`LTX2_NAG`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent
