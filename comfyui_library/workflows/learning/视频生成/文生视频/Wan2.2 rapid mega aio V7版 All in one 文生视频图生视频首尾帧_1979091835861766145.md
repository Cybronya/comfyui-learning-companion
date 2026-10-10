---
key: 视频生成/文生视频/Wan2.2 rapid mega aio V7版 All in one 文生视频图生视频首尾帧_1979091835861766145.json
name: Wan2.2 rapid mega aio V7版 All in one 文生视频图生视频首尾帧_1979091835861766145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 rapid mega aio V7版 All in one 文生视频图生视频首尾帧_1979091835861766145.json
hash: 39d6915501b7d8d8
coverage: 0.866667
learned_at: 2026-10-10 23:06:59
nodes: [SimpleMath+, INTConstant, INTConstant, INTConstant, CLIPTextEncode, WanVaceToVideo, WanVideoVACEStartToEndFrame, KSampler, VHS_VideoCombine, CLIPTextEncode, VAEDecode, Note, LoadImage, LoadImage, RHHiddenNodes]
patterns: []
missing: [SimpleMath+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 429552545191838, "steps": 4}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 rapid mega aio V7版 All in one 文生视频图生视频首尾帧_1979091835861766145.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 rapid mega aio V7版 All in one 文生视频图生视频首尾帧_1979091835861766145.json`

## 结构

**生成流程**：Condition → Sampling → Decode → Other

**节点**（15 个）：
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `RHHiddenNodes`

## 关键参数

- `seed` = `429552545191838`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`INTConstant`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`KSampler`、`VHS_VideoCombine`、`VAEDecode`、`LoadImage`、`RHHiddenNodes`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、LoadImage、INTConstant、RHHiddenNodes、VHS_VideoCombine、WanVaceToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
