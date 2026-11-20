---
name: unknown_workflow_video_lora_sampler_120
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.548438
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ExtendIntermediateSigmas, H3SigmaRefiner, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/【角色迁移】Minimax H3换人+双采工作流【AI小王子】_2113545794325409794.json, 数字人/数字人/【MINIMAX-H3】八月最强文戏-低配版_2100034371259555842.json, 视频生成/图生视频/MINIMAX-H3-全自动打斗武戏-15秒8分钟_2097790484570796033.json, 视频生成/图生视频/MINIMAX-H3开源 最强文戏-低配版_2094767825419333634.json, 视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-1参考图_2109836744655986690.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-5参考图_2095824845220171777.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采2_2109836609779757057.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2100179119110705153.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2101865695603683329.json, 视频生成/图生视频/【MINIMAX-H3】最强打斗武戏双采工作流（自动提示词）_2096434163439198209.json, 视频生成/图生视频/文戏_2095407932757331970.json, 视频生成/文生视频/MINIMAX-H3全能参考-低配文戏版_2095278454672543745.json, 视频生成/文生视频/MINIMAX-H3原本fl2va分布高低解码二采_2104191255403122689.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095318851016806402.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095913508104916993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（平台全量/【角色迁移】Minimax H3换人+双采工作流【AI小王子】_2113545794325409794.json、数字人/数字人/【MINIMAX-H3】八月最强文戏-低配版_2100034371259555842.json、视频生成/图生视频/MINIMAX-H3-全自动打斗武戏-15秒8分钟_2097790484570796033.json、视频生成/图生视频/MINIMAX-H3开源 最强文戏-低配版_2094767825419333634.json、视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
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
- `CR Prompt Text` —— 15/16 个有
- `GetNode` —— 15/16 个有
- `INTConstant` —— 15/16 个有
- `PreviewImage` —— 15/16 个有
- `SetNode` —— 15/16 个有
- `忽略多组孤海` —— 15/16 个有
- `LTXVConcatAVLatent` —— 14/16 个有
- `LTXVSeparateAVLatent` —— 14/16 个有
- `MinimaxH3LatentUpscaler3D` —— 14/16 个有
- `RH_LLMAPI_Pro_Node` —— 4/16 个有
- `Any Switch (rgthree)` —— 2/16 个有
- `EmptyImage` —— 2/16 个有
- `MuyeTextEditOutput` —— 2/16 个有
- `PreviewAny` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `ImageFromBatch` —— 1/16 个有
- `ManualSigmas` —— 1/16 个有
- `MiniMaxChunkFeedForward` —— 1/16 个有
- `MiniMaxLowVRAMAttention` —— 1/16 个有
- `PlaySound|pysssss` —— 1/16 个有
- `PrimitiveInt` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `Text Multiline` —— 1/16 个有
- `VHS_LoadVideoFFmpeg` —— 1/16 个有
- `VOSR2ModelLoader` —— 1/16 个有
- `VOSR2Upscale` —— 1/16 个有
- `c852b01f-c0f1-4c6a-89ab-a81efe05aea9` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有
- `孤海注释` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
