---
key: 数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json
name: Void_video_inpainting视频重绘V2V元素移除_2061983021380751361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json
hash: 7780214e812852e1
coverage: 0.840909
learned_at: 2026-10-26 01:57:37
nodes: [SaveVideo, MarkdownNote, CLIPLoader, VAELoader, CLIPTextEncode, CFGGuider, BasicScheduler, CFGGuider, RandomNoise, VOIDWarpedNoise, SamplerCustomAdvanced, MaskPreview, VOIDInpaintConditioning, VOIDWarpedNoiseSource, BasicScheduler, VOIDSampler, UNETLoader, CreateVideo, VOIDSampler, SamplerCustomAdvanced, VAEDecode, ImageFromBatch, GetImageSize, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, TrimAudioDuration, PrimitiveInt, ComfyMathExpression, CreateVideo, GetVideoComponents, PrimitiveInt, ComfyMathExpression, ComfySwitchNode, VAEDecode, OpticalFlowLoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, SaveVideo, MarkdownNote, LoadVideo, SAM3_Detect]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `SaveVideo`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `BasicScheduler`
- `CFGGuider`
- `RandomNoise`
- `VOIDWarpedNoise`
- `SamplerCustomAdvanced` ★核心
- `MaskPreview`
- `VOIDInpaintConditioning`
- `VOIDWarpedNoiseSource`
- `BasicScheduler`
- `VOIDSampler` ★核心
- `UNETLoader` ★核心
- `CreateVideo`
- `VOIDSampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `GetImageSize`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `TrimAudioDuration`
- `PrimitiveInt`
- `ComfyMathExpression`
- `CreateVideo`
- `GetVideoComponents`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `OpticalFlowLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `SaveVideo`
- `MarkdownNote`
- `LoadVideo`
- `SAM3_Detect`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`SaveVideo`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CFGGuider`、`BasicScheduler`、`RandomNoise`、`VOIDWarpedNoise`、`SamplerCustomAdvanced`、`MaskPreview`、`VOIDInpaintConditioning`、`VOIDWarpedNoiseSource`、`VOIDSampler`、`UNETLoader`、`CreateVideo`、`VAEDecode`、`ImageFromBatch`、`GetImageSize`、`PrimitiveBoolean`、`TrimAudioDuration`、`ComfyMathExpression`、`GetVideoComponents`、`OpticalFlowLoader`、`CheckpointLoaderSimple`、`LoadVideo`、`SAM3_Detect`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、SamplerCustomAdvanced
