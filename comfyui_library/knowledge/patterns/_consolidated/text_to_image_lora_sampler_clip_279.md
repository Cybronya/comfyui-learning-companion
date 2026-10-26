---
name: text_to_image_lora_sampler_clip_279
type: Text To Image
frequency: 8
level: strong
coverage: 0.872
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minmax生图工作流｜多人姿势迁移视频制作_2097811139928354818.json, 视频生成/文生视频/上下文文生视频扩写2K｜MiniMax H3一句话生成工作流_2096737308723728385.json, 视频生成/文生视频/上下文竖屏极速文生｜MiniMax H3一句话短视频生成_2096738714239197185.json, 视频生成/文生视频/低价批量视频生成｜文生图生视频生视频模型直出_2093139939205668866.json, 视频生成/文生视频/全能参考生真人视频｜Seedance2.0 文生视频图生视频一站搞定_2105499577867653122.json, 视频生成/文生视频/全能参考生真人视频｜Seedance2.0文生视频生视频_2095870248128958465.json, 视频生成/文生视频/宽审多图多视频参考｜pipi-Seedance2.0-global生成_2095579714701316098.json, 视频生成/文生视频/电商友好型Seedance2.0多参视频生成｜平价好用_2095291656303104002.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_279

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/minmax生图工作流｜多人姿势迁移视频制作_2097811139928354818.json、视频生成/文生视频/上下文文生视频扩写2K｜MiniMax H3一句话生成工作流_2096737308723728385.json、视频生成/文生视频/上下文竖屏极速文生｜MiniMax H3一句话短视频生成_2096738714239197185.json、视频生成/文生视频/低价批量视频生成｜文生图生视频生视频模型直出_2093139939205668866.json、视频生成/文生视频/全能参考生真人视频｜Seedance2.0 文生视频图生视频一站搞定_2105499577867653122.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/8 个有
- `LoadVideo` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `RH_MinimaxHailuoH3ContextIrText` —— 2/8 个有
- `RH_MinimaxHailuoH3TextToVideo` —— 2/8 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 2/8 个有
- `RH_BytedanceSeedance20GlobalMultimodalVideo` —— 1/8 个有
- `RH_BytedanceSeedance25TokenTextToVideo` —— 1/8 个有
- `RelayGrokImagineVideo` —— 1/8 个有
- `Seedance_Config` —— 1/8 个有
- `Seedance_MultimodalVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
