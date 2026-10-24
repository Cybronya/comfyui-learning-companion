---
name: unknown_workflow_lora_sampler_unet_29
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.5808
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_二次采样+放大武器对决工作流_2096593027769913345.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武戏工作流_2096227914462355458.json, 视频生成/图生视频/Minimax H3 多图参考 真实感极佳_2092151387793747970.json, 视频生成/图生视频/Minimax H3 脸不崩！打斗不糊！H3 sigma强化+超清放大，生成1080P视频，效果极佳，不过速度为普通流的2倍_2089537626373181442.json, 视频生成/图生视频/Minimax H3双模双采工作流-小脸不崩-脸不油，高动态不崩脸_2093185884203085826.json, 视频生成/图生视频/Minimax H3开源 小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流_2089663075422130178.json, 视频生成/图生视频/Minimax H3开源 小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流_2089687254284455937.json, 视频生成/图生视频/Minimaxh3双采浅空间放大_2092523112779837442.json, 视频生成/图生视频/h3潜空间放大工作流老八_2089878151064276994.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3双模双采工作流_2091613369202724865.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091830576230780930.json, 视频生成/文生视频/(0823修复）海螺H3 sigma强化+潜空间放大+高清人脸工作流_2091505787058348034.json, 视频生成/文生视频/H3 高清优化版-小脸不崩-运动不模糊_2089690104179810306.json, 视频生成/文生视频/Minimax H3 双采样全能参考高清工作流｜超分放大｜4倍加速｜8倍加速_2092731840196079618.json, 视频生成/文生视频/Minimax H3 双采样全能参考｜真实电影感｜超分高清放大｜4倍加速｜8倍加速_2094320738051383298.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_二次采样+放大武器对决工作流_2096593027769913345.json、视频生成/图生视频/MiniMax_H3_二次采样+放大武戏工作流_2096227914462355458.json、视频生成/图生视频/Minimax H3 多图参考 真实感极佳_2092151387793747970.json、视频生成/图生视频/Minimax H3 脸不崩！打斗不糊！H3 sigma强化+超清放大，生成1080P视频，效果极佳，不过速度为普通流的2倍_2089537626373181442.json、视频生成/图生视频/Minimax H3双模双采工作流-小脸不崩-脸不油，高动态不崩脸_2093185884203085826.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/15 个有
- `H3SigmaRefiner` —— 13/15 个有
- `MiniMaxH3SigmaShift` —— 13/15 个有
- `ModelAttentionBackend` —— 13/15 个有
- `PrimitiveStringMultiline` —— 13/15 个有
- `SplitSigmas` —— 13/15 个有
- `MinimaxH3LatentUpscaler3D` —— 12/15 个有
- `ModelPreviewOverrideKJ` —— 11/15 个有
- `MiniMaxLowVRAMAttention` —— 7/15 个有
- `SolAttnMiniMax` —— 7/15 个有
- `easy cleanGpuUsed` —— 6/15 个有
- `孤海注释` —— 5/15 个有
- `LoadAudio` —— 3/15 个有
- `MinimaxH3LatentUpscalerNode3D` —— 3/15 个有
- `CR Prompt Text` —— 2/15 个有
- `ExtendIntermediateSigmas` —— 2/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `FlashVSRNode` —— 2/15 个有
- `HAIGC_VideoLoader` —— 2/15 个有
- `Sleep` —— 2/15 个有
- `SplitSigmasDenoise` —— 2/15 个有
- `CR Text Concatenate` —— 1/15 个有
- `Float` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `MiniMaxChunkFeedForward` —— 1/15 个有
- `MiniMaxH3BlockCacheT8` —— 1/15 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/15 个有
- `MuyeTextEditOutput` —— 1/15 个有
- `StringConcatenate` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
