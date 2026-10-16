---
key: 视频生成/图生视频/vace_native_start_end_lightx超长视频生成_1943205882685775873.json
name: vace_native_start_end_lightx超长视频生成_1943205882685775873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1943205882685775873.json
hash: 35f33eb0f420b4af
coverage: 0.464646
learned_at: 2026-10-15 22:30:38
nodes: [SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoVACEStartToEndFrame, GetNode, GetNode, GetNode, KSampler, GetNode, GetNode, GetNode, PreviewImage, MaskPreview, GetNode, ModelSamplingSD3, VAEDecode, GetNode, TrimVideoLatent, GetNode, ModelSamplingSD3, GetNode, GetImageSizeAndCount, ImageFromBatch, SetNode, GetNode, SimpleMath+, SetNode, VAEDecode, GetNode, GetNode, WanVaceToVideo, VHS_VideoCombine, PreviewImage, INTConstant, INTConstant, INTConstant, INTConstant, UNETLoader, CLIPLoader, VAELoader, PathchSageAttentionKJ, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, SetNode, SetNode, WanVaceToVideo, ImageResizeKJv2, RMBG, SetNode, SetNode, GetNode, PreviewImage, GetNode, easy forLoopEnd, GetImageSizeAndCount, SetNode, ImageFromBatch, SimpleMath+, GetNode, WanVideoVACEStartToEndFrame, MaskPreview+, ImageBatchMulti, GetNode, GetNode, KSampler, SimpleMath+, SimpleMath+, ImageFromBatch, ImageColorMatch+, GetNode, INTConstant, INTConstant, LoadImage, CLIPTextEncode, easy forLoopStart, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 464172821071779, "steps": 10}
---

# 视频生成/图生视频/vace_native_start_end_lightx超长视频生成_1943205882685775873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1943205882685775873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `MaskPreview`
- `GetNode`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `WanVaceToVideo`
- `VHS_VideoCombine`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `WanVaceToVideo`
- `ImageResizeKJv2`
- `RMBG`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageFromBatch`
- `SimpleMath+`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `MaskPreview+`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `ImageFromBatch`
- `ImageColorMatch+`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `464172821071779`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（46/99）

**有卡**：`TrimVideoLatent`、`WanVideoVACEStartToEndFrame`、`KSampler`、`MaskPreview`、`ModelSamplingSD3`、`VAEDecode`、`GetImageSizeAndCount`、`ImageFromBatch`、`SimpleMath+`、`WanVaceToVideo`、`VHS_VideoCombine`、`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`ImageResizeKJv2`、`RMBG`、`easy forLoopEnd`、`MaskPreview+`、`ImageBatchMulti`、`ImageColorMatch+`、`LoadImage`、`easy forLoopStart`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
