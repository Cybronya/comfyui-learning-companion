---
key: 视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V1_2016740203737653250.json
name: InfiniteTalk 2.1+2.2混用高动态图生视频数字人V1_2016740203737653250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016740203737653250.json
hash: e54dbb3500d87f7a
coverage: 0.921053
learned_at: 2026-10-15 22:34:43
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, AudioEncoderLoader, ModelPatchLoader, KSamplerAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM, PreviewAny, KSamplerAdvanced, RIFE VFI, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, PainterAI2V, VAEDecode, easy seed, JWInteger, CLIPTextEncode, CR Prompt Text, LoadAudio, LoadImage, AudioEncoderEncode, PainterAudioCut, JWInteger, JWInteger, Note, Note, ColorMatch, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "dpmpp_sde", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V1_2016740203737653250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016740203737653250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `AudioEncoderLoader`
- `ModelPatchLoader`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `PreviewAny`
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PainterAI2V`
- `VAEDecode` ★核心
- `easy seed`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `LoadAudio`
- `LoadImage`
- `AudioEncoderEncode`
- `PainterAudioCut`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `ColorMatch`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_sde`
- `denoise` = `normal`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`AudioEncoderLoader`、`ModelPatchLoader`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`RIFE VFI`、`VHS_VideoCombine`、`PainterAI2V`、`VAEDecode`、`easy seed`、`JWInteger`、`CR Prompt Text`、`LoadAudio`、`LoadImage`、`AudioEncoderEncode`、`PainterAudioCut`、`ColorMatch`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
