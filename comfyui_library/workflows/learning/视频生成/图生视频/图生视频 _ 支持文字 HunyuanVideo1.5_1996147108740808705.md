---
key: 视频生成/图生视频/图生视频 _ 支持文字 HunyuanVideo1.5_1996147108740808705.json
name: 图生视频 _ 支持文字 HunyuanVideo1.5_1996147108740808705.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 _ 支持文字 HunyuanVideo1.5_1996147108740808705.json
hash: 399488205b91b0ca
coverage: 1
learned_at: 2026-10-15 22:33:25
nodes: [CLIPVisionLoader, DualCLIPLoader, VAELoader, UNETLoader, VAEDecodeTiled, RandomNoise, KSamplerSelect, CFGGuider, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, HunyuanVideo15ImageToVideo, CLIPVisionEncode, EasyCache, ModelSamplingSD3, SamplerCustomAdvanced, DF_Int_to_Float, CreateVideo, SaveVideo, VAEDecode, LoadImage, MathExpression|pysssss, JWInteger, BasicScheduler, CLIPTextEncode, CR Text, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频 _ 支持文字 HunyuanVideo1.5_1996147108740808705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996147108740808705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `HunyuanVideo15ImageToVideo`
- `CLIPVisionEncode`
- `EasyCache`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `DF_Int_to_Float`
- `CreateVideo`
- `SaveVideo`
- `VAEDecode` ★核心
- `LoadImage`
- `MathExpression|pysssss`
- `JWInteger`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `CR Text`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`CLIPVisionLoader`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecodeTiled`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`HunyuanVideo15ImageToVideo`、`CLIPVisionEncode`、`EasyCache`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`DF_Int_to_Float`、`CreateVideo`、`SaveVideo`、`VAEDecode`、`LoadImage`、`MathExpression|pysssss`、`JWInteger`、`BasicScheduler`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
