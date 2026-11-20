---
key: 平台全量/MiniMaxH3动作迁移v1.0（参考版）_2117765448346456066.json
name: MiniMaxH3动作迁移v1.0（参考版）_2117765448346456066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMaxH3动作迁移v1.0（参考版）_2117765448346456066.json
hash: d5bca2757f280742
coverage: 0.673913
learned_at: 2026-11-14 00:44:40
nodes: [MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, KSamplerSelect, LoraLoaderModelOnly, CLIPLoader, UNETLoader, VAELoader, VAELoader, ResolutionSelector, ModelAttentionBackend, LoraLoaderModelOnly, Yuan_VideoUI, Yuan_H3ProgressiveSampler, BasicScheduler, TextGenerate, PrimitiveStringMultiline, CLIPLoader, SetNode, GetNode, ComfyMathExpression, Yuan_H3MotionContextTrim, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, YUAN_TXTPreviewContent, PrimitiveStringMultiline, PrimitiveStringMultiline, YUAN_TXTPreviewContent, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, easy clearCacheAll, Yuan_MiniMaxH3RefEmbeds, Yuan_MiniMaxH3RefToVideo, YuanLoadImageOutput, YuanMultiImage, ImageFromBatch, PreviewImage, GetImageSize, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/MiniMaxH3动作迁移v1.0（参考版）_2117765448346456066.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMaxH3动作迁移v1.0（参考版）_2117765448346456066.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（46 个）：
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `ResolutionSelector`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `Yuan_VideoUI`
- `Yuan_H3ProgressiveSampler` ★核心
- `BasicScheduler`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `Yuan_H3MotionContextTrim`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `YUAN_TXTPreviewContent`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `YUAN_TXTPreviewContent`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `Yuan_MiniMaxH3RefEmbeds`
- `Yuan_MiniMaxH3RefToVideo`
- `YuanLoadImageOutput`
- `YuanMultiImage`
- `ImageFromBatch`
- `PreviewImage`
- `GetImageSize`
- `VHS_VideoCombine`

## 知识

覆盖率 **67%**（31/46）

**有卡**：`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`KSamplerSelect`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`ModelAttentionBackend`、`Yuan_VideoUI`、`Yuan_H3ProgressiveSampler`、`BasicScheduler`、`TextGenerate`、`ComfyMathExpression`、`Yuan_H3MotionContextTrim`、`YUAN_TXTPreviewContent`、`easy cleanGpuUsed`、`easy clearCacheAll`、`Yuan_MiniMaxH3RefEmbeds`、`Yuan_MiniMaxH3RefToVideo`、`YuanLoadImageOutput`、`YuanMultiImage`、`ImageFromBatch`、`GetImageSize`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、Yuan_H3ProgressiveSampler、GetImageSize
