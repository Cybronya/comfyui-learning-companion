---
name: unknown_workflow_upscale_latent_upscale_lora_12
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.6872
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3数字人视频带货H3多图生视频电商带货视频数字人视频_2108913611300237314.json, 视频生成/图生视频/MiniMaxH3数字人视频带货H3多图生视频电商带货视频数字人视频_2110325567538159618.json, 视频生成/图生视频/MiniMaxH3数字人视频带货！H3多图生视频！_2104537388365213698.json, 视频生成/图生视频/MiniMaxH3数字人视频带货！H3多图生视频！艾橘溪_2088870328951984130.json, 视频生成/图生视频/MiniMaxH3数字人视频带货！H3多图生视频！艾橘溪_2100540179919491073.json, 视频生成/图生视频/MiniMaxH3数字人视频带货！效果超好！_2096285325629935618.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大文戏工作流_2096179690426949633.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武器对决工作流_2096593027769913345.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武戏工作流_2096227914462355458.json, 视频生成/图生视频/Minimax H3 多图参考 真实感极佳_2092151387793747970.json, 视频生成/图生视频/Minimax H3-SelfLift双采对比普通双采_2101283145361481729.json, 视频生成/图生视频/Minimax H3双模双采工作流-小脸不崩-脸不油，高动态不崩脸_2093185884203085826.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3双模双采工作流_2091613369202724865.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091830576230780930.json, 视频生成/文生视频/Minimax H3优化！浅空间二次放大！优化小脸和打斗_2087552804436140033.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3数字人视频带货H3多图生视频电商带货视频数字人视频_2108913611300237314.json、视频生成/图生视频/MiniMaxH3数字人视频带货H3多图生视频电商带货视频数字人视频_2110325567538159618.json、视频生成/图生视频/MiniMaxH3数字人视频带货！H3多图生视频！_2104537388365213698.json、视频生成/图生视频/MiniMaxH3数字人视频带货！H3多图生视频！艾橘溪_2088870328951984130.json、视频生成/图生视频/MiniMaxH3数字人视频带货！H3多图生视频！艾橘溪_2100540179919491073.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `CreateVideo` —— 9/15 个有
- `SaveVideo` —— 9/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/15 个有
- `VHS_VideoCombine` —— 8/15 个有
- `H3SigmaRefiner` —— 7/15 个有
- `ManualSigmas` —— 7/15 个有
- `ModelAttentionBackend` —— 7/15 个有
- `SplitSigmas` —— 7/15 个有
- `easy cleanGpuUsed` —— 7/15 个有
- `JjkText` —— 6/15 个有
- `MiniMaxH3SigmaShift` —— 6/15 个有
- `MiniMaxLowVRAMAttention` —— 6/15 个有
- `ModelPreviewOverrideKJ` —— 6/15 个有
- `PrimitiveStringMultiline` —— 6/15 个有
- `孤海注释` —— 6/15 个有
- `CR Prompt Text` —— 3/15 个有
- `ExtendIntermediateSigmas` —— 2/15 个有
- `SplitSigmasDenoise` —— 2/15 个有
- `AddLabel` —— 1/15 个有
- `ConditioningZeroOut` —— 1/15 个有
- `ImageConcatMulti` —— 1/15 个有
- `MiniMaxChunkFeedForward` —— 1/15 个有
- `SelfLiftH3Sampler` —— 1/15 个有
- `StringConcatenate` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
