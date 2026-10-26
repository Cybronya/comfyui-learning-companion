---
name: text_to_image_video_lora_sampler_59
type: Text To Image
frequency: 13
level: strong
coverage: 0.665538
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, FeiHouEasyH3RH, FeiHouEasyH3RHLoader, FeiHouEasyH3RHOutput, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LoraLoaderModelOnly, ModelAttentionBackend, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3无限画布式生成｜极致简化图生视频工作流_2096340210660495361.json, 视频生成/图生视频/H3极简画布模式多参工作流 轻量化多模态创作_2100276875628208129.json, 视频生成/图生视频/Remix双采样多参｜MiniMax H3图生视频生成_2092618564485337090.json, 视频生成/图生视频/Remix双采样多参｜MiniMax H3图生视频直出_2092361288776241153.json, 视频生成/图生视频/极简自动提示词流｜MiniMax H3全功能图生视频修复版_2090219462069932033.json, 视频生成/文生视频/H3全能参考漫剧工作流 文生视频图生视频创作_2099947593500549121.json, 视频生成/文生视频/H3全能参考漫剧工作流_文生视频图生视频创作_2100426387504066562.json, 视频生成/文生视频/H3极简画布模式多参工作流 轻量化多模态创作_2099954372460503041.json, 视频生成/文生视频/H3极简画布模式多参工作流_轻量化多模态创作_2100508539260325889.json, 视频生成/文生视频/MiniMax H3 Remix无限画布极简版｜提示词反推双采样_2094914309708140546.json, 视频生成/文生视频/MiniMax H3画布满血多参工作流｜极简文生视频视频生视频_2094846962746085377.json, 视频生成/文生视频/Remix无限画布极简操作｜MiniMax H3双采样反推提示词_2093118371503099906.json, 视频生成/文生视频/无限画布式操作｜MiniMax H3 Remix极致简化双采样_2095121034084175873.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_59

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/H3无限画布式生成｜极致简化图生视频工作流_2096340210660495361.json、视频生成/图生视频/H3极简画布模式多参工作流 轻量化多模态创作_2100276875628208129.json、视频生成/图生视频/Remix双采样多参｜MiniMax H3图生视频生成_2092618564485337090.json、视频生成/图生视频/Remix双采样多参｜MiniMax H3图生视频直出_2092361288776241153.json、视频生成/图生视频/极简自动提示词流｜MiniMax H3全功能图生视频修复版_2090219462069932033.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FeiHouEasyH3RH`
- `FeiHouEasyH3RHLoader`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `FeiHouEasyH3RHLoraStack` —— 12/13 个有
- `RandomSeedNoise` —— 12/13 个有
- `孤海注释` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `ImageResizeKJv2` —— 8/13 个有
- `ResolutionSelector` —— 8/13 个有
- `VAEEncode` —— 8/13 个有
- `VAEEncodeAudio` —— 8/13 个有
- `FeiHouEasyH3RHPromptPreview` —— 7/13 个有
- `LoraLoaderBypassModelOnly` —— 7/13 个有
- `SaveImage` —— 7/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/13 个有
- `ModelPreviewOverrideKJ` —— 6/13 个有
- `easy cleanGpuUsed` —— 6/13 个有
- `H3SigmaRefiner` —— 5/13 个有
- `LTXVSeparateAVLatent` —— 5/13 个有
- `MinimaxH3LatentUpscaler3D` —— 5/13 个有
- `easy float` —— 5/13 个有
- `CM_FloatToInt` —— 2/13 个有
- `ComfySwitchNodeV2` —— 2/13 个有
- `DuckHideNode` —— 2/13 个有
- `EmptyImage` —— 2/13 个有
- `FeiHouEasyH3RHDurationCrop` —— 2/13 个有
- `MiniMaxH3SigmaShift` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `RandomNoise` —— 2/13 个有
- `Int` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

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
