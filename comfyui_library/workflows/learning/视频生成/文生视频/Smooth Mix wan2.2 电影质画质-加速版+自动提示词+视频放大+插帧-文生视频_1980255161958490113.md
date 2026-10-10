---
key: 视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json
name: Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json
hash: 41a13f95e6b30000
coverage: 0.666667
learned_at: 2026-10-11 02:45:01
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, WanImageToVideo, CLIPTextEncode, CLIPTextEncode, UNETLoader, SetNode, Int, Int, Int, easy seed, KSamplerAdvanced, KSamplerAdvanced, wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), SimpleMath+, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, CR Upscale Image, easy cleanGpuUsed, VHS_VideoCombine, easy ifElse, TextBox1, CR Text Replace, RH_Prompter, ShowText, TextBox1, PrimitiveBoolean, JjkText]
patterns: []
missing: [CR Text Replace, Fast Bypasser (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), RIFE VFI, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, CR Upscale Image, easy seed]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（42 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `Int`
- `Int`
- `Int`
- `easy seed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `CR Upscale Image`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `easy ifElse`
- `TextBox1`
- `CR Text Replace`
- `RH_Prompter`
- `ShowText`
- `TextBox1`
- `PrimitiveBoolean`
- `JjkText`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **67%**（28/42）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`WanImageToVideo`、`CLIPTextEncode`、`Int`、`KSamplerAdvanced`、`wanBlockSwap`、`VHS_VideoCombine`、`TextBox1`、`RH_Prompter`、`ShowText`、`PrimitiveBoolean`

**缺卡**（11）：`CR Text Replace`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`CR Upscale Image`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、RH_Prompter、Int

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
