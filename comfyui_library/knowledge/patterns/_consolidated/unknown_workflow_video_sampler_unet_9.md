---
name: unknown_workflow_video_sampler_unet_9
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.52568
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json, 视频生成/图生视频/h3图生视频gy_2087784031445413890.json, 视频生成/图生视频/minimax h3电商产品_2095444070079492097.json, 视频生成/图生视频/poster animation_2094321304538279938.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-1参考图_2109836744655986690.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-5参考图_2095824845220171777.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采2_2109836609779757057.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2100179119110705153.json, 视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版_2101865695603683329.json, 视频生成/图生视频/【MINIMAX-H3】最强打斗武戏双采工作流（自动提示词）_2096434163439198209.json, 视频生成/图生视频/文戏_2095407932757331970.json, 视频生成/图生视频/测试01剧本 YZ金鱼-MiniMax H3-多参考生视频-优化版_2107313229809672193.json, 视频生成/图生视频/金鱼-多参考生视频-电影感_2094788063007432706.json, 视频生成/图生视频/（最强一致性Singularity_v2）Minimax_H3多参考双采生视频_2113793684742434817.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频_2097875587942666242.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频多比例版本_2104119164674859010.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2096460541328973825.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2097340280092581890.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒竖屏960分辨率）_2096477149321580546.json, 视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json, 视频生成/文生视频/MINIMAX-H3全能参考-低配文戏版_2095278454672543745.json, 视频生成/文生视频/MINIMAX-H3原本fl2va分布高低解码二采_2104191255403122689.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095318851016806402.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095913508104916993.json, 视频生成/文生视频/Minimax-H3剧情片工作台_2096851323793797122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_9

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json、视频生成/图生视频/h3图生视频gy_2087784031445413890.json、视频生成/图生视频/minimax h3电商产品_2095444070079492097.json、视频生成/图生视频/poster animation_2094321304538279938.json、视频生成/图生视频/【MINIMAX-H3】八月最强文戏-低配版-单采-1参考图_2109836744655986690.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 24/25 个有
- `LTXVConcatAVLatent` —— 24/25 个有
- `LTXVSeparateAVLatent` —— 24/25 个有
- `MinimaxH3LatentUpscaler3D` —— 24/25 个有
- `PrimitiveFloat` —— 24/25 个有
- `ResolutionSelector` —— 24/25 个有
- `SetNode` —— 24/25 个有
- `LoadAudio` —— 22/25 个有
- `忽略多组孤海` —— 22/25 个有
- `ModelAttentionBackend` —— 20/25 个有
- `LoraLoaderModelOnly` —— 18/25 个有
- `H3SigmaRefiner` —— 13/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/25 个有
- `PreviewImage` —— 13/25 个有
- `CR Prompt Text` —— 12/25 个有
- `ExtendIntermediateSigmas` —— 12/25 个有
- `Text` —— 12/25 个有
- `INTConstant` —— 11/25 个有
- `SplitSigmas` —— 11/25 个有
- `easy float` —— 11/25 个有
- `VHS_LoadVideo` —— 9/25 个有
- `Lora Loader Stack (rgthree)` —— 7/25 个有
- `SolAttnMiniMax` —— 7/25 个有
- `EmptyImage` —— 3/25 个有
- `Label (rgthree)` —— 3/25 个有
- `RH_LLMAPI_Pro_Node` —— 3/25 个有
- `Any Switch (rgthree)` —— 2/25 个有
- `MuyeTextEditOutput` —— 2/25 个有
- `easy int` —— 2/25 个有
- `JjkText` —— 1/25 个有
- `LayerUtility: TextJoin` —— 1/25 个有
- `PlaySound|pysssss` —— 1/25 个有
- `PreviewAny` —— 1/25 个有
- `PrimitiveStringMultiline` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
