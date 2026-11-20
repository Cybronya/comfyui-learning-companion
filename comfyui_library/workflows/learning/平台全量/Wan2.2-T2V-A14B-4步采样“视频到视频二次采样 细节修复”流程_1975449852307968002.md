---
key: 平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1975449852307968002.json
name: Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1975449852307968002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1975449852307968002.json
hash: 26eb75495f0bfbe4
coverage: 0.756757
learned_at: 2026-11-14 01:06:02
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, CLIPLoader, ModelSamplingSD3, PathchSageAttentionKJ, TorchCompileModel, VAEEncode, KSampler, ContextWindowsManual, WanVideoEnhanceAVideoKJ, VHS_VideoCombine, easy cleanGpuUsed, Reroute, CreateVideo, AILab_MiniCPM_4_V_Advanced, ShowText|pysssss, Note, Note, Fast Groups Bypasser (rgthree), Reroute, ImageConcanate, Note, MarkdownNote, UNETLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Label (rgthree), VAELoader, VHS_VideoCombine, INTConstant, INTConstant, PDImageResize, VHS_VideoInfoLoaded, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.2, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 888, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1975449852307968002.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-T2V-A14B-4步采样“视频到视频二次采样 细节修复”流程_1975449852307968002.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ContextWindowsManual`
- `WanVideoEnhanceAVideoKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `Reroute`
- `CreateVideo`
- `AILab_MiniCPM_4_V_Advanced`
- `ShowText|pysssss`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `ImageConcanate`
- `Note`
- `MarkdownNote`
- `UNETLoader` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `VAELoader`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `PDImageResize`
- `VHS_VideoInfoLoaded`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `888`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.2`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`TorchCompileModel`、`VAEEncode`、`KSampler`、`ContextWindowsManual`、`WanVideoEnhanceAVideoKJ`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`CreateVideo`、`AILab_MiniCPM_4_V_Advanced`、`ImageConcanate`、`UNETLoader`、`LoraLoaderModelOnly`、`Label (rgthree)`、`VAELoader`、`INTConstant`、`PDImageResize`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
