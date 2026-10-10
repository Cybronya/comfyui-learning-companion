---
key: 【老金驿站】WAN2.1国家地理场景分镜生成工作流_1929433520668839938.json
name: 【老金驿站】WAN2.1国家地理场景分镜生成工作流_1929433520668839938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【老金驿站】WAN2.1国家地理场景分镜生成工作流_1929433520668839938.json
hash: a5d5990f0ea6eda7
coverage: 0.870968
learned_at: 2026-10-10 20:59:31
nodes: [WanVideoVRAMManagement, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJ, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, VHS_VideoCombine, WanVideoDecode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoTorchCompileSettings, VAELoader, DualCLIPLoader, EmptySD3LatentImage, VAEDecode, SaveImage, PreviewImage, EmptyConditioning, UNETLoader, LoadImage, WanVideoLoraSelect, Fast Groups Bypasser (rgthree), CLIPTextEncode, WanVideoTextEncode, WanVideoSampler, KSampler]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 386416523079482, "steps": 25}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 【老金驿站】WAN2.1国家地理场景分镜生成工作流_1929433520668839938.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【老金驿站】WAN2.1国家地理场景分镜生成工作流_1929433520668839938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `WanVideoVRAMManagement`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoTorchCompileSettings`
- `VAELoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `EmptyConditioning`
- `UNETLoader` ★核心
- `LoadImage`
- `WanVideoLoraSelect`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `386416523079482`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`WanVideoVRAMManagement`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJ`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`VAELoader`、`DualCLIPLoader`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`EmptyConditioning`、`UNETLoader`、`LoadImage`、`WanVideoLoraSelect`、`CLIPTextEncode`、`WanVideoTextEncode`、`WanVideoSampler`、`KSampler`

**缺卡**（2）：`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、WanVideoSampler、LoadWanVideoT5TextEncoder

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
