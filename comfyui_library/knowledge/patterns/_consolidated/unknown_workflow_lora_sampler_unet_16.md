---
name: unknown_workflow_lora_sampler_unet_16
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.820625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy promptConcat, easy saveVideo, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Minimax H3 全自动小短片_2089557392110473217.json, 数字人/数字人/一键生成一分钟长视频 Minimax H3_2088144166755856385.json, 视频生成/图生视频/Minimax H3 全自动小短片_2087477277696282625.json, 视频生成/图生视频/Minimax+H3+全自动小短片+二采高清4+2_2096828253884473345.json, 视频生成/图生视频/Minimax+H3+全自动小短片+二采高清8+4_2096863166981566465.json, 视频生成/图生视频/ONE SHOT STORY｜MiniMax H3 一图生成15秒品牌短片_2087898553539710978.json, 视频生成/图生视频/一键MV_2095144928673357825.json, 视频生成/文生视频/Minimax H3 全自动短片（要配合提示词skill使用）林耀_2091930702962057218.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Minimax H3 全自动小短片_2089557392110473217.json、数字人/数字人/一键生成一分钟长视频 Minimax H3_2088144166755856385.json、视频生成/图生视频/Minimax H3 全自动小短片_2087477277696282625.json、视频生成/图生视频/Minimax+H3+全自动小短片+二采高清4+2_2096828253884473345.json、视频生成/图生视频/Minimax+H3+全自动小短片+二采高清8+4_2096863166981566465.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptConcat`
- `easy saveVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ExtractLinesByIndex` —— 7/8 个有
- `Int Literal` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `ShowText|pysssss` —— 7/8 个有
- `Text To Image (mtb)` —— 7/8 个有
- `easy batchAnything` —— 7/8 个有
- `Text String Truncate` —— 5/8 个有
- `DF_Float` —— 3/8 个有
- `LTXVConcatAVLatent` —— 2/8 个有
- `LTXVSeparateAVLatent` —— 2/8 个有
- `MinimaxH3LatentUpscaler3D` —— 2/8 个有
- `SplitSigmas` —— 2/8 个有
- `ACE_AudioCrop` —— 1/8 个有
- `ASRMW` —— 1/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `CreateVideo` —— 1/8 个有
- `GetAudioDurationFromAudio` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `SaveVideo` —— 1/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/8 个有
- `easy MiniMaxH3MotionContextHard` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有
- `ttN concat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
