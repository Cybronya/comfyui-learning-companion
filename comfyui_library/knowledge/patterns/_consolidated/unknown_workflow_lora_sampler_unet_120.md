---
name: unknown_workflow_lora_sampler_unet_120
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.812
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ExtractLinesByIndex, Int Literal, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MotionContext, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy promptConcat, easy saveVideo, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/一键生成一分钟长视频 Minimax H3_2088144166755856385.json, 视频生成/图生视频/Minimax H3 全自动小短片_2087477277696282625.json, 视频生成/图生视频/Minimax+H3+全自动小短片+二采高清4+2_2096828253884473345.json, 视频生成/图生视频/Minimax+H3+全自动小短片+二采高清8+4_2096863166981566465.json, 视频生成/图生视频/ONE SHOT STORY｜MiniMax H3 一图生成15秒品牌短片_2087898553539710978.json, 视频生成/文生视频/Minimax H3 全自动短片（要配合提示词skill使用）林耀_2091930702962057218.json, 视频生成/文生视频/动漫短剧全自动工作流V5（海螺MinimaxH3）（自动循环+自动延长）_2089665991025455105.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_120

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/一键生成一分钟长视频 Minimax H3_2088144166755856385.json、视频生成/图生视频/Minimax H3 全自动小短片_2087477277696282625.json、视频生成/图生视频/Minimax+H3+全自动小短片+二采高清4+2_2096828253884473345.json、视频生成/图生视频/Minimax+H3+全自动小短片+二采高清8+4_2096863166981566465.json、视频生成/图生视频/ONE SHOT STORY｜MiniMax H3 一图生成15秒品牌短片_2087898553539710978.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtractLinesByIndex`
- `Int Literal`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MotionContext`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
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
- `LoadAudio` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `MiniMaxH3MotionContextTrim` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `Text To Image (mtb)` —— 6/7 个有
- `easy batchAnything` —— 6/7 个有
- `Text String Truncate` —— 4/7 个有
- `DF_Float` —— 2/7 个有
- `LTXVConcatAVLatent` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `MinimaxH3LatentUpscaler3D` —— 2/7 个有
- `SplitSigmas` —— 2/7 个有
- `CreateVideo` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `SaveVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
