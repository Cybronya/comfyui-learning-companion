---
key: 视频生成/文生视频/文生视频-Wan2.1-VACE-Native_1924863840855465985.json
name: 文生视频-Wan2.1-VACE-Native_1924863840855465985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频-Wan2.1-VACE-Native_1924863840855465985.json
hash: da6ee9868d480770
coverage: 1
learned_at: 2026-10-10 23:13:09
nodes: [VAEDecode, TrimVideoLatent, CLIPLoader, CLIPTextEncode, VAELoader, INTConstant, INTConstant, UNETLoader, WanVaceToVideo, KSampler, INTConstant, ModelSamplingSD3, CFGZeroStarAndInit, WanVideoEnhanceAVideoKJ, TorchCompileModelWanVideo, PatchModelPatcherOrder, VHS_VideoCombine, LoraLoaderModelOnly, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 804579447650274, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生视频-Wan2.1-VACE-Native_1924863840855465985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频-Wan2.1-VACE-Native_1924863840855465985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `WanVaceToVideo`
- `KSampler` ★核心
- `INTConstant`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `WanVideoEnhanceAVideoKJ`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `804579447650274`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`VAEDecode`、`TrimVideoLatent`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`INTConstant`、`UNETLoader`、`WanVaceToVideo`、`KSampler`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`WanVideoEnhanceAVideoKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`VHS_VideoCombine`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
