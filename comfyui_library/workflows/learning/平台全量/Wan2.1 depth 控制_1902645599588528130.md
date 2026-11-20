---
key: 平台全量/Wan2.1 depth 控制_1902645599588528130.json
name: Wan2.1 depth 控制_1902645599588528130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 depth 控制_1902645599588528130.json
hash: 82433971cfcd68b0
coverage: 0.686275
learned_at: 2026-11-14 01:04:28
nodes: [VAELoader, CLIPLoader, KSamplerSelect, GetNode, Anything Everywhere, ModelSamplingSD3, UNETLoader, SetNode, BasicScheduler, SplitSigmas, SetNode, SetNode, LoraLoaderModelOnly, SetNode, GetNode, Reroute, ImageResizeKJ, VHS_SelectImages, ImageScale, AIO_Preprocessor, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, VAEDecode, WanVideoLoraSelect, WanVideoModelLoader, CLIPTextEncode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoControlEmbeds, WanVideoEncode, GetNode, WanVideoVAELoader, Anything Everywhere, WanVideoDecode, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, WanVideoSampler, Fast Groups Muter (rgthree), InstructPixToPixConditioning, SamplerCustom, SamplerCustom, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, CLIPTextEncode, VHS_LoadVideo, Note]
patterns: []
missing: []
---

# 平台全量/Wan2.1 depth 控制_1902645599588528130.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 depth 控制_1902645599588528130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
- `VAELoader`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `GetNode`
- `Anything Everywhere`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `SetNode`
- `BasicScheduler`
- `SplitSigmas`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `Reroute`
- `ImageResizeKJ`
- `VHS_SelectImages`
- `ImageScale`
- `AIO_Preprocessor`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `CLIPTextEncode` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoControlEmbeds`
- `WanVideoEncode`
- `GetNode`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `Fast Groups Muter (rgthree)`
- `InstructPixToPixConditioning`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `Note`

## 知识

覆盖率 **69%**（35/51）

**有卡**：`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`ModelSamplingSD3`、`UNETLoader`、`BasicScheduler`、`SplitSigmas`、`LoraLoaderModelOnly`、`ImageResizeKJ`、`VHS_SelectImages`、`ImageScale`、`AIO_Preprocessor`、`VAEDecode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`CLIPTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoControlEmbeds`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`、`RIFE VFI`、`WanVideoSampler`、`InstructPixToPixConditioning`、`SamplerCustom`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerSelect、SamplerCustom
