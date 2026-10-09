---
key: 图片生成/文生图/Wan2.2 Smooth Mix文生视频_1980468292714455042.json
name: Wan2.2 Smooth Mix文生视频_1980468292714455042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 Smooth Mix文生视频_1980468292714455042.json
hash: 1ed6c41a0fb55830
coverage: 0.393939
learned_at: 2026-10-09 19:56:20
nodes: [SetNode, SetNode, SetNode, INTConstant, SetNode, SimpleMath+, SetNode, CLIPLoader, easy cleanGpuUsed, GetNode, VAEDecode, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, SetNode, VAELoader, WanImageToVideo, CLIPTextEncode, SetNode, SetNode, GetNode, ImageFromBatch+, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, easy cleanGpuUsed, SetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, PathchSageAttentionKJ, FloatConstant, CLIPTextEncode, easy seed, SetNode, UNETLoader, INTConstant, INTConstant, UNETLoader, VHS_VideoCombine, easy clearCacheAll, GIMMVFI_interpolate, easy cleanGpuUsed, easy clearCacheAll, DownloadAndLoadGIMMVFIModel, Int, SimpleMath+, GetNode, Primitive string multiline [Crystools], VHS_VideoCombine, SimpleCondition+, GetNode, JjkShowText, RH_LLMAPI_NODE, SetNode, VHS_VideoCombine]
patterns: []
missing: [ImageFromBatch+, Primitive string multiline [Crystools], SimpleCondition+, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll, easy seed]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleCondition+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Wan2.2 Smooth Mix文生视频_1980468292714455042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1980468292714455042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（66 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageFromBatch+`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `FloatConstant`
- `CLIPTextEncode` ★核心
- `easy seed`
- `SetNode`
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `GIMMVFI_interpolate`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `DownloadAndLoadGIMMVFIModel`
- `Int`
- `SimpleMath+`
- `GetNode`
- `Primitive string multiline [Crystools]`
- `VHS_VideoCombine`
- `SimpleCondition+`
- `GetNode`
- `JjkShowText`
- `RH_LLMAPI_NODE`
- `SetNode`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **39%**（26/66）

**有卡**：`INTConstant`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`WanImageToVideo`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`FloatConstant`、`UNETLoader`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`Int`、`JjkShowText`、`RH_LLMAPI_NODE`

**缺卡**（13）：`ImageFromBatch+`、`Primitive string multiline [Crystools]`、`SimpleCondition+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、FloatConstant、Int

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleCondition+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
