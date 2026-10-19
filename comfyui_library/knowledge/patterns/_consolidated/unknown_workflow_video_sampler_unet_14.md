---
name: unknown_workflow_video_sampler_unet_14
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.492111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)_2084210400207396866.json, 视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)真人短剧加速版_2084291490649567233.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+图生视频+1280分辨率加速流_2085330041017298945.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+（首帧）_2084283095339065346.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085589980080070658.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考+数字人+人物音频一致性_2086164860592807937.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考（1280分辨率）加速流_2085330061422579714.json, 视频生成/图生视频/AI代码侠土豆-MiniMax H3 T2V（文生视频）_2084169620658937858.json, 视频生成/图生视频/H3 动漫转真人+ 指定人物_2093180746625273857.json, 视频生成/图生视频/H3_动作迁移 + 深度视频参考_2090034137221648385.json, 视频生成/图生视频/MMH3全能参考生视频自用调优版（附带视频续接教程）_2096409310929702913.json, 视频生成/图生视频/MiniMax H3-图生视频_2103135562264834050.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2108223200814518274.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2108234638559899650.json, 视频生成/图生视频/MiniMax H3-多参考生视频-去油王版_2094419718181572610.json, 视频生成/图生视频/MiniMax H3-多参考生视频-去油王版_2111461486425100290.json, 视频生成/图生视频/MiniMax H3-多参考生视频-高质量hybrid_2095884837700853761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_14

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)_2084210400207396866.json、视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)真人短剧加速版_2084291490649567233.json、视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+图生视频+1280分辨率加速流_2085330041017298945.json、视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+（首帧）_2084283095339065346.json、视频生成/图生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085589980080070658.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 16/18 个有
- `LoadImage` —— 16/18 个有
- `PrimitiveFloat` —— 16/18 个有
- `SetNode` —— 16/18 个有
- `MiniMaxH3ReferenceToVideo` —— 15/18 个有
- `LoraLoaderModelOnly` —— 14/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/18 个有
- `Label (rgthree)` —— 11/18 个有
- `LTXVConcatAVLatent` —— 8/18 个有
- `LTXVSeparateAVLatent` —— 8/18 个有
- `MinimaxH3LatentUpscaler3D` —— 8/18 个有
- `LoadAudio` —— 7/18 个有
- `SplitSigmas` —— 7/18 个有
- `VHS_LoadVideo` —— 7/18 个有
- `easy float` —— 7/18 个有
- `忽略多组孤海` —— 5/18 个有
- `MiniMaxH3ImageToVideo` —— 3/18 个有
- `SigmasGraph` —— 3/18 个有
- `孤海注释` —— 3/18 个有
- `Float` —— 2/18 个有
- `PlaySound|pysssss` —— 2/18 个有
- `easy cleanGpuUsed` —— 2/18 个有
- `CR Text` —— 1/18 个有
- `CR Text Concatenate` —— 1/18 个有
- `EasyCache` —— 1/18 个有
- `EmptyImage` —— 1/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `ImageScale` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `ModelPreviewOverrideKJ` —— 1/18 个有
- `PreviewAny` —— 1/18 个有
- `RH_LLMAPI_Pro_Node` —— 1/18 个有
- `ZNGB_AudioCrop` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
