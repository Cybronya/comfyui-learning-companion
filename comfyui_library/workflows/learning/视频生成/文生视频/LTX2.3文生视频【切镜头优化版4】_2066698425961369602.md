---
key: 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2066698425961369602.json
name: LTX2.3文生视频【切镜头优化版4】_2066698425961369602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2066698425961369602.json
hash: 2c1b11b216401e34
coverage: 0.948276
learned_at: 2026-10-15 22:45:12
nodes: [PIP_IntegerCalculator, Int, PrimitiveFloat, PrimitiveInt, LTXVConcatAVLatent, RandomNoise, Int, CLIPTextEncode, VRAMReserver, VAELoaderKJ, easy cleanGpuUsed, CLIPTextEncode, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, GetImageSize, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, KSamplerSelect, KSamplerSelect, VAELoaderKJ, ImageScaleBy, easy convertAnything, Int, easy cleanGpuUsed, easy cleanGpuUsed, SaveVideo, LoraLoaderModelOnly, LTXVLatentUpsampler, CreateVideo, CFGGuider, LTXVConditioning, SamplerCustomAdvanced, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, DualCLIPLoader, easy cleanGpuUsed, LTXVCropGuides, Int, LTXVConcatAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, ManualSigmas, CFGGuider, BasicScheduler, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, LTXVScheduler, LTXICLoRALoaderModelOnly, easy cleanGpuUsed, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2066698425961369602.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2066698425961369602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `PIP_IntegerCalculator`
- `Int`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `Int`
- `CLIPTextEncode` ★核心
- `VRAMReserver`
- `VAELoaderKJ`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PIP_IntegerCalculator`
- `EmptyImage`
- `PrimitiveInt`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `ImageScaleBy`
- `easy convertAnything`
- `Int`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `CreateVideo`
- `CFGGuider`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `LTXVCropGuides`
- `Int`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `CFGGuider`
- `BasicScheduler`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `LTXICLoRALoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `CR Text`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（55/58）

**有卡**：`PIP_IntegerCalculator`、`Int`、`LTXVConcatAVLatent`、`RandomNoise`、`CLIPTextEncode`、`VRAMReserver`、`VAELoaderKJ`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`EmptyImage`、`GetImageSize`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`ImageScaleBy`、`easy convertAnything`、`SaveVideo`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`CreateVideo`、`CFGGuider`、`LTXVConditioning`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LTX2_NAG`、`ManualSigmas`、`BasicScheduler`、`VHS_VideoCombine`、`UNETLoader`、`LTXVScheduler`、`LTXICLoRALoaderModelOnly`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
