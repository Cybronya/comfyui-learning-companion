---
key: 视频生成/图生视频/Smooth Mix 2.0 混合 LightX2V 3图多帧控制_1985359491870900226.json
name: Smooth Mix 2.0 混合 LightX2V 3图多帧控制_1985359491870900226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth Mix 2.0 混合 LightX2V 3图多帧控制_1985359491870900226.json
hash: 22132ae3771470cd
coverage: 0.933333
learned_at: 2026-10-15 22:32:50
nodes: [LayerUtility: PurgeVRAM, KSamplerAdvanced, Note, CLIPTextEncode, VAELoader, JWInteger, PrimitiveNode, CLIPTextEncode, CLIPLoader, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, UNETLoader, ImageResize+, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionEncode, LoadImage, LoadImage, LoadImage, ImageResize+, CR Prompt Text, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, WanFirstMiddleLastFrameToVideo, ModelSamplingSD3, ModelSamplingSD3, ColorMatch, VHS_VideoCombine, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Smooth Mix 2.0 混合 LightX2V 3图多帧控制_1985359491870900226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985359491870900226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `JWInteger`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageResize+`
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstMiddleLastFrameToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ColorMatch`
- `VHS_VideoCombine`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`CLIPTextEncode`、`VAELoader`、`JWInteger`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`、`ImageResize+`、`LoadImage`、`CR Prompt Text`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstMiddleLastFrameToVideo`、`ModelSamplingSD3`、`ColorMatch`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
