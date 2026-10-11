---
key: 视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json
name: 漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json
hash: a0a3252a215519c2
coverage: 0.35443
learned_at: 2026-10-11 19:49:50
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Note, CLIPLoader, Note, wanBlockSwap, Reroute, Reroute, Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VHS_VideoCombine, VAEDecode, Note, INTConstant, INTConstant, RIFE VFI, Reroute, Reroute, Reroute, Note, WanFirstLastFrameToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, Fast Groups Bypasser (rgthree), Reroute, Reroute, Reroute, VAELoader, Int, Int, Reroute, KSamplerAdvanced, KSamplerAdvanced, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, PreviewImage, wanBlockSwap, UNETLoader, UNETLoader, ImageLoader, ImageLoader, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RIFE VFI, easy cleanGpuUsed]
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `CLIPLoader`
- `Note`
- `wanBlockSwap`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Note`
- `INTConstant`
- `INTConstant`
- `RIFE VFI`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `WanFirstLastFrameToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Int`
- `Int`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageLoader`
- `ImageLoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **35%**（28/79）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`CLIPLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`VHS_VideoCombine`、`VAEDecode`、`INTConstant`、`WanFirstLastFrameToVideo`、`VAELoader`、`Int`、`KSamplerAdvanced`、`ImageResizeKJv2`、`UNETLoader`、`ImageLoader`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`RIFE VFI`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、ImageResizeKJv2、Int

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
