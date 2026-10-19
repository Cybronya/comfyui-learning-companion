---
name: unknown_workflow_video_lora_sampler_68
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.518167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3开源 最强文戏-低配版_2094767825419333634.json, 视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json, 视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json, 视频生成/图生视频/MiniMax H3-单采_2102816230406189058.json, 视频生成/图生视频/YZ金鱼-MiniMax H3超级多合一工作流-官方版_2093245007657521154.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-1参考图_2109836744655986690.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-5参考图_2095824845220171777.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采2_2109836609779757057.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2100179119110705153.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2101865695603683329.json, 视频生成/图生视频/【MINIMAX-H3】最强W版武戏-极速版_2111450852316770305.json, 视频生成/图生视频/【MINIMAX-H3】最强打斗武戏双采工作流（自动提示词）_2096434163439198209.json, 视频生成/图生视频/文戏_2095407932757331970.json, 视频生成/文生视频/MINIMAX-H3全能参考-低配文戏版_2095278454672543745.json, 视频生成/文生视频/MINIMAX-H3原本fl2va分布高低解码二采_2104191255403122689.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095318851016806402.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095913508104916993.json, 视频生成/文生视频/Minimax-H3剧情片工作台_2096851323793797122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3开源 最强文戏-低配版_2094767825419333634.json、视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json、视频生成/图生视频/MiniMax H3 + VOSR2 文戏短剧（低配单采样2K）_2097340183623589889.json、视频生成/图生视频/MiniMax H3-单采_2102816230406189058.json、视频生成/图生视频/YZ金鱼-MiniMax H3超级多合一工作流-官方版_2093245007657521154.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 17/18 个有
- `PreviewImage` —— 17/18 个有
- `PrimitiveFloat` —— 17/18 个有
- `ExtendIntermediateSigmas` —— 16/18 个有
- `H3SigmaRefiner` —— 16/18 个有
- `LoadAudio` —— 16/18 个有
- `CR Prompt Text` —— 15/18 个有
- `忽略多组孤海` —— 15/18 个有
- `INTConstant` —— 13/18 个有
- `LTXVConcatAVLatent` —— 12/18 个有
- `LTXVSeparateAVLatent` —— 12/18 个有
- `MinimaxH3LatentUpscaler3D` —— 12/18 个有
- `RH_LLMAPI_Pro_Node` —— 3/18 个有
- `Text` —— 3/18 个有
- `Any Switch (rgthree)` —— 2/18 个有
- `EmptyImage` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `MuyeTextEditOutput` —— 2/18 个有
- `Float` —— 1/18 个有
- `MiniMaxChunkFeedForward` —— 1/18 个有
- `MiniMaxLowVRAMAttention` —— 1/18 个有
- `PlaySound|pysssss` —— 1/18 个有
- `PreviewAny` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `ShowText|pysssss` —— 1/18 个有
- `VHS_LoadVideo` —— 1/18 个有
- `VOSR2ModelLoader` —— 1/18 个有
- `VOSR2Upscale` —— 1/18 个有
- `XB_BatchImages` —— 1/18 个有
- `llama_cpp_instruct_adv` —— 1/18 个有
- `llama_cpp_model_loader` —— 1/18 个有
- `llama_cpp_parameters` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
