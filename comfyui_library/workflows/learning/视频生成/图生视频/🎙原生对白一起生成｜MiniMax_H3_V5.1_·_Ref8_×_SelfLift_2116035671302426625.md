---
key: 视频生成/图生视频/🎙原生对白一起生成｜MiniMax_H3_V5.1_·_Ref8_×_SelfLift_2116035671302426625.json
name: 🎙原生对白一起生成｜MiniMax_H3_V5.1_·_Ref8_×_SelfLift_2116035671302426625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🎙原生对白一起生成｜MiniMax_H3_V5.1_·_Ref8_×_SelfLift_2116035671302426625.json
hash: c7c6b299cb3da3f1
coverage: 1
learned_at: 2026-10-30 23:30:07
nodes: [UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, MiniMaxH3SigmaShift, MiniMaxH3ReferenceToVideo, KSamplerSelect, BasicScheduler, SaveVideo, SelfLiftH3Sampler, VAEDecode, VAEDecodeAudio, CreateVideo, ConditioningZeroOut, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/🎙原生对白一起生成｜MiniMax_H3_V5.1_·_Ref8_×_SelfLift_2116035671302426625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/🎙原生对白一起生成｜MiniMax_H3_V5.1_·_Ref8_×_SelfLift_2116035671302426625.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3SigmaShift`
- `MiniMaxH3ReferenceToVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveVideo`
- `SelfLiftH3Sampler` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `ConditioningZeroOut`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`MiniMaxH3SigmaShift`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`BasicScheduler`、`SaveVideo`、`SelfLiftH3Sampler`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`ConditioningZeroOut`、`LoadImage`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect
