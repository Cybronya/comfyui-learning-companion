---
key: 视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V2(动态加强)_2017231057254354945.json
name: InfiniteTalk 2.1+2.2混用高动态图生视频数字人V2(动态加强)_2017231057254354945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017231057254354945.json
hash: 51fd11bb193be1ca
coverage: 0.921053
learned_at: 2026-10-15 22:34:45
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, AudioEncoderLoader, ModelPatchLoader, KSamplerAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM, PreviewAny, VHS_VideoCombine, PainterAI2V, VAEDecode, JWInteger, CLIPTextEncode, AudioEncoderEncode, PainterAudioCut, Note, Note, JWInteger, JWInteger, RIFE VFI, ColorMatch, LoadImage, CR Prompt Text, LoadAudio, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy seed]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "dpmpp_sde", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V2(动态加强)_2017231057254354945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017231057254354945.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
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
- `VHS_VideoCombine`
- `PainterAI2V`
- `VAEDecode` ★核心
- `JWInteger`
- `CLIPTextEncode` ★核心
- `AudioEncoderEncode`
- `PainterAudioCut`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `RIFE VFI`
- `ColorMatch`
- `LoadImage`
- `CR Prompt Text`
- `LoadAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy seed`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_sde`
- `denoise` = `normal`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`AudioEncoderLoader`、`ModelPatchLoader`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`PainterAI2V`、`VAEDecode`、`JWInteger`、`AudioEncoderEncode`、`PainterAudioCut`、`RIFE VFI`、`ColorMatch`、`LoadImage`、`CR Prompt Text`、`LoadAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoraLoaderModelOnly`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
