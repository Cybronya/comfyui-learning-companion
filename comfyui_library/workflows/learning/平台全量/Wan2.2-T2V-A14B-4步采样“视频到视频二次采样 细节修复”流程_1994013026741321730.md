---
key: 平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1994013026741321730.json
name: Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1994013026741321730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1994013026741321730.json
hash: 6e7dc77c721b3139
coverage: 0.75
learned_at: 2026-11-14 01:06:02
nodes: [CLIPTextEncode, VAEDecode, CLIPLoader, ModelSamplingSD3, PathchSageAttentionKJ, TorchCompileModel, WanVideoEnhanceAVideoKJ, VHS_VideoCombine, easy cleanGpuUsed, Reroute, CreateVideo, AILab_MiniCPM_4_V_Advanced, Note, Note, Fast Groups Bypasser (rgthree), Reroute, ImageConcanate, MarkdownNote, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Label (rgthree), VAELoader, CLIPTextEncode, ShowText|pysssss, Note, Note, KSampler, ContextWindowsManual, VAEEncode, ImageScale, VHS_VideoInfoLoaded, VHS_VideoInfo, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.08000000000000002, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 889, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1994013026741321730.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1994013026741321730.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `WanVideoEnhanceAVideoKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `Reroute`
- `CreateVideo`
- `AILab_MiniCPM_4_V_Advanced`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `ImageConcanate`
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `Note`
- `Note`
- `KSampler` ★核心
- `ContextWindowsManual`
- `VAEEncode` ★核心
- `ImageScale`
- `VHS_VideoInfoLoaded`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `889`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.08000000000000002`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`TorchCompileModel`、`WanVideoEnhanceAVideoKJ`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`CreateVideo`、`AILab_MiniCPM_4_V_Advanced`、`ImageConcanate`、`UNETLoader`、`LoraLoaderModelOnly`、`Label (rgthree)`、`VAELoader`、`KSampler`、`ContextWindowsManual`、`VAEEncode`、`ImageScale`、`VHS_VideoInfoLoaded`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
