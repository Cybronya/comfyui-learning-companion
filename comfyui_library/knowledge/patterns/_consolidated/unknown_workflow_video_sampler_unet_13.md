---
name: unknown_workflow_video_sampler_unet_13
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.557435
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json, 视频生成/图生视频/MiNiMaxH3_六图+三音频参考_2111108549219799042.json, 视频生成/图生视频/MiniMax H3  15s全参_2084269888650174465.json, 视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json, 视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-1参考图_2109836744655986690.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-5参考图_2095824845220171777.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采2_2109836609779757057.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2100179119110705153.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2101865695603683329.json, 视频生成/图生视频/【MINIMAX-H3】最强打斗武戏双采工作流（自动提示词）_2096434163439198209.json, 视频生成/图生视频/文戏_2095407932757331970.json, 视频生成/文生视频/MINIMAX-H3全能参考-低配文戏版_2095278454672543745.json, 视频生成/文生视频/MINIMAX-H3原本fl2va分布高低解码二采_2104191255403122689.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095318851016806402.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095913508104916993.json, 视频生成/文生视频/Minimax-H3剧情片工作台_2096851323793797122.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-低配版_2100800495819517953.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-高配版_2100787794460372994.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2094872667374571522.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2098355739667554306.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2094683715619348482.json, 视频生成/文生视频/【MINIMAX-H3】打斗版-二采_2101165086437109761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json、视频生成/图生视频/MiNiMaxH3_六图+三音频参考_2111108549219799042.json、视频生成/图生视频/MiniMax H3  15s全参_2084269888650174465.json、视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json、视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 22/23 个有
- `ModelAttentionBackend` —— 22/23 个有
- `GetNode` —— 21/23 个有
- `LoadAudio` —— 21/23 个有
- `SetNode` —— 21/23 个有
- `CR Prompt Text` —— 20/23 个有
- `ExtendIntermediateSigmas` —— 20/23 个有
- `H3SigmaRefiner` —— 20/23 个有
- `INTConstant` —— 20/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 20/23 个有
- `LoraLoaderModelOnly` —— 20/23 个有
- `忽略多组孤海` —— 20/23 个有
- `LTXVConcatAVLatent` —— 18/23 个有
- `LTXVSeparateAVLatent` —— 18/23 个有
- `MinimaxH3LatentUpscaler3D` —— 18/23 个有
- `PreviewImage` —— 17/23 个有
- `RH_LLMAPI_Pro_Node` —— 5/23 个有
- `PreviewAny` —— 3/23 个有
- `Any Switch (rgthree)` —— 2/23 个有
- `EmptyImage` —— 2/23 个有
- `LoraLoaderBypassModelOnly` —— 2/23 个有
- `MuyeTextEditOutput` —— 2/23 个有
- `PrimitiveStringMultiline` —— 2/23 个有
- `SolAttnMiniMax` —— 2/23 个有
- `Text` —— 2/23 个有
- `MiniMaxChunkFeedForward` —— 1/23 个有
- `MiniMaxH3BlockCacheT8` —— 1/23 个有
- `MiniMaxLowVRAMAttention` —— 1/23 个有
- `PlaySound|pysssss` —— 1/23 个有
- `VOSR2ModelLoader` —— 1/23 个有
- `VOSR2Upscale` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
