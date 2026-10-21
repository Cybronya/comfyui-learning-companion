---
name: unknown_workflow_video_sampler_unet_12
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.664739
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json, 视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json, 视频生成/图生视频/【MiniMax H3】短剧工作流_2110380691388194818.json, 视频生成/图生视频/【MiniMax_H3】短剧工作流_2110893565873311745.json, 视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json, 视频生成/图生视频/单图Minimax H3_2084901814679461889.json, 视频生成/图生视频/文戏_2095407932757331970.json, 视频生成/图生视频/海螺1080全能参考生视频v2-带视频_2089977803579150337.json, 视频生成/图生视频/海螺1080全能参考生视频v2-带音频_2089977775015948289.json, 视频生成/图生视频/海螺1080全能参考生视频v2_2088548493907550210.json, 视频生成/图生视频/海螺480全能参考生视频v2_2088511013770584066.json, 视频生成/图生视频/海螺720全能参考生视频v2-带视频_2089977416050630658.json, 视频生成/图生视频/海螺720全能参考生视频v2-带音频_2089977064664424450.json, 视频生成/图生视频/海螺720全能参考生视频v2_2088533399135932418.json, 视频生成/文生视频/MINIMAX-H3全能参考-低配文戏版_2095278454672543745.json, 视频生成/文生视频/MINIMAX-H3原本fl2va分布高低解码二采_2104191255403122689.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095318851016806402.json, 视频生成/文生视频/MiniMax H3全能参考-武戏版｜可选提示词（手动输入 & 自动生成）_2095913508104916993.json, 视频生成/文生视频/Minimax-H3剧情片工作台_2096851323793797122.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-低配版_2100800495819517953.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-高配版_2100787794460372994.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2098355739667554306.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2094683715619348482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json、视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json、视频生成/图生视频/【MiniMax H3】短剧工作流_2110380691388194818.json、视频生成/图生视频/【MiniMax_H3】短剧工作流_2110893565873311745.json、视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 22/23 个有
- `LoraLoaderModelOnly` —— 21/23 个有
- `INTConstant` —— 19/23 个有
- `LoadAudio` —— 19/23 个有
- `CR Prompt Text` —— 18/23 个有
- `H3SigmaRefiner` —— 18/23 个有
- `GetNode` —— 17/23 个有
- `LTXVConcatAVLatent` —— 17/23 个有
- `LTXVSeparateAVLatent` —— 17/23 个有
- `MinimaxH3LatentUpscaler3D` —— 17/23 个有
- `SetNode` —— 17/23 个有
- `PrimitiveFloat` —— 16/23 个有
- `SolAttnMiniMax` —— 12/23 个有
- `忽略多组孤海` —— 12/23 个有
- `ExtendIntermediateSigmas` —— 11/23 个有
- `LoraLoaderBypassModelOnly` —— 11/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/23 个有
- `MiniMaxH3SigmaShift` —— 8/23 个有
- `PreviewImage` —— 8/23 个有
- `CM_IntToFloat` —— 7/23 个有
- `FloatConstant` —— 7/23 个有
- `ManualSigmas` —— 7/23 个有
- `ResizeShortestToNode` —— 7/23 个有
- `SplitSigmas` —— 7/23 个有
- `VHS_LoadVideo` —— 7/23 个有
- `easy showAnything` —— 7/23 个有
- `PrimitiveStringMultiline` —— 6/23 个有
- `ModelPreviewOverrideKJ` —— 3/23 个有
- `Any Switch (rgthree)` —— 2/23 个有
- `MuyeTextEditOutput` —— 2/23 个有
- `RH_LLMAPI_Pro_Node` —— 2/23 个有
- `EmptyImage` —— 1/23 个有
- `MiniMaxH3BlockCacheT8` —— 1/23 个有
- `PlaySound|pysssss` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
