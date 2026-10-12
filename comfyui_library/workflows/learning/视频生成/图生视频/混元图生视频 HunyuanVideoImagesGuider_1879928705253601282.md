---
key: 视频生成/图生视频/混元图生视频 HunyuanVideoImagesGuider_1879928705253601282.json
name: 混元图生视频 HunyuanVideoImagesGuider_1879928705253601282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/混元图生视频 HunyuanVideoImagesGuider_1879928705253601282.json
hash: f07b410e30f40f4e
coverage: 0.75
learned_at: 2026-10-12 20:12:51
nodes: [CR Text Replace, Reroute, RandomNoise, CLIPTextEncode, VAEDecodeTiled, KSamplerSelect, Note, Florence2Run, Florence2ModelLoader, SamplerCustomAdvanced, VAEEncodeTiled, FluxGuidance, UNETLoader, VAELoader, DualCLIPLoader, BasicScheduler, BasicGuider, StringFunction|pysssss, ModelSamplingSD3, LoadImage, RH_Captioner, ShowText|pysssss, VHS_VideoCombine, Hunyuan Video Image To Guider]
patterns: []
missing: [CR Text Replace, Hunyuan Video Image To Guider, StringFunction|pysssss]
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Hunyuan Video Image To Guider` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识]
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

覆盖率 **75%**（18/24）

**有卡**：`RandomNoise`、`CLIPTextEncode`、`VAEDecodeTiled`、`KSamplerSelect`、`Florence2Run`、`Florence2ModelLoader`、`SamplerCustomAdvanced`、`VAEEncodeTiled`、`FluxGuidance`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`BasicScheduler`、`BasicGuider`、`ModelSamplingSD3`、`LoadImage`、`RH_Captioner`、`VHS_VideoCombine`

**缺卡**（3）：`CR Text Replace`、`Hunyuan Video Image To Guider`、`StringFunction|pysssss`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `Hunyuan Video Image To Guider` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
