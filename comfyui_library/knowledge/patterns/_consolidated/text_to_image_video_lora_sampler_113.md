---
name: text_to_image_video_lora_sampler_113
type: Text To Image
frequency: 6
level: strong
coverage: 0.927667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3超级加速二阶段快速文戏视频工作流 高效生成_2099913692656787457.json, 图片生成/图生图/MiniMax H3超级加速工作流｜二阶段快速文戏视频生成_2097430777486204930.json, 图片生成/图生图/二阶段快速文戏｜MiniMax H3超级加速，热门IP视频快出_2099923443507617794.json, 视频生成/图生视频/8步去油双时钟参考生视频V2｜Lightx2v正式版Minimax图生视频_2088160534666502145.json, 视频生成/图生视频/MiniMax H3视频复刻数字人｜换人换产品换文案换语音_2111128408808845313.json, 视频生成/视频生视频/MiniMax H3视频复刻视频编辑视频翻拍二创与指定角色替换长视频直出方案_2106075579454943233.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/H3超级加速二阶段快速文戏视频工作流 高效生成_2099913692656787457.json、图片生成/图生图/MiniMax H3超级加速工作流｜二阶段快速文戏视频生成_2097430777486204930.json、图片生成/图生图/二阶段快速文戏｜MiniMax H3超级加速，热门IP视频快出_2099923443507617794.json、视频生成/图生视频/8步去油双时钟参考生视频V2｜Lightx2v正式版Minimax图生视频_2088160534666502145.json、视频生成/图生视频/MiniMax H3视频复刻数字人｜换人换产品换文案换语音_2111128408808845313.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SolAttnMiniMax` —— 5/6 个有
- `CFGGuider` —— 3/6 个有
- `ConcatTextOfUtils` —— 3/6 个有
- `CreateVideo` —— 3/6 个有
- `GetVideoComponents` —— 3/6 个有
- `LTXVConditioning` —— 3/6 个有
- `LTXVLatentUpsampler` —— 3/6 个有
- `LatentUpscaleModelLoader` —— 3/6 个有
- `MiniMaxH3OutputTrimT8` —— 3/6 个有
- `MiniMaxH3SolEngineDraftToLTXT8Advanced` —— 3/6 个有
- `MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced` —— 3/6 个有
- `MiniMaxH3SolEngineTAEHVDecodeT8Advanced` —— 3/6 个有
- `MiniMaxH3SolEngineTAEHVLoaderT8Advanced` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `VAEEncode` —— 3/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `LoadVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
