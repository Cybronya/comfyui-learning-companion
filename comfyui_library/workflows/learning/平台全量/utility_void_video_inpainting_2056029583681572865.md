---
key: 平台全量/utility_void_video_inpainting_2056029583681572865.json
name: utility_void_video_inpainting_2056029583681572865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/utility_void_video_inpainting_2056029583681572865.json
hash: 6b12492f06da2f3f
coverage: 0.925
learned_at: 2026-11-14 01:18:28
nodes: [MarkdownNote, MarkdownNote, CLIPLoader, VAELoader, CLIPTextEncode, BasicScheduler, SamplerCustomAdvanced, MaskPreview, OpticalFlowLoader, VOIDInpaintConditioning, VOIDSampler, UNETLoader, UNETLoader, VOIDSampler, SamplerCustomAdvanced, VAEDecode, ImageFromBatch, VAEDecode, GetImageSize, ComfySwitchNode, PrimitiveBoolean, SAM3_Detect, CheckpointLoaderSimple, VHS_VideoInfo, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, INTConstant, INTConstant, INTConstant, CLIPTextEncode, CLIPTextEncode, INTConstant, VHS_LoadVideo, VOIDWarpedNoise, VOIDWarpedNoiseSource, BasicScheduler, CFGGuider, RandomNoise, CFGGuider]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/utility_void_video_inpainting_2056029583681572865.json

> 来源文件 `comfyui_library/workflows/平台全量/utility_void_video_inpainting_2056029583681572865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `MaskPreview`
- `OpticalFlowLoader`
- `VOIDInpaintConditioning`
- `VOIDSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VOIDSampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `VAEDecode` ★核心
- `GetImageSize`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `VHS_LoadVideo`
- `VOIDWarpedNoise`
- `VOIDWarpedNoiseSource`
- `BasicScheduler`
- `CFGGuider`
- `RandomNoise`
- `CFGGuider`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **92%**（37/40）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`BasicScheduler`、`SamplerCustomAdvanced`、`MaskPreview`、`OpticalFlowLoader`、`VOIDInpaintConditioning`、`VOIDSampler`、`UNETLoader`、`VAEDecode`、`ImageFromBatch`、`GetImageSize`、`PrimitiveBoolean`、`SAM3_Detect`、`CheckpointLoaderSimple`、`VHS_VideoInfo`、`ImageResizeKJv2`、`VHS_VideoCombine`、`INTConstant`、`VHS_LoadVideo`、`VOIDWarpedNoise`、`VOIDWarpedNoiseSource`、`CFGGuider`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode、CFGGuider、SamplerCustomAdvanced
