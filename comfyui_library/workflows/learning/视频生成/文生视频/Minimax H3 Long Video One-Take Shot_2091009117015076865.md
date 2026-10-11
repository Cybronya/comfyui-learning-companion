---
key: 视频生成/文生视频/Minimax H3 Long Video One-Take Shot_2091009117015076865.json
name: Minimax H3 Long Video One-Take Shot_2091009117015076865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3 Long Video One-Take Shot_2091009117015076865.json
hash: 04a803cde0c1e81d
coverage: 0.545455
learned_at: 2026-10-11 21:19:47
nodes: [RandomNoise, KSamplerSelect, ComfyMathExpression, VAELoader, VAELoader, easy matchLine, easy ifElse, easy int, MiniMaxH3MotionContextSaveLatent, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, SetNode, easy mergeVideosFromPaths, easy ifElse, PathchSageAttentionKJ, BasicGuider, ManualSigmas, SimpleMathDual+, MiniMaxH3MotionContext, ComfyMathExpression, easy ifElse, MiniMaxH3MotionContextLoadLatent, LoraLoaderModelOnly, easy minimaxH3ToVideo, ModelPreviewOverrideKJ, CLIPLoader, MarkdownNote, PreviewAny, easy cleanGpuUsed, easy forLoopStart, ComfyMathExpression, ComfyMathExpression, llama_cpp_model_loader, llama_cpp_instruct_adv, easy ifElse, easy saveVideo, MiniMaxH3MotionContextTrim, VAEDecodeAudio, VAEDecode, SaveVideo, SamplerCustomAdvanced, easy promptLine, easy promptLine, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3HybridLoader, ManualSigmas, easy ifElse, PrimitiveBoolean, PrimitiveBoolean, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy seed, PrimitiveBoolean, easy multiTrackEditor]
patterns: []
missing: [SimpleMathDual+, easy batchAnything, easy cleanGpuUsed, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy int, easy matchLine, easy mergeVideosFromPaths, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy promptLine, easy promptLine, easy saveVideo, easy seed]
discoveries: [次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy matchLine` 知识库中没有该节点类型的任何知识, 次要节点 `easy mergeVideosFromPaths` 知识库中没有该节点类型的任何知识, 次要节点 `easy minimaxH3ToVideo` 知识库中没有该节点类型的任何知识, 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识, 次要节点 `easy multiTrackInfoOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy multiTrackTaskOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy saveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Minimax H3 Long Video One-Take Shot_2091009117015076865.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3 Long Video One-Take Shot_2091009117015076865.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（55 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `VAELoader`
- `VAELoader`
- `easy matchLine`
- `easy ifElse`
- `easy int`
- `MiniMaxH3MotionContextSaveLatent`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `SetNode`
- `easy mergeVideosFromPaths`
- `easy ifElse`
- `PathchSageAttentionKJ`
- `BasicGuider`
- `ManualSigmas`
- `SimpleMathDual+`
- `MiniMaxH3MotionContext`
- `ComfyMathExpression`
- `easy ifElse`
- `MiniMaxH3MotionContextLoadLatent`
- `LoraLoaderModelOnly` ★核心
- `easy minimaxH3ToVideo`
- `ModelPreviewOverrideKJ`
- `CLIPLoader`
- `MarkdownNote`
- `PreviewAny`
- `easy cleanGpuUsed`
- `easy forLoopStart`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy ifElse`
- `easy saveVideo`
- `MiniMaxH3MotionContextTrim`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `easy promptLine`
- `easy promptLine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3HybridLoader`
- `ManualSigmas`
- `easy ifElse`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy seed`
- `PrimitiveBoolean`
- `easy multiTrackEditor`

## 知识

覆盖率 **55%**（30/55）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ComfyMathExpression`、`VAELoader`、`MiniMaxH3MotionContextSaveLatent`、`PathchSageAttentionKJ`、`BasicGuider`、`ManualSigmas`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextLoadLatent`、`LoraLoaderModelOnly`、`ModelPreviewOverrideKJ`、`CLIPLoader`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`MiniMaxH3MotionContextTrim`、`VAEDecodeAudio`、`VAEDecode`、`SaveVideo`、`SamplerCustomAdvanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3HybridLoader`、`PrimitiveBoolean`

**缺卡**（17）：`SimpleMathDual+`、`easy batchAnything`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy forLoopStart`、`easy int`、`easy matchLine`、`easy mergeVideosFromPaths`、`easy minimaxH3ToVideo`、`easy multiTrackEditor`、`easy multiTrackInfoOutput`、`easy multiTrackTaskOutput`、`easy promptLine`、`easy promptLine`、`easy saveVideo`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、MiniMaxH3MotionContextLoadLatent

## 学习发现

- 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy matchLine` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mergeVideosFromPaths` 知识库中没有该节点类型的任何知识
- 次要节点 `easy minimaxH3ToVideo` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multiTrackInfoOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy multiTrackTaskOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
