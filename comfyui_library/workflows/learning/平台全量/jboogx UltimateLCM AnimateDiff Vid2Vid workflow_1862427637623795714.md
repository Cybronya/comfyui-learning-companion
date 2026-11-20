---
key: 平台全量/jboogx UltimateLCM AnimateDiff Vid2Vid workflow_1862427637623795714.json
name: jboogx UltimateLCM AnimateDiff Vid2Vid workflow_1862427637623795714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/jboogx UltimateLCM AnimateDiff Vid2Vid workflow_1862427637623795714.json
hash: 76525b6610f97cf0
coverage: 0.883117
learned_at: 2026-11-14 01:12:55
nodes: [ControlNetLoaderAdvanced, ControlNetLoaderAdvanced, HEDPreprocessor, ControlNetLoaderAdvanced, FaceRestoreModelLoader, ReActorFaceSwap, LoadImage, PrepImageForClipVision, PreviewImage, PreviewImage, PrepImageForClipVision, FaceRestoreCFWithModel, IPAdapterEncoder, IPAdapterEncoder, DWPreprocessor, LoadImage, Control Net Stacker, Control Net Stacker, IPAdapterEncoder, IPAdapterEncoder, PrepImageForClipVision, PrepImageForClipVision, Control Net Stacker, Control Net Stacker, CLIPTextEncode, ADE_LoopedUniformContextOptions, ADE_AnimateDiffLoRALoader, LineArtPreprocessor, IPAdapterCombineEmbeds, IPAdapterEmbeds, InvertMask, IPAdapterEmbeds, IPAdapterCombineEmbeds, PreviewImage, PreviewImage, Apply ControlNet Stack, LoadImage, LatentUpscaleBy, KSampler (Efficient), FreeU_V2, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, DifferentialDiffusion, ADE_AnimateDiffLoaderWithContext, DepthAnythingPreprocessor, CLIPVisionLoader, IPAdapterModelLoader, IPAdapterModelLoader, CLIPVisionLoader, ControlNetLoaderAdvanced, ImageScale, LayerMask: SegmentAnythingUltra V2, ResizeMask, BatchPromptSchedule, Reroute, LoadImage, LoadImage, LoRA Stacker, Efficient Loader, ControlNetLoaderAdvanced, Control Net Stacker, Control Net Stacker, VHS_VideoCombine, KSampler (Efficient), PrimitiveNode, PrimitiveNode, Reroute, LayerMask: MaskPreview, PreviewImage, ControlNetLoaderAdvanced, FileNamePrefix, FileNamePrefix, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 1.1, "denoise": 1, "sampler_name": "lcm", "scheduler": "sgm_uniform", "seed": 133306879036632, "steps": 11}
---

# 平台全量/jboogx UltimateLCM AnimateDiff Vid2Vid workflow_1862427637623795714.json

> 来源文件 `comfyui_library/workflows/平台全量/jboogx UltimateLCM AnimateDiff Vid2Vid workflow_1862427637623795714.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Process → Output → Other

**节点**（77 个）：
- `ControlNetLoaderAdvanced`
- `ControlNetLoaderAdvanced`
- `HEDPreprocessor`
- `ControlNetLoaderAdvanced`
- `FaceRestoreModelLoader`
- `ReActorFaceSwap`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `PreviewImage`
- `PrepImageForClipVision`
- `FaceRestoreCFWithModel`
- `IPAdapterEncoder`
- `IPAdapterEncoder`
- `DWPreprocessor`
- `LoadImage`
- `Control Net Stacker`
- `Control Net Stacker`
- `IPAdapterEncoder`
- `IPAdapterEncoder`
- `PrepImageForClipVision`
- `PrepImageForClipVision`
- `Control Net Stacker`
- `Control Net Stacker`
- `CLIPTextEncode` ★核心
- `ADE_LoopedUniformContextOptions`
- `ADE_AnimateDiffLoRALoader` ★核心
- `LineArtPreprocessor`
- `IPAdapterCombineEmbeds`
- `IPAdapterEmbeds`
- `InvertMask`
- `IPAdapterEmbeds`
- `IPAdapterCombineEmbeds`
- `PreviewImage`
- `PreviewImage`
- `Apply ControlNet Stack`
- `LoadImage`
- `LatentUpscaleBy`
- `KSampler (Efficient)` ★核心
- `FreeU_V2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DifferentialDiffusion`
- `ADE_AnimateDiffLoaderWithContext`
- `DepthAnythingPreprocessor`
- `CLIPVisionLoader`
- `IPAdapterModelLoader`
- `IPAdapterModelLoader`
- `CLIPVisionLoader`
- `ControlNetLoaderAdvanced`
- `ImageScale`
- `LayerMask: SegmentAnythingUltra V2`
- `ResizeMask`
- `BatchPromptSchedule`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `LoRA Stacker`
- `Efficient Loader`
- `ControlNetLoaderAdvanced`
- `Control Net Stacker`
- `Control Net Stacker`
- `VHS_VideoCombine`
- `KSampler (Efficient)` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `Reroute`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `ControlNetLoaderAdvanced`
- `FileNamePrefix`
- `FileNamePrefix`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `133306879036632`
- `steps` = `11`
- `cfg` = `1.1`
- `sampler_name` = `lcm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **88%**（68/77）

**有卡**：`ControlNetLoaderAdvanced`、`HEDPreprocessor`、`FaceRestoreModelLoader`、`ReActorFaceSwap`、`LoadImage`、`PrepImageForClipVision`、`FaceRestoreCFWithModel`、`IPAdapterEncoder`、`DWPreprocessor`、`Control Net Stacker`、`CLIPTextEncode`、`ADE_LoopedUniformContextOptions`、`ADE_AnimateDiffLoRALoader`、`LineArtPreprocessor`、`IPAdapterCombineEmbeds`、`IPAdapterEmbeds`、`InvertMask`、`Apply ControlNet Stack`、`LatentUpscaleBy`、`KSampler (Efficient)`、`FreeU_V2`、`VHS_VideoCombine`、`DifferentialDiffusion`、`ADE_AnimateDiffLoaderWithContext`、`DepthAnythingPreprocessor`、`CLIPVisionLoader`、`IPAdapterModelLoader`、`ImageScale`、`LayerMask: SegmentAnythingUltra V2`、`ResizeMask`、`BatchPromptSchedule`、`LoRA Stacker`、`Efficient Loader`、`LayerMask: MaskPreview`、`FileNamePrefix`、`VHS_LoadVideo`

**用到的条目**：CLIPTextEncode、LoadImage、Apply ControlNet Stack、Control Net Stacker、ControlNetLoaderAdvanced、DepthAnythingPreprocessor、KSampler (Efficient)、IPAdapterEncoder
