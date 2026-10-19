---
name: unknown_workflow_video_sampler_unet_25
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.57975
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/minimax h3文生视频双采高清流_2093374091788115970.json, 视频生成/文生视频/minimax_h3_r2v_video_edit视频编辑_2094267455395950594.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-低配版_2100800495819517953.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-高配版_2100787794460372994.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2094872667374571522.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2098355739667554306.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2094683715619348482.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2098599696725004290.json, 视频生成/文生视频/【MINIMAX-H3】打斗版-二采_2101165086437109761.json, 视频生成/文生视频/【二采-低配版】MinMaxh3日常短剧专用_2095180548556808193.json, 视频生成/文生视频/【二采】MinMaxh3动态打斗专用_2095187337885085698.json, 视频生成/文生视频/动漫短剧武戏最强工作流（模型、提示词二选一）_2095498147790417922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_25

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/minimax h3文生视频双采高清流_2093374091788115970.json、视频生成/文生视频/minimax_h3_r2v_video_edit视频编辑_2094267455395950594.json、视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-低配版_2100800495819517953.json、视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-高配版_2100787794460372994.json、视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2094872667374571522.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
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
- `CR Prompt Text` —— 11/12 个有
- `GetNode` —— 11/12 个有
- `LTXVConcatAVLatent` —— 11/12 个有
- `LTXVSeparateAVLatent` —— 11/12 个有
- `LoadImage` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `ExtendIntermediateSigmas` —— 10/12 个有
- `H3SigmaRefiner` —— 10/12 个有
- `INTConstant` —— 10/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/12 个有
- `MinimaxH3LatentUpscaler3D` —— 10/12 个有
- `LoadAudio` —— 9/12 个有
- `忽略多组孤海` —— 9/12 个有
- `PreviewImage` —— 7/12 个有
- `PreviewAny` —— 5/12 个有
- `RH_LLMAPI_Pro_Node` —— 4/12 个有
- `ManualSigmas` —— 2/12 个有
- `MiniMaxH3SigmaShift` —— 2/12 个有
- `ModelPreviewOverrideKJ` —— 2/12 个有
- `SplitSigmas` —— 2/12 个有
- `Int` —— 1/12 个有
- `LamSwitcherCase` —— 1/12 个有
- `LoraLoaderBypassModelOnly` —— 1/12 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
