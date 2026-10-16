---
key: 视频生成/图生视频/全自动LTX-2.3_MSR 多图参考高动态图生视频工作流_2064250965800349698.json
name: 全自动LTX-2.3_MSR 多图参考高动态图生视频工作流_2064250965800349698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064250965800349698.json
hash: 9dd953a8405a818f
coverage: 0.830189
learned_at: 2026-10-15 22:39:22
nodes: [UNETLoader, CLIPTextEncode, LTXAddVideoICLoRAGuide, LTXVConditioning, LTXVConcatAVLatent, LTXVSeparateAVLatent, Note, Note, Note, Note, LiconMSR, CLIPTextEncode, LoadImage, LoadImage, LoadImage, LoadImage, easy float, INTConstant, SimpleMath+, Note, Note, Note, Note, CR Text, CR Text Concatenate, llama_cpp_unload_model, llama_cpp_parameters, LayerUtility: PurgeVRAM V2, llama_cpp_instruct_adv, llama_cpp_model_loader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, PathchSageAttentionKJ, SamplerCustomAdvanced, LTXVAudioVAEDecode, KSamplerSelect, PreviewTextNode, VHS_VideoCombine, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CR Float To Integer, ManualSigmas, VAELoader, RandomNoise, LTXVCropGuides, CFGGuider, VAEDecodeTiled, CR Text, INTConstant, INTConstant, DualCLIPLoader, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/全自动LTX-2.3_MSR 多图参考高动态图生视频工作流_2064250965800349698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064250965800349698.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（53 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `Note`
- `Note`
- `Note`
- `Note`
- `LiconMSR`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy float`
- `INTConstant`
- `SimpleMath+`
- `Note`
- `Note`
- `Note`
- `Note`
- `CR Text`
- `CR Text Concatenate`
- `llama_cpp_unload_model`
- `llama_cpp_parameters`
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `PathchSageAttentionKJ`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `PreviewTextNode`
- `VHS_VideoCombine`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `CR Float To Integer`
- `ManualSigmas`
- `VAELoader`
- `RandomNoise`
- `LTXVCropGuides`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `CR Text`
- `INTConstant`
- `INTConstant`
- `DualCLIPLoader`
- `ShowText|pysssss`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（44/53）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LiconMSR`、`LoadImage`、`easy float`、`INTConstant`、`SimpleMath+`、`CR Text`、`CR Text Concatenate`、`llama_cpp_unload_model`、`llama_cpp_parameters`、`LayerUtility: PurgeVRAM V2`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`PreviewTextNode`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CR Float To Integer`、`ManualSigmas`、`VAELoader`、`RandomNoise`、`LTXVCropGuides`、`CFGGuider`、`VAEDecodeTiled`、`DualCLIPLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
