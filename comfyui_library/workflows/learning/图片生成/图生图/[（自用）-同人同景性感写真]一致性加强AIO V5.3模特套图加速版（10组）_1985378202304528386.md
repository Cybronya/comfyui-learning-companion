---
key: 图片生成/图生图/[（自用）-同人同景性感写真]一致性加强AIO V5.3模特套图加速版（10组）_1985378202304528386.json
name: [（自用）-同人同景性感写真]一致性加强AIO V5.3模特套图加速版（10组）_1985378202304528386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/[（自用）-同人同景性感写真]一致性加强AIO V5.3模特套图加速版（10组）_1985378202304528386.json
hash: c34f26ddc3e74cab
coverage: 0.95
learned_at: 2026-10-23 11:33:25
nodes: [ModelSamplingAuraFlow, LoraLoaderModelOnly, CR Prompt Text, ShowText|pysssss, TextEncodeQwenImageEdit, JDCN_StringToList, AILab_QwenVL, ProcessString, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, TT_img_enc_v2, SaveImage, CR Prompt Text, LoadImage, SaveImage, TT_img_enc, VAEDecode, ImageListToBatch+, Float, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "sampler_name": "lcm", "scheduler": "sgm_uniform", "seed": 1046699024124233, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/[（自用）-同人同景性感写真]一致性加强AIO V5.3模特套图加速版（10组）_1985378202304528386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/[（自用）-同人同景性感写真]一致性加强AIO V5.3模特套图加速版（10组）_1985378202304528386.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `JDCN_StringToList`
- `AILab_QwenVL`
- `ProcessString`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `TT_img_enc_v2`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`
- `TT_img_enc`
- `VAEDecode` ★核心
- `ImageListToBatch+`
- `Float`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `1046699024124233`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CR Prompt Text`、`TextEncodeQwenImageEdit`、`JDCN_StringToList`、`AILab_QwenVL`、`ProcessString`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`TT_img_enc_v2`、`SaveImage`、`LoadImage`、`TT_img_enc`、`VAEDecode`、`ImageListToBatch+`、`Float`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、LoadImage、TextEncodeQwenImageEdit、TextEncodeQwenImageEditPlusAdvance_lrzjason、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
