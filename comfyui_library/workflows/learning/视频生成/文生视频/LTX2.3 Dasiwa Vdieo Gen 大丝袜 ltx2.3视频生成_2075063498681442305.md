---
key: 视频生成/文生视频/LTX2.3 Dasiwa Vdieo Gen 大丝袜 ltx2.3视频生成_2075063498681442305.json
name: LTX2.3 Dasiwa Vdieo Gen 大丝袜 ltx2.3视频生成_2075063498681442305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 Dasiwa Vdieo Gen 大丝袜 ltx2.3视频生成_2075063498681442305.json
hash: 26daf72818410762
coverage: 0.588889
learned_at: 2026-10-15 22:44:57
nodes: [PathchSageAttentionKJ, LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, SetNode, VAELoaderKJ, VAELoader, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, ModelPatchTorchSettings, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, BasicScheduler, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVPreprocess, LTXVConditioning, GetNode, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, CLIPTextEncode, SetNode, SetNode, GetNode, VAEDecode, ManualSigmas, LTXVEmptyLatentAudio, SimpleCalculatorKJ, GetNode, GetNode, GetNode, LTXVCropGuides, CFGGuider, CFGGuider, GetNode, LTXVConcatAVLatent, LTXVImgToVideoInplace, Note, UNETLoader, DualCLIPLoader, SetNode, Fast Groups Bypasser (rgthree), Note, easy cleanGpuUsed, llama_cpp_instruct_adv, Note, CLIPTextEncode, Fast Groups Bypasser (rgthree), RandomNoise, GetNode, LTXVLatentUpsampler, llama_cpp_model_loader, ImageResizeKJv2, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, PrimitiveStringMultiline, PrimitiveStringMultiline, ShowText|pysssss, PrimitiveBoolean, LoadImage, PrimitiveStringMultiline, ImageScaleBy, GetImageSize, SetNode, PrimitiveFloat, INTConstant, SimpleCalculatorKJ, SimpleMath+, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/文生视频/LTX2.3 Dasiwa Vdieo Gen 大丝袜 ltx2.3视频生成_2075063498681442305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 Dasiwa Vdieo Gen 大丝袜 ltx2.3视频生成_2075063498681442305.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `PathchSageAttentionKJ`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `ModelPatchTorchSettings`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `CFGGuider`
- `CFGGuider`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `Note`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `RandomNoise`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `llama_cpp_model_loader`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `PrimitiveBoolean`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImageScaleBy`
- `GetImageSize`
- `SetNode`
- `PrimitiveFloat`
- `INTConstant`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **59%**（53/90）

**有卡**：`PathchSageAttentionKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`VAELoaderKJ`、`VAELoader`、`LatentUpscaleModelLoader`、`ModelPatchTorchSettings`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`KSamplerSelect`、`BasicScheduler`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`VAEDecode`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`LTXVCropGuides`、`CFGGuider`、`UNETLoader`、`DualCLIPLoader`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`RandomNoise`、`LTXVLatentUpsampler`、`llama_cpp_model_loader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`PrimitiveBoolean`、`LoadImage`、`ImageScaleBy`、`GetImageSize`、`INTConstant`、`SimpleMath+`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
