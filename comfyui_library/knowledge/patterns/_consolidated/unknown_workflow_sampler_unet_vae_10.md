---
name: unknown_workflow_sampler_unet_vae_10
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.783739
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3图生视频工作流_2102372635475791873.json, 视频生成/图生视频/MINIMAX-H3首尾帧视频_2085192239885668354.json, 视频生成/图生视频/Mini max  H3开源啦(加速版）_2085639639234338818.json, 视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084172305701367810.json, 视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084193937832632322.json, 视频生成/图生视频/MiniMax H3  动画与风格化影像_2084557369203322882.json, 视频生成/图生视频/MiniMax H3 -全能参考生视频-情景剧_2085386101346365442.json, 视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜BF16 20步高质量基线版_2090727907718164481.json, 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2111345897249533954.json, 视频生成/图生视频/MiniMax H3 Ref2VA多图参考生视频-导演级官方提示词标准化模板_2084942982297505793.json, 视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json, 视频生成/图生视频/MiniMax H3 全能参考｜图生视频工作流（优化版）_2090248587761512450.json, 视频生成/图生视频/MiniMax H3 多图参考+官方提示词模板+提速40%无劣化 真人短剧剧情演绎_2084620840548786177.json, 视频生成/图生视频/MiniMax H3 多图参考+官方提示词模板+提速40%无劣化_2083480380576976897.json, 视频生成/图生视频/MiniMax H3 极速首尾帧图生视频_2087539459008057345.json, 视频生成/图生视频/MiniMax H3_图生视频工作流_2084485598643048450.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2084154545424388098.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2087935494813478914.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2099783471219699713.json, 视频生成/图生视频/海螺H3-全自动图生视频-自动撰写提示词_2086431051328614402.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图-动态去高躁_2088657311995879425.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2085050902129504257.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2087936662021173250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3图生视频工作流_2102372635475791873.json、视频生成/图生视频/MINIMAX-H3首尾帧视频_2085192239885668354.json、视频生成/图生视频/Mini max  H3开源啦(加速版）_2085639639234338818.json、视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084172305701367810.json、视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084193937832632322.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 22/23 个有
- `PrimitiveFloat` —— 22/23 个有
- `ResolutionSelector` —— 22/23 个有
- `CreateVideo` —— 18/23 个有
- `SaveVideo` —— 18/23 个有
- `MiniMaxH3ImageToVideo` —— 15/23 个有
- `PathchSageAttentionKJ` —— 15/23 个有
- `LoraLoaderModelOnly` —— 11/23 个有
- `easy showAnything` —— 11/23 个有
- `EasyCache` —— 9/23 个有
- `MiniMaxH3ReferenceToVideo` —— 8/23 个有
- `SolAttnPatch` —— 8/23 个有
- `VHS_VideoCombine` —— 8/23 个有
- `MiniMaxH3BlockCacheT8` —— 7/23 个有
- `Int` —— 5/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/23 个有
- `PrimitiveStringMultiline` —— 4/23 个有
- `Text` —— 4/23 个有
- `GetNode` —— 3/23 个有
- `ModelPatchTorchSettings` —— 3/23 个有
- `SetNode` —— 3/23 个有
- `ImageResizeKJv2` —— 2/23 个有
- `ExtendIntermediateSigmas` —— 1/23 个有
- `H3SigmaRefiner` —— 1/23 个有
- `Label (rgthree)` —— 1/23 个有
- `RHMiniMaxH3PromptOptimizerCompact` —— 1/23 个有
- `RH_LLMAPI_Pro_Node` —— 1/23 个有
- `StringFunction|pysssss` —— 1/23 个有
- `孤海注释` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
