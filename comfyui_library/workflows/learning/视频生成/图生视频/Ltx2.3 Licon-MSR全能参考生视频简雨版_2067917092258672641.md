---
key: 视频生成/图生视频/Ltx2.3 Licon-MSR全能参考生视频简雨版_2067917092258672641.json
name: Ltx2.3 Licon-MSR全能参考生视频简雨版_2067917092258672641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 Licon-MSR全能参考生视频简雨版_2067917092258672641.json
hash: 2237410c0d8e643d
coverage: 0.893617
learned_at: 2026-10-15 22:40:14
nodes: [RandomNoise, JjkText, LTXAddVideoICLoRAGuide, LTXVConditioning, SamplerCustomAdvanced, SaveVideo, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, LTXVAudioVAELoader, llama_cpp_parameters, llama_cpp_model_loader, CR Prompt Text, PreviewAny, llama_cpp_instruct_adv, CR Text Concatenate, LTXVEmptyLatentAudio, easy positive, SetNode, LTXICLoRALoaderModelOnly, INTConstant, LoadImage, LoadImage, ImageBatchMultiple+, PreviewImage, LiconMSR, ImageConcatFromBatch, EmptyLTXVLatentVideo, INTConstant, INTConstant, GetNode, LTXVConcatAVLatent, ManualSigmas, LTXVAudioVAEDecode, LTXVSeparateAVLatent, CreateVideo, VAEDecode, LTXVCropGuides, CFGGuider, LoadImage, LoadImage, LoadImage, KSamplerSelect, DualCLIPLoaderGGUF, VAELoader, UNETLoader, LoaderGGUF]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/Ltx2.3 Licon-MSR全能参考生视频简雨版_2067917092258672641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067917092258672641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `RandomNoise`
- `JjkText`
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `LTXVAudioVAELoader`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `CR Prompt Text`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `CR Text Concatenate`
- `LTXVEmptyLatentAudio` ★核心
- `easy positive`
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `ImageBatchMultiple+`
- `PreviewImage`
- `LiconMSR`
- `ImageConcatFromBatch`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `CFGGuider`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSamplerSelect` ★核心
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `UNETLoader` ★核心
- `LoaderGGUF`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`RandomNoise`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`SamplerCustomAdvanced`、`SaveVideo`、`CLIPTextEncode`、`CR Prompt Text`、`LTXVAudioVAELoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`CR Text Concatenate`、`LTXVEmptyLatentAudio`、`easy positive`、`LTXICLoRALoaderModelOnly`、`INTConstant`、`LoadImage`、`ImageBatchMultiple+`、`LiconMSR`、`ImageConcatFromBatch`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`CreateVideo`、`VAEDecode`、`LTXVCropGuides`、`CFGGuider`、`KSamplerSelect`、`DualCLIPLoaderGGUF`、`VAELoader`、`UNETLoader`、`LoaderGGUF`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
