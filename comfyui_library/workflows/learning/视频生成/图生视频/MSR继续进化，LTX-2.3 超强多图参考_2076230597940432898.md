---
key: 视频生成/图生视频/MSR继续进化，LTX-2.3 超强多图参考_2076230597940432898.json
name: MSR继续进化，LTX-2.3 超强多图参考_2076230597940432898.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MSR继续进化，LTX-2.3 超强多图参考_2076230597940432898.json
hash: 8efb89477ada11d4
coverage: 0.895833
learned_at: 2026-10-15 22:41:29
nodes: [llama_cpp_instruct_adv, CLIPTextEncode, PreviewImage, LTXVConditioning, llama_cpp_model_loader, llama_cpp_parameters, CLIPTextEncode, LTXVEmptyLatentAudio, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVCropGuides, CR Prompt Text, VAEDecode, ShowText|pysssss, EmptyLTXVLatentVideo, PrimitiveInt, SimpleMath+, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CR Prompt Text, INTConstant, INTConstant, PrimitiveInt, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXICLoRALoaderModelOnly, LiconMSR, LTXAddVideoICLoRAGuide, VHS_VideoCombine, PreviewImage, LowVRAMCheckpointLoader, LoadImage, KenChenLLMGeminiBananaImageCollageNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/MSR继续进化，LTX-2.3 超强多图参考_2076230597940432898.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076230597940432898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LTXVConditioning`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVCropGuides`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `SimpleMath+`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CR Prompt Text`
- `INTConstant`
- `INTConstant`
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `LiconMSR`
- `LTXAddVideoICLoRAGuide`
- `VHS_VideoCombine`
- `PreviewImage`
- `LowVRAMCheckpointLoader` ★核心
- `LoadImage`
- `KenChenLLMGeminiBananaImageCollageNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **90%**（43/48）

**有卡**：`llama_cpp_instruct_adv`、`CLIPTextEncode`、`LTXVConditioning`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVCropGuides`、`CR Prompt Text`、`VAEDecode`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`INTConstant`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTXICLoRALoaderModelOnly`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`VHS_VideoCombine`、`LowVRAMCheckpointLoader`、`LoadImage`、`KenChenLLMGeminiBananaImageCollageNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerSelect`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
