---
key: 视频生成/文生视频/LTX2.3文生视频【根据时间写剧情】_2067564577201672194.json
name: LTX2.3文生视频【根据时间写剧情】_2067564577201672194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【根据时间写剧情】_2067564577201672194.json
hash: 363fa0fedc6ffd02
coverage: 0.827586
learned_at: 2026-10-11 20:21:27
nodes: [Int, PrimitiveFloat, PrimitiveInt, LTXVConcatAVLatent, RandomNoise, Int, CLIPTextEncode, VRAMReserver, VAELoaderKJ, easy cleanGpuUsed, CLIPTextEncode, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, GetImageSize, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, KSamplerSelect, KSamplerSelect, VAELoaderKJ, ImageScaleBy, easy convertAnything, easy cleanGpuUsed, easy cleanGpuUsed, LoraLoaderModelOnly, LTXVLatentUpsampler, CFGGuider, LTXVConditioning, SamplerCustomAdvanced, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, DualCLIPLoader, easy cleanGpuUsed, LTXVCropGuides, Int, LTXVConcatAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, ManualSigmas, CFGGuider, BasicScheduler, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, LTXVScheduler, easy cleanGpuUsed, Int, CreateVideo, SaveVideo, CR Text, PIP_IntegerCalculator, LTXICLoRALoaderModelOnly]
patterns: []
missing: [CR Text, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy convertAnything]
parameters: {"batch_size": 1, "height": 25, "width": 121}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3文生视频【根据时间写剧情】_2067564577201672194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【根据时间写剧情】_2067564577201672194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
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
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
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
- `easy cleanGpuUsed`
- `Int`
- `CreateVideo`
- `SaveVideo`
- `CR Text`
- `PIP_IntegerCalculator`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（48/58）

**有卡**：`Int`、`LTXVConcatAVLatent`、`RandomNoise`、`CLIPTextEncode`、`VRAMReserver`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`PIP_IntegerCalculator`、`EmptyImage`、`GetImageSize`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`ImageScaleBy`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`CFGGuider`、`LTXVConditioning`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LTX2_NAG`、`ManualSigmas`、`BasicScheduler`、`VHS_VideoCombine`、`UNETLoader`、`LTXVScheduler`、`CreateVideo`、`SaveVideo`、`LTXICLoRALoaderModelOnly`

**缺卡**（7）：`CR Text`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy convertAnything`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
