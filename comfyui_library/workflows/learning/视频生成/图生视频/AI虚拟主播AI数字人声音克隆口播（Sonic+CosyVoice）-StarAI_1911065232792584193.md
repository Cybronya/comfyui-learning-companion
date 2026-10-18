---
key: 视频生成/图生视频/AI虚拟主播AI数字人声音克隆口播（Sonic+CosyVoice）-StarAI_1911065232792584193.json
name: AI虚拟主播AI数字人声音克隆口播（Sonic+CosyVoice）-StarAI_1911065232792584193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI虚拟主播AI数字人声音克隆口播（Sonic+CosyVoice）-StarAI_1911065232792584193.json
hash: 57a06e1c00cd4207
coverage: 0.4
learned_at: 2026-10-15 22:29:30
nodes: [SetNode, SetNode, SetNode, ConvertAny2Float, JjkText, SetNode, CR String To Boolean, JjkText, JjkText, GetNode, easy ifElse, SetNode, GetNode, GetNode, GetNode, NTCosyVoiceZeroShotSampler, NTCosyVoiceInstruct2Sampler, SetNode, SetNode, LoadImage, Note Plus (mtb), JjkText, VHS_VideoCombine, LoadAudio, JjkText, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SONIC_PreData, SONICSampler, easy imageSizeByLongerSide, GetNode, GetNode, SONICTLoader, ImageOnlyCheckpointLoader]
patterns: []
missing: []
parameters: {"checkpoint": "svd_xt-fp16.safetensors"}
---

# 视频生成/图生视频/AI虚拟主播AI数字人声音克隆口播（Sonic+CosyVoice）-StarAI_1911065232792584193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911065232792584193.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `ConvertAny2Float`
- `JjkText`
- `SetNode`
- `CR String To Boolean`
- `JjkText`
- `JjkText`
- `GetNode`
- `easy ifElse`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `NTCosyVoiceZeroShotSampler` ★核心
- `NTCosyVoiceInstruct2Sampler` ★核心
- `SetNode`
- `SetNode`
- `LoadImage`
- `Note Plus (mtb)`
- `JjkText`
- `VHS_VideoCombine`
- `LoadAudio`
- `JjkText`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SONIC_PreData`
- `SONICSampler` ★核心
- `easy imageSizeByLongerSide`
- `GetNode`
- `GetNode`
- `SONICTLoader`
- `ImageOnlyCheckpointLoader` ★核心

## 关键参数

- `checkpoint` = `svd_xt-fp16.safetensors`

## 知识

覆盖率 **40%**（14/35）

**有卡**：`ConvertAny2Float`、`CR String To Boolean`、`NTCosyVoiceZeroShotSampler`、`NTCosyVoiceInstruct2Sampler`、`LoadImage`、`Note Plus (mtb)`、`VHS_VideoCombine`、`LoadAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`SONIC_PreData`、`SONICSampler`、`easy imageSizeByLongerSide`、`SONICTLoader`、`ImageOnlyCheckpointLoader`

**用到的条目**：LoadImage、SONICSampler、NTCosyVoiceInstruct2Sampler、NTCosyVoiceZeroShotSampler、ImageOnlyCheckpointLoader、easy imageSizeByLongerSide、LoadAudio、VHS_VideoCombine
