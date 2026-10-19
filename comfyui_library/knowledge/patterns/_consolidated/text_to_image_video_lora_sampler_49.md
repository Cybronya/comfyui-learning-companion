---
name: text_to_image_video_lora_sampler_49
type: Text To Image
frequency: 13
level: strong
coverage: 0.776308
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1080全能参考生视频｜海螺v2图生视频直出_2093816760570044417.json, 视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json, 视频生成/图生视频/H3_People_Dancing人物跳舞｜多种舞蹈风格自动机_2107669075152433153.json, 视频生成/图生视频/H3一键角色替换 图生视频换人剪辑神器工作流推荐_2094810569621725186.json, 视频生成/图生视频/H3角色替换工作流｜视频人物替换图生视频生成_2094905654396940289.json, 视频生成/图生视频/MiniMax H3全能插件加音频设计 视频加音效一站式方案_2105420482479742977.json, 视频生成/图生视频/MiniMax H3全能插件升级｜音频设计加持视频创作_2105253049693458433.json, 视频生成/图生视频/带视频1080全能参考｜海螺v2视频生视频生成_2094014088853680129.json, 视频生成/图生视频/带视频1080全能参考｜海螺生视频v2视频生视频_2093786874312749058.json, 视频生成/图生视频/带视频720全能参考｜海螺v2生视频生成工作流_2094038101344739330.json, 视频生成/图生视频/带音频1080全能参考｜海螺生视频v2图生视频_2093785361196605441.json, 视频生成/图生视频/显存终极优化｜MINIMAX-H3视频图生视频工作流_2090556860897259521.json, 视频生成/图生视频/武打戏特化制作｜MINIMAX-H3视频生视频图生视频_2092210437902393346.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1080全能参考生视频｜海螺v2图生视频直出_2093816760570044417.json、视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json、视频生成/图生视频/H3_People_Dancing人物跳舞｜多种舞蹈风格自动机_2107669075152433153.json、视频生成/图生视频/H3一键角色替换 图生视频换人剪辑神器工作流推荐_2094810569621725186.json、视频生成/图生视频/H3角色替换工作流｜视频人物替换图生视频生成_2094905654396940289.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MinimaxH3LatentUpscaler3D` —— 12/13 个有
- `ModelAttentionBackend` —— 12/13 个有
- `H3SigmaRefiner` —— 11/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/13 个有
- `VHS_LoadVideo` —— 9/13 个有
- `PrimitiveFloat` —— 8/13 个有
- `CR Prompt Text` —— 7/13 个有
- `GetNode` —— 7/13 个有
- `LoadAudio` —— 7/13 个有
- `SetNode` —— 7/13 个有
- `easy showAnything` —— 7/13 个有
- `ModelPreviewOverrideKJ` —— 6/13 个有
- `PrimitiveStringMultiline` —— 6/13 个有
- `CM_IntToFloat` —— 5/13 个有
- `FloatConstant` —— 5/13 个有
- `INTConstant` —— 5/13 个有
- `LoraLoaderBypassModelOnly` —— 5/13 个有
- `ManualSigmas` —— 5/13 个有
- `ResizeShortestToNode` —— 5/13 个有
- `SaveImage` —— 5/13 个有
- `SolAttnMiniMax` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `MiniMaxLowVRAMAttention` —— 4/13 个有
- `PreviewImage` —— 4/13 个有
- `EmptyImage` —— 2/13 个有
- `FlashVSRNode` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `MiniMaxChunkFeedForward` —— 2/13 个有
- `MiniMaxH3Unified` —— 2/13 个有
- `RHHiddenNodes` —— 2/13 个有
- `Sleep` —— 2/13 个有
- `Vignette` —— 2/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
