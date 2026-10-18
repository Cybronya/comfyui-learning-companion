---
key: 音频生成/音频生成/声音克隆开源大模型：Step-Audio-EditX，ComfyUI工作流大公开_1990014651792543746.json
name: 声音克隆开源大模型：Step-Audio-EditX，ComfyUI工作流大公开_1990014651792543746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/声音克隆开源大模型：Step-Audio-EditX，ComfyUI工作流大公开_1990014651792543746.json
hash: 076f208393372312
coverage: 0.941176
learned_at: 2026-10-18 01:47:03
nodes: [RunningHub StepAudioEditX Sampler(Emotion), RunningHub StepAudioEditX Sampler(Denoise), PreviewAudio, RunningHub StepAudioEditX Sampler(Paralinguistic), SaveAudio, SaveAudio, SaveAudio, SaveAudio, RunningHub StepAudioEditX ModelLoader, MarkdownNote, SaveAudio, KepStringLiteral, RunningHub StepAudioEditX Sampler(Clone), RunningHub StepAudioEditX Sampler(Style), LoadAudio, AudioSeparation, Label (rgthree)]
patterns: []
missing: []
---

# 音频生成/音频生成/声音克隆开源大模型：Step-Audio-EditX，ComfyUI工作流大公开_1990014651792543746.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/声音克隆开源大模型：Step-Audio-EditX，ComfyUI工作流大公开_1990014651792543746.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（17 个）：
- `RunningHub StepAudioEditX Sampler(Emotion)` ★核心
- `RunningHub StepAudioEditX Sampler(Denoise)` ★核心
- `PreviewAudio`
- `RunningHub StepAudioEditX Sampler(Paralinguistic)` ★核心
- `SaveAudio`
- `SaveAudio`
- `SaveAudio`
- `SaveAudio`
- `RunningHub StepAudioEditX ModelLoader`
- `MarkdownNote`
- `SaveAudio`
- `KepStringLiteral`
- `RunningHub StepAudioEditX Sampler(Clone)` ★核心
- `RunningHub StepAudioEditX Sampler(Style)` ★核心
- `LoadAudio`
- `AudioSeparation`
- `Label (rgthree)`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`RunningHub StepAudioEditX Sampler(Emotion)`、`RunningHub StepAudioEditX Sampler(Denoise)`、`PreviewAudio`、`RunningHub StepAudioEditX Sampler(Paralinguistic)`、`SaveAudio`、`RunningHub StepAudioEditX ModelLoader`、`KepStringLiteral`、`RunningHub StepAudioEditX Sampler(Clone)`、`RunningHub StepAudioEditX Sampler(Style)`、`LoadAudio`、`AudioSeparation`、`Label (rgthree)`

**用到的条目**：RunningHub StepAudioEditX Sampler(Emotion)、RunningHub StepAudioEditX Sampler(Paralinguistic)、RunningHub StepAudioEditX Sampler(Style)、RunningHub StepAudioEditX Sampler(Clone)、RunningHub StepAudioEditX Sampler(Denoise)、SaveAudio、PreviewAudio、LoadAudio
