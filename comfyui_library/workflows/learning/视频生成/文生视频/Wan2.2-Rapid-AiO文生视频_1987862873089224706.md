---
key: 视频生成/文生视频/Wan2.2-Rapid-AiO文生视频_1987862873089224706.json
name: Wan2.2-Rapid-AiO文生视频_1987862873089224706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-Rapid-AiO文生视频_1987862873089224706.json
hash: 1bb9b86d339a30e7
coverage: 0.785714
learned_at: 2026-10-11 02:57:38
nodes: [CLIPTextEncode, ApplySageAttention, WanVaceToVideo, CLIPTextEncode, ModelSamplingSD3, KSampler, VAEDecode, VHS_VideoCombine, CheckpointLoaderSimple, SimpleMath+, LayerUtility: TextJoin, Wan22PromptSelector, CR Text, INTConstant]
patterns: []
missing: [CR Text, LayerUtility: TextJoin, SimpleMath+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 870837176853440, "steps": 4}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2-Rapid-AiO文生视频_1987862873089224706.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-Rapid-AiO文生视频_1987862873089224706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `ApplySageAttention`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `SimpleMath+`
- `LayerUtility: TextJoin`
- `Wan22PromptSelector`
- `CR Text`
- `INTConstant`

## 关键参数

- `seed` = `870837176853440`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`CLIPTextEncode`、`ApplySageAttention`、`WanVaceToVideo`、`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`Wan22PromptSelector`、`INTConstant`

**缺卡**（3）：`CR Text`、`LayerUtility: TextJoin`、`SimpleMath+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、Wan22PromptSelector、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
