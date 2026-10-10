---
key: 视频生成/文生视频/大凯辰光_SVI_2.0_Pro 长视频优化工作流-For循环+旅行提示词高级版_2006383252696735745.json
name: 大凯辰光_SVI_2.0_Pro 长视频优化工作流-For循环+旅行提示词高级版_2006383252696735745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/大凯辰光_SVI_2.0_Pro 长视频优化工作流-For循环+旅行提示词高级版_2006383252696735745.json
hash: 3ff74218e8e00552
coverage: 0.397959
learned_at: 2026-10-10 23:12:18
nodes: [PathchSageAttentionKJ, SetNode, GetNode, SetNode, SetNode, WanImageToVideoSVIPro, ModelSamplingSD3, VAEEncode, easy forLoopStart, GetNode, GetNode, GetNode, GetNode, Display Any (rgthree), GetNode, GetNode, GetNode, ModelSamplingSD3, ModelSamplingSD3, GetNode, WanVideoNAG, SetNode, LoraLoaderModelOnly, CFGZeroStar, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPVisionLoader, SetNode, INTConstant, INTConstant, SetNode, SetNode, ImageResizeKJv2, SetNode, GetImageRangeFromBatch, UNETLoader, UNETLoader, KSamplerAdvanced, easy cleanGpuUsed, easy clearCacheAll, SetNode, ModelSamplingSD3, Note, CLIPTextEncode, GetNode, GetNode, KSamplerAdvanced, GetNode, GetNode, WanVideoNAG, VAEDecode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy clearCacheAll, SetNode, Text Load Line From File, SetNode, PrimitiveStringMultiline, GetNode, SetNode, SetNode, ImageBatchExtendWithOverlap, GetNode, easy forLoopEnd, WanImageToVideoSVIPro, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEEncode, GetNode, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, CLIPTextEncode, SetNode, GetNode, SetNode, CLIPTextEncode, easy cleanGpuUsed, easy clearCacheAll, SetNode, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, GetNode, SetNode, LoadImage]
patterns: []
missing: [Display Any (rgthree), Text Load Line From File, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy forLoopEnd, easy forLoopStart]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/大凯辰光_SVI_2.0_Pro 长视频优化工作流-For循环+旅行提示词高级版_2006383252696735745.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/大凯辰光_SVI_2.0_Pro 长视频优化工作流-For循环+旅行提示词高级版_2006383252696735745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（98 个）：
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanImageToVideoSVIPro`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `easy forLoopStart`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Display Any (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `WanVideoNAG`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStar`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetImageRangeFromBatch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `ModelSamplingSD3`
- `Note`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `WanVideoNAG`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `Text Load Line From File`
- `SetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `easy forLoopEnd`
- `WanImageToVideoSVIPro`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `SetNode`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **40%**（39/98）

**有卡**：`PathchSageAttentionKJ`、`WanImageToVideoSVIPro`、`ModelSamplingSD3`、`VAEEncode`、`WanVideoNAG`、`LoraLoaderModelOnly`、`CFGZeroStar`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`INTConstant`、`ImageResizeKJv2`、`GetImageRangeFromBatch`、`UNETLoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`VAEDecode`、`ImageBatchExtendWithOverlap`、`VHS_VideoCombine`、`LoadImage`

**缺卡**（10）：`Display Any (rgthree)`、`Text Load Line From File`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
