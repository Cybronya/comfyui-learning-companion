---
key: 视频生成/图生视频/WAN2.2-RemixV2-I2V完美循环工作流v2_openclaw调用版_2026892222708326401.json
name: WAN2.2-RemixV2-I2V完美循环工作流v2_openclaw调用版_2026892222708326401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2026892222708326401.json
hash: 8055a992b0406db1
coverage: 0.443038
learned_at: 2026-10-15 22:35:15
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Reroute, KSamplerAdvanced, Reroute, Reroute, WanFirstLastFrameToVideo, KSamplerAdvanced, CLIPTextEncode, VAELoader, UNETLoader, UNETLoader, CLIPLoader, wanBlockSwap, wanBlockSwap, INTConstant, VAEDecode, ColorMatch, CreateVideo, INTConstant, ModelSamplingSD3, Reroute, Reroute, Reroute, ImageResizeKJv2, PreviewImage, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, DF_Get_image_size, DF_Get_image_size, PreviewImage, Reroute, Note, SimpleMath+, ModelSamplingSD3, PrimitiveFloat, SaveVideo, TwoWaySwitch, easy cleanGpuUsed, LoadImage, CLIPTextEncode, Int, LoadImage, WanSkipEndFrameImages_F2, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-RemixV2-I2V完美循环工作流v2_openclaw调用版_2026892222708326401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026892222708326401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `wanBlockSwap`
- `wanBlockSwap`
- `INTConstant`
- `VAEDecode` ★核心
- `ColorMatch`
- `CreateVideo`
- `INTConstant`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `DF_Get_image_size`
- `DF_Get_image_size`
- `PreviewImage`
- `Reroute`
- `Note`
- `SimpleMath+`
- `ModelSamplingSD3`
- `PrimitiveFloat`
- `SaveVideo`
- `TwoWaySwitch`
- `easy cleanGpuUsed`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Int`
- `LoadImage`
- `WanSkipEndFrameImages_F2`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **44%**（35/79）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`wanBlockSwap`、`INTConstant`、`VAEDecode`、`ColorMatch`、`CreateVideo`、`ModelSamplingSD3`、`ImageResizeKJv2`、`DF_Get_image_size`、`SimpleMath+`、`SaveVideo`、`TwoWaySwitch`、`easy cleanGpuUsed`、`LoadImage`、`Int`、`WanSkipEndFrameImages_F2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
