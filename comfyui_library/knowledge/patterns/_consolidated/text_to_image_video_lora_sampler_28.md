---
name: text_to_image_video_lora_sampler_28
type: Text To Image
frequency: 20
level: strong
coverage: 0.7023
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3极简版多合一工作流 轻量化图生图处理_2099557718532116482.json, 图片生成/图生图/H3极简版多合一工作流 轻量图生图处理 高效便捷_2099580692500934657.json, 图片生成/图生图/H3极简版多合一工作流 轻量图生图处理工具_2099571903122989058.json, 图片生成/图生图/MINIMAX-H3八月最强文戏低配版｜图生图轻量出片_2100818358718525441.json, 图片生成/图生图/MiniMax H3多参考生视频666版｜多图参考融合生成，一致性拉满_2107319483974111233.json, 图片生成/图生图/MiniMax H3极简版多合一工作流 轻量化图生图处理_2099193283837779969.json, 图片生成/图生图/MiniMax H3极简版多合一工作流 轻量图生图处理_2099204275854462977.json, 图片生成/图生图/MinimaxH3极简版多合一｜节点精简跑得快，多场景一条流搞定_2099555256848961538.json, 图片生成/文生图/8.31最佳多参考｜MiniMax H3反推提示词生视频_2094730905653956609.json, 图片生成/文生图/MiniMax H3多参考生视频工作流，文生图图生图多参考视频生成方案_2107562264558653442.json, 图片生成/文生图/MiniMax H3多参考生视频工作流，文生图图生图多参考视频生成方案_2107940300458119170.json, 视频生成/图生视频/1080全能参考生视频｜海螺v2图生视频直出_2093816760570044417.json, 视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json, 视频生成/图生视频/H3_People_Dancing人物跳舞｜多种舞蹈风格自动机_2107669075152433153.json, 视频生成/图生视频/MINIMAX-H3八月最强文戏低配版，单采2省显存出片_2110864933956177921.json, 视频生成/图生视频/带视频1080全能参考｜海螺v2视频生视频生成_2094014088853680129.json, 视频生成/图生视频/带视频1080全能参考｜海螺生视频v2视频生视频_2093786874312749058.json, 视频生成/图生视频/带视频720全能参考｜海螺v2生视频生成工作流_2094038101344739330.json, 视频生成/图生视频/带音频1080全能参考｜海螺生视频v2图生视频_2093785361196605441.json, 视频生成/图生视频/海螺480全能参考v2｜视频图生视频一键直出_2090200734355775489.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/H3极简版多合一工作流 轻量化图生图处理_2099557718532116482.json、图片生成/图生图/H3极简版多合一工作流 轻量图生图处理 高效便捷_2099580692500934657.json、图片生成/图生图/H3极简版多合一工作流 轻量图生图处理工具_2099571903122989058.json、图片生成/图生图/MINIMAX-H3八月最强文戏低配版｜图生图轻量出片_2100818358718525441.json、图片生成/图生图/MiniMax H3多参考生视频666版｜多图参考融合生成，一致性拉满_2107319483974111233.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 19/20 个有
- `LTXVSeparateAVLatent` —— 19/20 个有
- `LoadImage` —— 19/20 个有
- `MinimaxH3LatentUpscaler3D` —— 19/20 个有
- `GetNode` —— 18/20 个有
- `LoadAudio` —— 18/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/20 个有
- `SetNode` —— 18/20 个有
- `SplitSigmas` —— 17/20 个有
- `ComfyMathExpression` —— 14/20 个有
- `MiniMaxH3ReferenceToVideo` —— 14/20 个有
- `ResolutionSelector` —— 14/20 个有
- `CR Prompt Text` —— 10/20 个有
- `ModelAttentionBackend` —— 10/20 个有
- `PreviewImage` —— 10/20 个有
- `VHS_LoadVideo` —— 10/20 个有
- `EmptyImage` —— 9/20 个有
- `SaveImage` —— 9/20 个有
- `Text` —— 9/20 个有
- `INTConstant` —— 8/20 个有
- `MiniMaxH3SigmaShift` —— 8/20 个有
- `PrimitiveFloat` —— 8/20 个有
- `easy showAnything` —— 8/20 个有
- `H3SigmaRefiner` —— 7/20 个有
- `CM_IntToFloat` —— 6/20 个有
- `FloatConstant` —— 6/20 个有
- `MiniMaxH3Easy` —— 6/20 个有
- `MiniMaxH3EasyLoader` —— 6/20 个有
- `MiniMaxH3EasyOutput` —— 6/20 个有
- `ResizeShortestToNode` —— 6/20 个有
- `SolAttnMiniMax` —— 6/20 个有
- `LoadVideo` —— 5/20 个有
- `LoraLoaderBypassModelOnly` —— 5/20 个有
- `ManualSigmas` —— 5/20 个有
- `easy float` —— 4/20 个有
- `ExtendIntermediateSigmas` —— 2/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/20 个有
- `ModelPreviewOverrideKJ` —— 2/20 个有
- `RHHiddenNodes` —— 2/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（22/20 个样本）：Steps较低可能导致细节不足
