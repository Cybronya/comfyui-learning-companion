---
key: 视频生成/文生视频/Minimax H3 Long Video One-Take Shot_2091009117015076865.json
name: Minimax H3 Long Video One-Take Shot_2091009117015076865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3 Long Video One-Take Shot_2091009117015076865.json
hash: 04a803cde0c1e81d
coverage: 0.854545
learned_at: 2026-10-15 22:46:32
nodes: [RandomNoise, KSamplerSelect, ComfyMathExpression, VAELoader, VAELoader, easy matchLine, easy ifElse, easy int, MiniMaxH3MotionContextSaveLatent, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, SetNode, easy mergeVideosFromPaths, easy ifElse, PathchSageAttentionKJ, BasicGuider, ManualSigmas, SimpleMathDual+, MiniMaxH3MotionContext, ComfyMathExpression, easy ifElse, MiniMaxH3MotionContextLoadLatent, LoraLoaderModelOnly, easy minimaxH3ToVideo, ModelPreviewOverrideKJ, CLIPLoader, MarkdownNote, PreviewAny, easy cleanGpuUsed, easy forLoopStart, ComfyMathExpression, ComfyMathExpression, llama_cpp_model_loader, llama_cpp_instruct_adv, easy ifElse, easy saveVideo, MiniMaxH3MotionContextTrim, VAEDecodeAudio, VAEDecode, SaveVideo, SamplerCustomAdvanced, easy promptLine, easy promptLine, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3HybridLoader, ManualSigmas, easy ifElse, PrimitiveBoolean, PrimitiveBoolean, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy seed, PrimitiveBoolean, easy multiTrackEditor]
patterns: []
missing: []
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

覆盖率 **85%**（47/55）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ComfyMathExpression`、`VAELoader`、`easy matchLine`、`easy int`、`MiniMaxH3MotionContextSaveLatent`、`easy batchAnything`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy mergeVideosFromPaths`、`PathchSageAttentionKJ`、`BasicGuider`、`ManualSigmas`、`SimpleMathDual+`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextLoadLatent`、`LoraLoaderModelOnly`、`easy minimaxH3ToVideo`、`ModelPreviewOverrideKJ`、`CLIPLoader`、`easy forLoopStart`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy saveVideo`、`MiniMaxH3MotionContextTrim`、`VAEDecodeAudio`、`VAEDecode`、`SaveVideo`、`SamplerCustomAdvanced`、`easy promptLine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3HybridLoader`、`PrimitiveBoolean`、`easy multiTrackInfoOutput`、`easy multiTrackTaskOutput`、`easy seed`、`easy multiTrackEditor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、KSamplerSelect、SamplerCustomAdvanced、easy seed、VAEDecodeAudio
