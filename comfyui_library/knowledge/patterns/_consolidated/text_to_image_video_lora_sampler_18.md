---
name: text_to_image_video_lora_sampler_18
type: Text To Image
frequency: 20
level: strong
coverage: 0.58375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4步加速Lora二采高清放大｜H3全能参考图生视频画质增强_2088721636932538369.json, 视频生成/图生视频/4步加速Lora｜H3全能参考二采高清放大图生视频_2089065029676134402.json, 视频生成/图生视频/4步加速官方Skills提示词模板多参｜MINIMAX-H3图生视频工作流_2087201189288038401.json, 视频生成/图生视频/720P MiniMax H3超级多合一官方版｜图生视频工作流_2094857234391064577.json, 视频生成/图生视频/H3 Model High-Speed  美女模特图生视频直出 H3模型高速生成视频_2094945625723985922.json, 视频生成/图生视频/H3全能参考二采放大 图生视频高质量输出_2098282282468601858.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2090298920558747649.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2091428235719565313.json, 视频生成/图生视频/H3超级多合一工作流官方版 全功能视频生成_2100278481891450882.json, 视频生成/图生视频/Lightx2v+8步加速官模｜双模型双采样单图自动反推提词_2089395917622439937.json, 视频生成/图生视频/MINIMAX-H3全能参考去油防脸崩-视频生视频图生视频_2087370270070886402.json, 视频生成/图生视频/MiniMax H3超级多合一官方版工作流｜多模式视频生成_2094500712767115265.json, 视频生成/图生视频/MiniMax H3超级多合一工作流官方版｜全能参考生成_2094499255737208833.json, 视频生成/图生视频/双采去水印版多图参考｜MiniMax H3视频生成直出_2093427385231302657.json, 视频生成/图生视频/双采去水印版｜MiniMax H3多图参考图生视频生成_2093758899559165953.json, 视频生成/图生视频/超级多合一官方版｜YZ金鱼 MiniMax H3图生图生视频_2094723951757971458.json, 视频生成/文生视频/傲雪AIGC短剧双采｜MiniMax H3文生图生视频工作流_2093212268778582018.json, 视频生成/文生视频/多参2采8步加速｜MiniMax H3文生图生视频生成_2091601751957925889.json, 视频生成/文生视频/多参二采8步加速｜MiniMax H3视频生成提速_2091773543188090881.json, 视频生成/文生视频/超级多合一官方版V2文生图生视频｜MiniMax H3视频生成工作流_2088317993481760769.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/4步加速Lora二采高清放大｜H3全能参考图生视频画质增强_2088721636932538369.json、视频生成/图生视频/4步加速Lora｜H3全能参考二采高清放大图生视频_2089065029676134402.json、视频生成/图生视频/4步加速官方Skills提示词模板多参｜MINIMAX-H3图生视频工作流_2087201189288038401.json、视频生成/图生视频/720P MiniMax H3超级多合一官方版｜图生视频工作流_2094857234391064577.json、视频生成/图生视频/H3 Model High-Speed  美女模特图生视频直出 H3模型高速生成视频_2094945625723985922.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
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
- `GetNode` —— 19/20 个有
- `ImageResizeKJv2` —— 19/20 个有
- `SetNode` —— 19/20 个有
- `VAEEncode` —— 19/20 个有
- `孤海注释` —— 19/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/20 个有
- `VAEEncodeAudio` —— 17/20 个有
- `Fast Groups Bypasser (rgthree)` —— 16/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/20 个有
- `LoadAudio` —— 16/20 个有
- `PreviewImage` —— 16/20 个有
- `Text` —— 16/20 个有
- `VAEDecodeAudio` —— 16/20 个有
- `VHS_LoadVideo` —— 16/20 个有
- `easy cleanGpuUsed` —— 14/20 个有
- `ModelAttentionBackend` —— 12/20 个有
- `LTXVConcatAVLatent` —— 11/20 个有
- `PT_H3ConcatAVLatent` —— 8/20 个有
- `MiniMaxH3ImageToVideo` —— 7/20 个有
- `MiniMaxH3AVDecodeT8` —— 4/20 个有
- `PathchSageAttentionKJ` —— 4/20 个有
- `CR Prompt Text` —— 3/20 个有
- `LoraLoaderBypassModelOnly` —— 3/20 个有
- `RunningHub Deepcleaner` —— 2/20 个有
- `SaveImage` —— 2/20 个有
- `SaveVideo` —— 2/20 个有
- `CR Text` —— 1/20 个有
- `EmptyImage` —— 1/20 个有
- `FastGroupsBypassSwitch` —— 1/20 个有
- `PlaySound|pysssss` —— 1/20 个有
- `PrimitiveStringMultiline` —— 1/20 个有
- `RH_LLMAPI_Pro_Node` —— 1/20 个有
- `StringFunction|pysssss` —— 1/20 个有
- `easy clearCacheAll` —— 1/20 个有
- `easy promptConcat` —— 1/20 个有
- `easy showAnything` —— 1/20 个有

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
| Steps较低可能导致细节不足 | 21/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（21/20 个样本）：Steps较低可能导致细节不足
