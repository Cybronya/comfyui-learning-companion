---
key: 视频生成/图生视频/LTX2.3-MSR全能参考自定义音频（参考图反推）_2069220320195731457.json
name: LTX2.3-MSR全能参考自定义音频（参考图反推）_2069220320195731457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069220320195731457.json
hash: 1b3f89955743c042
coverage: 0.913793
learned_at: 2026-10-15 22:40:26
nodes: [KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, VisualizeSigmasKJ, CLIPTextEncode, VAELoaderKJ, VAEDecodeTiled, LTXAddVideoICLoRAGuide, VHS_VideoCombine, INTConstant, LiconMSR, INTConstant, Float, VAELoaderKJ, LTXVConcatAVLatent, SamplerCustom, LTXVEmptyLatentAudio, SimpleMath+, BasicScheduler, ComfySwitchNode, LTXVAudioVAEDecode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, ComfySwitchNode, Reroute, LoadAudio, LoadAudioUI, SimpleMath+, SimpleMath+, INTConstant, UNETLoader, LTX2_NAG, DualCLIPLoader, LTX2SamplingPreviewOverride, LTXVConditioning, EmptyLTXVLatentVideo, Textbox, ComfySwitchNode, CLIPTextEncode, LTXICLoRALoaderModelOnly, 忽略多组孤海, llama_cpp_model_loader, PrimitiveBoolean, llama_cpp_parameters, Float, Textbox, ComfySwitchNode, VHS_VideoCombine, llama_cpp_instruct_adv, LoadImage, Textbox, PrimitiveBoolean, PrimitiveBoolean, LoadImage, Textbox, Textbox, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 241}
---

# 视频生成/图生视频/LTX2.3-MSR全能参考自定义音频（参考图反推）_2069220320195731457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069220320195731457.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（58 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VisualizeSigmasKJ`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `VHS_VideoCombine`
- `INTConstant`
- `LiconMSR`
- `INTConstant`
- `Float`
- `VAELoaderKJ`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `BasicScheduler`
- `ComfySwitchNode`
- `LTXVAudioVAEDecode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `ComfySwitchNode`
- `Reroute`
- `LoadAudio`
- `LoadAudioUI`
- `SimpleMath+`
- `SimpleMath+`
- `INTConstant`
- `UNETLoader` ★核心
- `LTX2_NAG`
- `DualCLIPLoader`
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `Textbox`
- `ComfySwitchNode`
- `CLIPTextEncode` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `忽略多组孤海`
- `llama_cpp_model_loader`
- `PrimitiveBoolean`
- `llama_cpp_parameters`
- `Float`
- `Textbox`
- `ComfySwitchNode`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `Textbox`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `LoadImage`
- `Textbox`
- `Textbox`
- `LoadImage`

## 关键参数

- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（53/58）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`VisualizeSigmasKJ`、`CLIPTextEncode`、`VAELoaderKJ`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`VHS_VideoCombine`、`INTConstant`、`LiconMSR`、`Float`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`BasicScheduler`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LoadAudio`、`LoadAudioUI`、`UNETLoader`、`LTX2_NAG`、`DualCLIPLoader`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`Textbox`、`LTXICLoRALoaderModelOnly`、`忽略多组孤海`、`llama_cpp_model_loader`、`PrimitiveBoolean`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask
