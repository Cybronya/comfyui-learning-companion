---
key: 视频生成/图生视频/混元图生视频 HunyuanVideoImagesGuider_1879928705253601282.json
name: 混元图生视频 HunyuanVideoImagesGuider_1879928705253601282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/混元图生视频 HunyuanVideoImagesGuider_1879928705253601282.json
hash: f07b410e30f40f4e
coverage: 0.875
learned_at: 2026-10-15 22:43:05
nodes: [CR Text Replace, Reroute, RandomNoise, CLIPTextEncode, VAEDecodeTiled, KSamplerSelect, Note, Florence2Run, Florence2ModelLoader, SamplerCustomAdvanced, VAEEncodeTiled, FluxGuidance, UNETLoader, VAELoader, DualCLIPLoader, BasicScheduler, BasicGuider, StringFunction|pysssss, ModelSamplingSD3, LoadImage, RH_Captioner, ShowText|pysssss, VHS_VideoCombine, Hunyuan Video Image To Guider]
patterns: []
missing: []
---

# 视频生成/图生视频/混元图生视频 HunyuanVideoImagesGuider_1879928705253601282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/混元图生视频 HunyuanVideoImagesGuider_1879928705253601282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Other

**节点**（24 个）：
- `CR Text Replace`
- `Reroute`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `Note`
- `Florence2Run`
- `Florence2ModelLoader`
- `SamplerCustomAdvanced` ★核心
- `VAEEncodeTiled` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `BasicScheduler`
- `BasicGuider`
- `StringFunction|pysssss`
- `ModelSamplingSD3`
- `LoadImage`
- `RH_Captioner`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `Hunyuan Video Image To Guider`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CR Text Replace`、`RandomNoise`、`CLIPTextEncode`、`VAEDecodeTiled`、`KSamplerSelect`、`Florence2Run`、`Florence2ModelLoader`、`SamplerCustomAdvanced`、`VAEEncodeTiled`、`FluxGuidance`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`BasicScheduler`、`BasicGuider`、`StringFunction|pysssss`、`ModelSamplingSD3`、`LoadImage`、`RH_Captioner`、`VHS_VideoCombine`、`Hunyuan Video Image To Guider`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
