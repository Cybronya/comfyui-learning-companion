---
key: 视频生成/图生视频/wan（Remix_smooth_dasiwa）+PainterI2V图生视频手动提示词工作流V1_2016325482970615810.json
name: wan（Remix_smooth_dasiwa）+PainterI2V图生视频手动提示词工作流V1_2016325482970615810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan（Remix_smooth_dasiwa）+PainterI2V图生视频手动提示词工作流V1_2016325482970615810.json
hash: 7bed50334db27075
coverage: 0.723404
learned_at: 2026-10-15 22:34:42
nodes: [Note, Note, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPVisionLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, ImageResizeKJv2, VAEDecode, LayerUtility: PurgeVRAM, FILM VFI, Note, Note, Note, Note, Note, Note, Note, Note, PainterI2V, LayerUtility: PurgeVRAM, CLIPLoader, JWInteger, CLIPVisionEncode, LayerUtility: PurgeVRAM, VHS_VideoCombine, CLIPTextEncode, Float, Note, UNETLoader, UNETLoader, KSamplerAdvanced, Seed (rgthree), LoadImage, AILab_QwenVL, easy showAnything, CR Prompt Text, easy showAnything, JWInteger, UNETLoader, UNETLoader, RH_LLMAPI_NODE, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan（Remix_smooth_dasiwa）+PainterI2V图生视频手动提示词工作流V1_2016325482970615810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016325482970615810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `Note`
- `Note`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPVisionLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `FILM VFI`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `PainterI2V`
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `JWInteger`
- `CLIPVisionEncode`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Float`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `LoadImage`
- `AILab_QwenVL`
- `easy showAnything`
- `CR Prompt Text`
- `easy showAnything`
- `JWInteger`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（34/47）

**有卡**：`PathchSageAttentionKJ`、`CLIPVisionLoader`、`VAELoader`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`ImageResizeKJv2`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`FILM VFI`、`PainterI2V`、`CLIPLoader`、`JWInteger`、`CLIPVisionEncode`、`VHS_VideoCombine`、`CLIPTextEncode`、`Float`、`UNETLoader`、`Seed (rgthree)`、`LoadImage`、`AILab_QwenVL`、`CR Prompt Text`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
