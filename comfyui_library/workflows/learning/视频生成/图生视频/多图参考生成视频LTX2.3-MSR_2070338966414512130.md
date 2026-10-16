---
key: 视频生成/图生视频/多图参考生成视频LTX2.3-MSR_2070338966414512130.json
name: 多图参考生成视频LTX2.3-MSR_2070338966414512130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070338966414512130.json
hash: 89006382566974af
coverage: 0.945946
learned_at: 2026-10-15 22:40:38
nodes: [KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, SamplerCustom, CLIPTextEncode, VAELoaderKJ, VAELoaderKJ, VAEDecodeTiled, LTXVAudioVAEDecode, LTXAddVideoICLoRAGuide, BasicScheduler, Reroute, SimpleMath+, VHS_VideoCombine, LTX2_NAG, UNETLoader, LTXICLoRALoaderModelOnly, VHS_VideoCombine, LiconMSR, INTConstant, INTConstant, LoadImage, INTConstant, LTXVConditioning, MathExpression|pysssss, MathExpression|pysssss, Float, PrimitiveInt, DualCLIPLoader, CLIPTextEncode, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/多图参考生成视频LTX2.3-MSR_2070338966414512130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070338966414512130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（37 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXAddVideoICLoRAGuide`
- `BasicScheduler`
- `Reroute`
- `SimpleMath+`
- `VHS_VideoCombine`
- `LTX2_NAG`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LiconMSR`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `LTXVConditioning`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Float`
- `PrimitiveInt`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`SamplerCustom`、`CLIPTextEncode`、`VAELoaderKJ`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXAddVideoICLoRAGuide`、`BasicScheduler`、`SimpleMath+`、`VHS_VideoCombine`、`LTX2_NAG`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`LiconMSR`、`INTConstant`、`LoadImage`、`LTXVConditioning`、`MathExpression|pysssss`、`Float`、`DualCLIPLoader`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled
