---
key: 视频生成/文生视频/任意轨迹指令运动控制AI视频生成ComfyUI Wan 2.1文生视频图生视频工作流_2088434314995392513.json
name: 任意轨迹指令运动控制AI视频生成ComfyUI Wan 2.1文生视频图生视频工作流_2088434314995392513
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/任意轨迹指令运动控制AI视频生成ComfyUI Wan 2.1文生视频图生视频工作流_2088434314995392513.json
hash: 43ff8eea829e8bfa
coverage: 0.833333
learned_at: 2026-10-11 20:53:51
nodes: [CLIPVisionLoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, PrimitiveNode, Fast Groups Bypasser (rgthree), LoadImage, SplineEditor, ImageResizeKJv2, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, VHS_VideoCombine, Reroute, WanVideoATITracksVisualize, SplineEditor, StringConstantMultiline, SplineEditor, VHS_VideoCombine, WanVideoATITracks, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoDecode, AppendStringsToList, AppendStringsToList, WanVideoATITracksVisualize, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [easy clearCacheAll, easy clearCacheAll, easy clearCacheAll]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/任意轨迹指令运动控制AI视频生成ComfyUI Wan 2.1文生视频图生视频工作流_2088434314995392513.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/任意轨迹指令运动控制AI视频生成ComfyUI Wan 2.1文生视频图生视频工作流_2088434314995392513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `PrimitiveNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SplineEditor`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoATITracksVisualize`
- `SplineEditor`
- `StringConstantMultiline`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoATITracks`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `AppendStringsToList`
- `AppendStringsToList`
- `WanVideoATITracksVisualize`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`LoadImage`、`SplineEditor`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoATITracksVisualize`、`StringConstantMultiline`、`WanVideoATITracks`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`AppendStringsToList`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**缺卡**（3）：`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
