---
key: 平台全量/Bernini_testing_video_edit循环工作流，适合小显存_2067846777507762178.json
name: Bernini_testing_video_edit循环工作流，适合小显存_2067846777507762178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Bernini_testing_video_edit循环工作流，适合小显存_2067846777507762178.json
hash: 87bb42b73ae1eea4
coverage: 0.875
learned_at: 2026-11-14 00:20:20
nodes: [SamplerCustom, CLIPLoader, MarkdownNote, BasicScheduler, VantageWanBlockSwap, VantageWanBlockSwap, VAELoader, VAEDecode, KSamplerSelect, INTConstant, SamplerCustom, VHS_VideoInfo, SimpleCalculatorKJ, CLIPTextEncode, BerniniConditioning, MarkdownNote, BatchImagesNode, easy forLoopStart, PreviewAny, AudioConcat, easy batchAnything, easy forLoopEnd, SplitSigmas, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageFromBatch, SimpleCalculatorKJ, Note, FloatConstant, Note, SimpleMath+, INTConstant, LoadImage, INTConstant, INTConstant, CLIPTextEncode, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Bernini_testing_video_edit循环工作流，适合小显存_2067846777507762178.json

> 来源文件 `comfyui_library/workflows/平台全量/Bernini_testing_video_edit循环工作流，适合小显存_2067846777507762178.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `SamplerCustom` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `BasicScheduler`
- `VantageWanBlockSwap`
- `VantageWanBlockSwap`
- `VAELoader`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `INTConstant`
- `SamplerCustom` ★核心
- `VHS_VideoInfo`
- `SimpleCalculatorKJ`
- `CLIPTextEncode` ★核心
- `BerniniConditioning`
- `MarkdownNote`
- `BatchImagesNode`
- `easy forLoopStart`
- `PreviewAny`
- `AudioConcat`
- `easy batchAnything`
- `easy forLoopEnd`
- `SplitSigmas`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageFromBatch`
- `SimpleCalculatorKJ`
- `Note`
- `FloatConstant`
- `Note`
- `SimpleMath+`
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`SamplerCustom`、`CLIPLoader`、`BasicScheduler`、`VantageWanBlockSwap`、`VAELoader`、`VAEDecode`、`KSamplerSelect`、`INTConstant`、`VHS_VideoInfo`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`BerniniConditioning`、`BatchImagesNode`、`easy forLoopStart`、`AudioConcat`、`easy batchAnything`、`easy forLoopEnd`、`SplitSigmas`、`LoraLoaderModelOnly`、`ImageFromBatch`、`FloatConstant`、`SimpleMath+`、`LoadImage`、`DiffusionModelLoaderKJ`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom
