---
key: 视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json
name: Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json
hash: 41a13f95e6b30000
coverage: 0.928571
learned_at: 2026-10-15 22:47:01
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Bypasser (rgthree), PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, ModelPatchTorchSettings, VAEDecode, WanImageToVideo, CLIPTextEncode, CLIPTextEncode, UNETLoader, SetNode, Int, Int, Int, easy seed, KSamplerAdvanced, KSamplerAdvanced, wanBlockSwap, wanBlockSwap, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Fast Bypasser (rgthree), SimpleMath+, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, CR Upscale Image, easy cleanGpuUsed, VHS_VideoCombine, easy ifElse, TextBox1, CR Text Replace, RH_Prompter, ShowText, TextBox1, PrimitiveBoolean, JjkText]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
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

覆盖率 **93%**（39/42）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`Fast Bypasser (rgthree)`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`WanImageToVideo`、`CLIPTextEncode`、`Int`、`easy seed`、`KSamplerAdvanced`、`wanBlockSwap`、`Mute / Bypass Repeater (rgthree)`、`SimpleMath+`、`easy cleanGpuUsed`、`RIFE VFI`、`VHS_VideoCombine`、`CR Upscale Image`、`TextBox1`、`CR Text Replace`、`RH_Prompter`、`ShowText`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、easy seed、CR Upscale Image
