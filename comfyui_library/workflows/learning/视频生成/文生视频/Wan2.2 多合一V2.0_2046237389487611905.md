---
key: 视频生成/文生视频/Wan2.2 多合一V2.0_2046237389487611905.json
name: Wan2.2 多合一V2.0_2046237389487611905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 多合一V2.0_2046237389487611905.json
hash: 6cb14edbee6401e5
coverage: 0.364865
learned_at: 2026-10-11 19:49:43
nodes: [KSampler, GetNode, WanVaceToVideo, GetNode, ModelSamplingSD3, PathchSageAttentionKJ, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, WanVideoVACEStartToEndFrame, VAEDecode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), ImageResizeKJ, GetNode, GetNode, ImageResizeKJ, GetNode, GetNode, SetNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, CR Text, SetNode, LoadImage, SetNode, INTConstant, SimpleMath+, GetNode, SimpleMath+, SDPoseOODProcessor, GetNode, SetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), VHS_VideoCombine, GroundingDinoModelLoader_SDPose, YOLOModelLoader, SDPoseOODLoader, LoadImage, CLIPLoader, VAELoader, GetNode, SimpleMath+, GetNode, SetNode, SimpleMath+, GetNode, GetNode, SetNode, SetNode, SetNode, UNETLoader, VHS_LoadVideo, Note, INTConstant, INTConstant, INTConstant, INTConstant]
patterns: []
missing: [CR Text, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 927483042550590, "steps": 6}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 多合一V2.0_2046237389487611905.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 多合一V2.0_2046237389487611905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（74 个）：
- `KSampler` ★核心
- `GetNode`
- `WanVaceToVideo`
- `GetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `SetNode`
- `LoadImage`
- `SetNode`
- `INTConstant`
- `SimpleMath+`
- `GetNode`
- `SimpleMath+`
- `SDPoseOODProcessor`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `GroundingDinoModelLoader_SDPose`
- `YOLOModelLoader`
- `SDPoseOODLoader`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `Note`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `927483042550590`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **36%**（27/74）

**有卡**：`KSampler`、`WanVaceToVideo`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`WanVideoVACEStartToEndFrame`、`VAEDecode`、`ImageResizeKJ`、`LoadImage`、`INTConstant`、`SDPoseOODProcessor`、`VHS_VideoCombine`、`GroundingDinoModelLoader_SDPose`、`YOLOModelLoader`、`SDPoseOODLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`VHS_LoadVideo`

**缺卡**（5）：`CR Text`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ImageResizeKJ

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
