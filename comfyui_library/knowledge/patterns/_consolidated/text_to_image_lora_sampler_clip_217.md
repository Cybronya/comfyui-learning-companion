---
name: text_to_image_lora_sampler_clip_217
type: Text To Image
frequency: 9
level: strong
coverage: 0.927778
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3 OpenVDN DMD8参考生视频 文生视频多模态处理_2099201183129886721.json, 视频生成/文生视频/H3 OpenVDN DMD8参考生视频 文生视频多模态处理_2099583443020636161.json, 视频生成/文生视频/H3 OpenVDN DMD8通用生视频768P多模态创作_2099554412699152386.json, 视频生成/文生视频/MINIMAX H3多参生视频工作流，文生视频图生视频处理方案_2108343271964635137.json, 视频生成/文生视频/MiniMax H3 Larry 8步参考生视频 文生图生视频多模态处理_2098733935315480577.json, 视频生成/文生视频/MiniMax H3 OpenVDN DMD8参考生视频 文生图生视频多模态_2098646912223244290.json, 视频生成/文生视频/MiniMax H3 OpenVDN DMD8参考生视频｜参考图喂进去，视频稳稳出_2099521321498669058.json, 视频生成/文生视频/MiniMax H3 OpenVDN DMD8方案｜2K画质通用视频生成｜三模输入_2099099444166873089.json, 视频生成/文生视频/MiniMax H3 OpenVDN DMD8通用生视频 2K高清输出_2098830839260999681.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_217

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/H3 OpenVDN DMD8参考生视频 文生视频多模态处理_2099201183129886721.json、视频生成/文生视频/H3 OpenVDN DMD8参考生视频 文生视频多模态处理_2099583443020636161.json、视频生成/文生视频/H3 OpenVDN DMD8通用生视频768P多模态创作_2099554412699152386.json、视频生成/文生视频/MINIMAX H3多参生视频工作流，文生视频图生视频处理方案_2108343271964635137.json、视频生成/文生视频/MiniMax H3 Larry 8步参考生视频 文生图生视频多模态处理_2098733935315480577.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 8/9 个有
- `MiniMaxH3AVDecodeT8` —— 7/9 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 7/9 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 7/9 个有
- `SaveImage` —— 7/9 个有
- `RH_DLSS5FrameInterpolation` —— 3/9 个有
- `BasicScheduler` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `Int` —— 2/9 个有
- `SeedVR2` —— 2/9 个有
- `SeedVR2BlockSwap` —— 2/9 个有
- `VAEDecodeAudio` —— 2/9 个有
- `KSamplerSelect` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `MiniMaxH3ReferenceToVideo` —— 1/9 个有
- `MiniMaxH3TurboLoRA` —— 1/9 个有
- `MiniMaxH3TurboSampler` —— 1/9 个有
- `ResolutionSelector` —— 1/9 个有
- `easy float` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
