---
key: 视频生成/图生视频/【首尾帧+图生视频+文生视频】Wan2.2万相视频rapid mega aio综合工作流_1972197412775391234.json
name: 【首尾帧+图生视频+文生视频】Wan2.2万相视频rapid mega aio综合工作流_1972197412775391234.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972197412775391234.json
hash: d4f6df918b8b1296
coverage: 0.895522
learned_at: 2026-10-15 22:31:58
nodes: [ModelSamplingSD3, CLIPTextEncode, KSampler, VAEDecode, PreviewImage, CLIPTextEncode, CheckpointLoaderSimple, MathExpression|pysssss, Note, JWInteger, EmptyHunyuanLatentVideo, Note, VHS_VideoCombine, CheckpointLoaderSimple, VAEDecode, VHS_VideoCombine, CLIPTextEncode, ModelSamplingSD3, WanImageToVideo, PreviewImage, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, Note, MathExpression|pysssss, JWInteger, ModelSamplingSD3, CLIPTextEncode, CheckpointLoaderSimple, INTConstant, KSampler, Note, WanVideoVACEStartToEndFrame, WanVaceToVideo, CLIPTextEncode, LoadImage, LoadImage, easy clearCacheAll, VHS_VideoCombine, VAEDecode, easy cleanGpuUsed, MarkdownNote, CLIPTextEncode, WanVideoVACEStartToEndFrame, WanVaceToVideo, ModelSamplingSD3, INTConstant, KSampler, VAEDecode, easy cleanGpuUsed, easy clearCacheAll, CheckpointLoaderSimple, CLIPTextEncode, WanVaceToVideo, ModelSamplingSD3, KSampler, easy cleanGpuUsed, easy clearCacheAll, VAEDecode, VHS_VideoCombine, CLIPTextEncode, INTConstant, LoadImage, CheckpointLoaderSimple, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-nsfw-aio-v3.1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 1037530326509694, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【首尾帧+图生视频+文生视频】Wan2.2万相视频rapid mega aio综合工作流_1972197412775391234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972197412775391234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `MathExpression|pysssss`
- `Note`
- `JWInteger`
- `EmptyHunyuanLatentVideo`
- `Note`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `Note`
- `MathExpression|pysssss`
- `JWInteger`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `INTConstant`
- `KSampler` ★核心
- `Note`
- `WanVideoVACEStartToEndFrame`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `easy clearCacheAll`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `INTConstant`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1037530326509694`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-nsfw-aio-v3.1.safetensors`

## 知识

覆盖率 **90%**（60/67）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`CheckpointLoaderSimple`、`MathExpression|pysssss`、`JWInteger`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`WanImageToVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`WanVaceToVideo`、`easy clearCacheAll`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、EmptyHunyuanLatentVideo、INTConstant、ModelSamplingSD3

## 参数体检

发现 5 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
