---
name: text_to_image_video_lora_sampler_30
type: Text To Image
frequency: 21
level: strong
coverage: 0.600048
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4步加速Lora二采高清放大｜H3全能参考图生视频画质增强_2088721636932538369.json, 视频生成/图生视频/4步加速Lora｜H3全能参考二采高清放大图生视频_2089065029676134402.json, 视频生成/图生视频/4步加速官方Skills提示词模板多参｜MINIMAX-H3图生视频工作流_2087201189288038401.json, 视频生成/图生视频/720P MiniMax H3超级多合一官方版｜图生视频工作流_2094857234391064577.json, 视频生成/图生视频/9图参考一次出片｜MiniMax H3图生视频多图玩法_2089030736761409538.json, 视频生成/图生视频/H3 Model High-Speed  美女模特图生视频直出 H3模型高速生成视频_2094945625723985922.json, 视频生成/图生视频/H3全能参考二采放大 图生视频高质量输出_2098282282468601858.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2090298920558747649.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2091428235719565313.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2114652634794782721.json, 视频生成/图生视频/H3模型图生视频直出 高速一键出片人像写真处理工具_2113320234600984577.json, 视频生成/图生视频/H3模型图生视频直出利器｜高速一键出片｜角色一致性保持_2113091227037032450.json, 视频生成/图生视频/H3超级多合一工作流官方版 全功能视频生成_2100278481891450882.json, 视频生成/图生视频/Lightx2v+8步加速官模｜双模型双采样单图自动反推提词_2089395917622439937.json, 视频生成/图生视频/MINIMAX-H3全能参考去油防脸崩-视频生视频图生视频_2087370270070886402.json, 视频生成/图生视频/MiniMax H3超级多合一官方版工作流｜多模式视频生成_2094500712767115265.json, 视频生成/图生视频/MiniMax H3超级多合一工作流官方版｜全能参考生成_2094499255737208833.json, 视频生成/图生视频/全能参考去油防MINIMAX-H3脸崩工作流ENG_2087124608590901249.json, 视频生成/图生视频/双采去水印版多图参考｜MiniMax H3视频生成直出_2093427385231302657.json, 视频生成/图生视频/双采去水印版｜MiniMax H3多图参考图生视频生成_2093758899559165953.json, 视频生成/图生视频/多参考API用｜MiniMax H3工作流图生视频生成_2089482490334498817.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/4步加速Lora二采高清放大｜H3全能参考图生视频画质增强_2088721636932538369.json、视频生成/图生视频/4步加速Lora｜H3全能参考二采高清放大图生视频_2089065029676134402.json、视频生成/图生视频/4步加速官方Skills提示词模板多参｜MINIMAX-H3图生视频工作流_2087201189288038401.json、视频生成/图生视频/720P MiniMax H3超级多合一官方版｜图生视频工作流_2094857234391064577.json、视频生成/图生视频/9图参考一次出片｜MiniMax H3图生视频多图玩法_2089030736761409538.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 21 个 workflow 都包含：
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
- `GetNode` —— 20/21 个有
- `SetNode` —— 20/21 个有
- `孤海注释` —— 20/21 个有
- `ImageResizeKJv2` —— 19/21 个有
- `VAEEncode` —— 19/21 个有
- `Text` —— 17/21 个有
- `VAEDecodeAudio` —— 17/21 个有
- `VAEEncodeAudio` —— 17/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/21 个有
- `PreviewImage` —— 16/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/21 个有
- `Fast Groups Bypasser (rgthree)` —— 13/21 个有
- `LoadAudio` —— 13/21 个有
- `VHS_LoadVideo` —— 13/21 个有
- `easy cleanGpuUsed` —— 13/21 个有
- `PT_H3ConcatAVLatent` —— 12/21 个有
- `ModelAttentionBackend` —— 8/21 个有
- `PathchSageAttentionKJ` —— 8/21 个有
- `LTXVConcatAVLatent` —— 7/21 个有
- `MiniMaxH3ImageToVideo` —— 5/21 个有
- `MiniMaxH3AVDecodeT8` —— 4/21 个有
- `CR Prompt Text` —— 3/21 个有
- `LoraLoaderBypassModelOnly` —— 3/21 个有
- `RunningHub Deepcleaner` —— 3/21 个有
- `SaveImage` —— 3/21 个有
- `SaveVideo` —— 2/21 个有
- `CR Text` —— 1/21 个有
- `CRTFirstLastFrameSelector` —— 1/21 个有
- `EmptyImage` —— 1/21 个有
- `FastGroupsBypassSwitch` —— 1/21 个有
- `PrimitiveStringMultiline` —— 1/21 个有
- `RH_LLMAPI_Pro_Node` —— 1/21 个有
- `StringFunction|pysssss` —— 1/21 个有
- `easy clearCacheAll` —— 1/21 个有
- `easy promptConcat` —— 1/21 个有
- `easy showAnything` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（23/21 个样本）：Steps较低可能导致细节不足
