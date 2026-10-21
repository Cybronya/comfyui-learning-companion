---
name: text_to_image_video_lora_sampler_13
type: Text To Image
frequency: 28
level: strong
coverage: 0.603
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MiniMax H3 Ref2VA六图多参考角色一致性Sage加速文生图_2088251941397815297.json, 图片生成/文生图/文生视频 MiniMax H3_2097845481618624513.json, 数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json, 数字人/数字人/Minimax H3多参考口播｜数字人口播素材多路喂｜口型和画面都对得上_2102653513489805313.json, 数字人/数字人/优化版本新版口播方案，数字人视频生视频制作_2111284544136630274.json, 数字人/数字人/官方提示词模板提速40%｜MiniMax H3多图参考真人短剧演绎_2090193856364109826.json, 数字人/数字人/新版口播数字人视频生成工作流｜视频生视频一键出片_2108369479599218690.json, 视频生成/图生视频/4步加速Lora二采高清放大｜H3全能参考图生视频画质增强_2088721636932538369.json, 视频生成/图生视频/4步加速Lora｜H3全能参考二采高清放大图生视频_2089065029676134402.json, 视频生成/图生视频/720P MiniMax H3超级多合一官方版｜图生视频工作流_2094857234391064577.json, 视频生成/图生视频/H3 Model High-Speed  美女模特图生视频直出 H3模型高速生成视频_2094945625723985922.json, 视频生成/图生视频/H3全能参考二采放大 图生视频高质量输出_2098282282468601858.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2090298920558747649.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2091428235719565313.json, 视频生成/图生视频/H3超级多合一工作流官方版 全功能视频生成_2100278481891450882.json, 视频生成/图生视频/MINIMAX-H3全能参考去油防脸崩-视频生视频图生视频_2087370270070886402.json, 视频生成/图生视频/MiniMax H3超级多合一官方版工作流｜多模式视频生成_2094500712767115265.json, 视频生成/图生视频/MiniMax H3超级多合一工作流官方版｜全能参考生成_2094499255737208833.json, 视频生成/图生视频/全能参考二采高清放大｜H3 4步加速Lora图生视频_2096298417860468738.json, 视频生成/图生视频/全能参考去油防MINIMAX-H3脸崩工作流ENG_2087124608590901249.json, 视频生成/图生视频/双采去水印版多图参考｜MiniMax H3视频生成直出_2093427385231302657.json, 视频生成/图生视频/双采去水印版｜MiniMax H3多图参考图生视频生成_2093758899559165953.json, 视频生成/图生视频/超级多合一官方V2｜MiniMax H3场景特效图生视频_2089454565593804802.json, 视频生成/图生视频/超级多合一官方版｜YZ金鱼 MiniMax H3图生图生视频_2094723951757971458.json, 视频生成/文生视频/MiniMax H3超级多合一工作流官方版V2文生视频图生视频持续优化_2088350962753826818.json, 视频生成/文生视频/傲雪AIGC短剧双采｜MiniMax H3文生图生视频工作流_2093212268778582018.json, 视频生成/文生视频/多参2采8步加速｜MiniMax H3文生图生视频生成_2091601751957925889.json, 视频生成/文生视频/多参二采8步加速｜MiniMax H3视频生成提速_2091773543188090881.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 Ref2VA六图多参考角色一致性Sage加速文生图_2088251941397815297.json、图片生成/文生图/文生视频 MiniMax H3_2097845481618624513.json、数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json、数字人/数字人/Minimax H3多参考口播｜数字人口播素材多路喂｜口型和画面都对得上_2102653513489805313.json、数字人/数字人/优化版本新版口播方案，数字人视频生视频制作_2111284544136630274.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 27/28 个有
- `MiniMaxH3ReferenceToVideo` —— 27/28 个有
- `GetNode` —— 26/28 个有
- `SetNode` —— 26/28 个有
- `孤海注释` —— 26/28 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 23/28 个有
- `Text` —— 23/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 22/28 个有
- `ImageResizeKJv2` —— 21/28 个有
- `LoadAudio` —— 21/28 个有
- `VAEEncode` —— 21/28 个有
- `VHS_LoadVideo` —— 21/28 个有
- `VAEDecodeAudio` —— 20/28 个有
- `Fast Groups Bypasser (rgthree)` —— 19/28 个有
- `PreviewImage` —— 19/28 个有
- `VAEEncodeAudio` —— 18/28 个有
- `ModelAttentionBackend` —— 15/28 个有
- `easy cleanGpuUsed` —— 14/28 个有
- `LTXVConcatAVLatent` —— 11/28 个有
- `PT_H3ConcatAVLatent` —— 10/28 个有
- `MiniMaxH3ImageToVideo` —— 9/28 个有
- `MiniMaxH3AVDecodeT8` —— 8/28 个有
- `PathchSageAttentionKJ` —— 7/28 个有
- `RunningHub Deepcleaner` —— 4/28 个有
- `CR Prompt Text` —— 3/28 个有
- `LoraLoaderBypassModelOnly` —— 3/28 个有
- `MiniMaxH3AddGuide` —— 3/28 个有
- `SaveImage` —— 3/28 个有
- `EasyCache` —— 2/28 个有
- `GetImageSize` —— 2/28 个有
- `ResizeImageMaskNode` —— 2/28 个有
- `SaveVideo` —— 2/28 个有
- `Textbox` —— 2/28 个有
- `EmptyImage` —— 1/28 个有
- `PlaySound|pysssss` —— 1/28 个有
- `VHS_LoadVideoFFmpeg` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 28 | 100% |
| 采样算法 | er_sde | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |
| 宽度 | 80 | 80 - 80 | 28 | 100% |
| 高度 | 80 | 80 - 80 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
