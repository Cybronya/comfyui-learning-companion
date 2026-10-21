---
name: text_to_image_lora_sampler_clip_131
type: Text To Image
frequency: 9
level: strong
coverage: 0.862222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3 MAX智能提示词工作流｜一句话自动增强出片_2095592106181091330.json, 视频生成/文生视频/H3 MAX智能运镜工作流｜AI看图自动运镜生成_2095586803368681473.json, 视频生成/文生视频/RuningHub企业版Seedance2.0｜图生视频视频生视频一键生成_2094303698901102593.json, 视频生成/文生视频/RuningHub企业版不降智｜Seedance2.0图生视频秒出大片_2090829853393244162.json, 视频生成/文生视频/Seedance 2.5文生视频处理生成工具_2102527398846754817.json, 视频生成/文生视频/Seedance2.0 企业版图生视频 不降智不排队可传真人照_2094167174255570946.json, 视频生成/文生视频/minmax生图工作流｜多人姿势迁移视频制作_2097811139928354818.json, 视频生成/文生视频/上下文文生视频扩写2K｜MiniMax H3一句话生成工作流_2096737308723728385.json, 视频生成/文生视频/上下文竖屏极速文生｜MiniMax H3一句话短视频生成_2096738714239197185.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_131

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/H3 MAX智能提示词工作流｜一句话自动增强出片_2095592106181091330.json、视频生成/文生视频/H3 MAX智能运镜工作流｜AI看图自动运镜生成_2095586803368681473.json、视频生成/文生视频/RuningHub企业版Seedance2.0｜图生视频视频生视频一键生成_2094303698901102593.json、视频生成/文生视频/RuningHub企业版不降智｜Seedance2.0图生视频秒出大片_2090829853393244162.json、视频生成/文生视频/Seedance 2.5文生视频处理生成工具_2102527398846754817.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
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
- `LoadImage` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `RH_MinimaxHailuoH3ContextIrText` —— 3/9 个有
- `RH_RhartVideoSparkvideo20FastImageToVideo` —— 3/9 个有
- `RH_BytedanceSeedance25TokenTextToVideo` —— 2/9 个有
- `RH_MinimaxHailuoH3TextToVideo` —— 2/9 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/9 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 1/9 个有
- `RH_MinimaxHailuoH3MaxTextToVideo` —— 1/9 个有

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
