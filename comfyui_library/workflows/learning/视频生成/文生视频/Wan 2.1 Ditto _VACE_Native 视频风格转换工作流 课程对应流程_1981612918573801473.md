---
key: 视频生成/文生视频/Wan 2.1 Ditto _VACE_Native 视频风格转换工作流 课程对应流程_1981612918573801473.json
name: Wan 2.1 Ditto _VACE_Native 视频风格转换工作流 课程对应流程_1981612918573801473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.1 Ditto _VACE_Native 视频风格转换工作流 课程对应流程_1981612918573801473.json
hash: abe9aeb4a16d3902
coverage: 0.488372
learned_at: 2026-10-10 23:06:07
nodes: [CLIPTextEncode, WanVaceToVideo, INTConstant, INTConstant, INTConstant, ModelSamplingSD3, TrimVideoLatent, VAEDecode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, wanBlockSwap, TorchCompileModelWanVideoV2, VHS_VideoInfo, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, DiffusionModelSelector, DiffusionModelLoaderKJ, PatchModelPatcherOrder, VAELoader, CLIPLoader, SetNode, Power Lora Loader (rgthree), VHS_LoadVideo, Note, Note, CLIPTextEncode, GetNode, KSampler, GetNode, VHS_VideoCombine]
patterns: []
missing: [Power Lora Loader (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.2, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 236343881282854, "steps": 4}
discoveries: [次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan 2.1 Ditto _VACE_Native 视频风格转换工作流 课程对应流程_1981612918573801473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.1 Ditto _VACE_Native 视频风格转换工作流 课程对应流程_1981612918573801473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `wanBlockSwap`
- `TorchCompileModelWanVideoV2`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `DiffusionModelSelector`
- `DiffusionModelLoaderKJ`
- `PatchModelPatcherOrder`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `Power Lora Loader (rgthree)`
- `VHS_LoadVideo`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `236343881282854`
- `steps` = `4`
- `cfg` = `1.2`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **49%**（21/43）

**有卡**：`CLIPTextEncode`、`WanVaceToVideo`、`INTConstant`、`ModelSamplingSD3`、`TrimVideoLatent`、`VAEDecode`、`wanBlockSwap`、`TorchCompileModelWanVideoV2`、`VHS_VideoInfo`、`ImageResizeKJv2`、`DiffusionModelSelector`、`DiffusionModelLoaderKJ`、`PatchModelPatcherOrder`、`VAELoader`、`CLIPLoader`、`VHS_LoadVideo`、`KSampler`、`VHS_VideoCombine`

**缺卡**（1）：`Power Lora Loader (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、TrimVideoLatent、ImageResizeKJv2、INTConstant

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
