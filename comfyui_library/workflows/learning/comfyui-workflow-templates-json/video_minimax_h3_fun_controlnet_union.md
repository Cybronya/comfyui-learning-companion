---
key: comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json
name: video_minimax_h3_fun_controlnet_union
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json
hash: 8f6c8f1bbc732b9b
official: true
coverage: 0.615385
learned_at: 2026-10-07 21:37:08
nodes: [ResolutionSelector, MarkdownNote, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, MarkdownNote, ComfySwitchNode, ComfySwitchNode, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, PrimitiveBoolean, MiniMaxH3FunControlNetApply, ModelPatchLoader, LoadVideo, 622cceeb-7ba3-4dd9-b0e8-00066c5222a4, PreviewImage, Video Slice, SaveVideo, MarkdownNote, GetVideoComponents, GetImageSize, PrimitiveBoolean, MarkdownNote, MarkdownNote]
patterns: []
missing: [622cceeb-7ba3-4dd9-b0e8-00066c5222a4, Video Slice]
parameters: {"controlnet_strength": 1}
discoveries: [次要节点 `622cceeb-7ba3-4dd9-b0e8-00066c5222a4` 知识库中没有该节点类型的任何知识, 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json`

## 结构

**生成流程**：Model → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `MiniMaxH3FunControlNetApply` ★核心
- `ModelPatchLoader`
- `LoadVideo`
- `622cceeb-7ba3-4dd9-b0e8-00066c5222a4`
- `PreviewImage`
- `Video Slice`
- `SaveVideo`
- `MarkdownNote`
- `GetVideoComponents`
- `GetImageSize`
- `PrimitiveBoolean`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `controlnet_strength` = `1`

## 知识

覆盖率 **62%**（24/39）

**有卡**：`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`MiniMaxH3FunControlNetApply`、`ModelPatchLoader`、`LoadVideo`、`SaveVideo`、`GetVideoComponents`、`GetImageSize`

**缺卡**（2）：`622cceeb-7ba3-4dd9-b0e8-00066c5222a4`、`Video Slice`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、MiniMaxH3FunControlNetApply、KSamplerSelect

## 学习发现

- 次要节点 `622cceeb-7ba3-4dd9-b0e8-00066c5222a4` 知识库中没有该节点类型的任何知识
- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
