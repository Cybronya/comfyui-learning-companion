---
key: 视频生成/图生视频/LTX2.3 prompt relay 提示词分段控制流_2052341800647569410.json
name: LTX2.3 prompt relay 提示词分段控制流_2052341800647569410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052341800647569410.json
hash: 0a6d871ef8593ba1
coverage: 0.733333
learned_at: 2026-10-15 22:37:29
nodes: [SamplerCustomAdvanced, Reroute, LTXVAudioVAEDecode, CFGGuider, CreateVideo, RandomNoise, LTXVCropGuides, LTXVSeparateAVLatent, KSamplerSelect, BasicScheduler, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, ResizeImagesByLongerEdge, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, easy showAnything, UNETLoader, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, ComfyMathExpression, Int, PrimitiveInt, PrimitiveFloat, VAEDecodeTiled, LoadImage, PromptRelayEncodeTimeline, SaveVideo, LoraLoaderModelOnly, LTXVConditioning, Note, Note, Note, Note, Note, LoadImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 193}
---

# 视频生成/图生视频/LTX2.3 prompt relay 提示词分段控制流_2052341800647569410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052341800647569410.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `CreateVideo`
- `RandomNoise`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `easy showAnything`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ComfyMathExpression`
- `Int`
- `PrimitiveInt`
- `PrimitiveFloat`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `PromptRelayEncodeTimeline`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `Note`

## 关键参数

- `width` = `193`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（33/45）

**有卡**：`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`CFGGuider`、`CreateVideo`、`RandomNoise`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`Int`、`VAEDecodeTiled`、`LoadImage`、`PromptRelayEncodeTimeline`、`SaveVideo`、`LoraLoaderModelOnly`、`LTXVConditioning`

**用到的条目**：LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
