---
key: 视频生成/文生视频/AI视频制作神器 自动连续分镜Next Scene V1.0版_1979224907714301953.json
name: AI视频制作神器 自动连续分镜Next Scene V1.0版_1979224907714301953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI视频制作神器 自动连续分镜Next Scene V1.0版_1979224907714301953.json
hash: 2eb7f17e520edef1
coverage: 0.73494
learned_at: 2026-10-10 22:58:35
nodes: [Note, Note, PathchSageAttentionKJ, CLIPLoader, ModelPatchTorchSettings, wanBlockSwap, WanMoeKSampler, CLIPTextEncode, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, CLIPVisionEncode, Note, ImageResizeKJv2, WanFirstLastFrameToVideo, easy cleanGpuUsed, UNETLoader, UNETLoader, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, VAEDecode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPVisionEncode, SimpleMath+, Note, Note, Note, Note, easy cleanGpuUsed, RIFE VFI, WanMoeKSampler, WanImageToVideo, ImageResizeKJv2, DF_Integer, INTConstant, wanBlockSwap, wanBlockSwap, Int, Int, CLIPVisionLoader, CLIPLoader, UNETLoader, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, Int, INTConstant, Int, RIFE VFI, Fast Groups Bypasser (rgthree), Note, LoadImage, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, easy promptLine, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, VAEDecode, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, LoadImage, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, CLIPTextEncode, LoadImage, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree)]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RIFE VFI, RIFE VFI, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy promptLine]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-SFW-v5.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 214, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/AI视频制作神器 自动连续分镜Next Scene V1.0版_1979224907714301953.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI视频制作神器 自动连续分镜Next Scene V1.0版_1979224907714301953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `Note`
- `Note`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `WanMoeKSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `Note`
- `ImageResizeKJv2`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPVisionEncode`
- `SimpleMath+`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `WanMoeKSampler` ★核心
- `WanImageToVideo`
- `ImageResizeKJv2`
- `DF_Integer`
- `INTConstant`
- `wanBlockSwap`
- `wanBlockSwap`
- `Int`
- `Int`
- `CLIPVisionLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `Int`
- `INTConstant`
- `Int`
- `RIFE VFI`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy promptLine`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `214`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-SFW-v5.safetensors`

## 知识

覆盖率 **73%**（61/83）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`ModelPatchTorchSettings`、`wanBlockSwap`、`WanMoeKSampler`、`CLIPTextEncode`、`VAEDecode`、`CLIPVisionEncode`、`ImageResizeKJv2`、`WanFirstLastFrameToVideo`、`UNETLoader`、`WanImageToVideo`、`DF_Integer`、`INTConstant`、`Int`、`CLIPVisionLoader`、`VAELoader`、`ConditioningZeroOut`、`LoadImage`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`SaveImage`、`VHS_VideoCombine`

**缺卡**（8）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`RIFE VFI`、`RIFE VFI`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
