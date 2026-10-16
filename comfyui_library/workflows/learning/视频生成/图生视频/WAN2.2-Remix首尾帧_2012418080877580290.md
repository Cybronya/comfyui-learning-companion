---
key: 视频生成/图生视频/WAN2.2-Remix首尾帧_2012418080877580290.json
name: WAN2.2-Remix首尾帧_2012418080877580290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2012418080877580290.json
hash: d83005b39ae40342
coverage: 1
learned_at: 2026-10-15 22:34:27
nodes: [easy int, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, SimpleMath+, LoadImage, easy int, easy int, LoadImage, Textbox, GetImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-Remix首尾帧_2012418080877580290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2012418080877580290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `easy int`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `LoadImage`
- `easy int`
- `easy int`
- `LoadImage`
- `Textbox`
- `GetImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`easy int`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`wanBlockSwap`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`SimpleMath+`、`LoadImage`、`Textbox`、`GetImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelPatchTorchSettings
