---
name: text_to_image_lora_sampler_clip_161
type: Text To Image
frequency: 6
level: strong
coverage: 0.891667
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax导演台 长视频多段编排视频生成_2104689816385445890.json, 视频生成/图生视频/minimax导演台图生视频｜分镜掌控感拉满的导演级工具_2104576913363791874.json, 视频生成/图生视频/minimax导演台长视频多段编排 视频生成工作流_2104976866355531778.json, 视频生成/文生视频/MiniMax导演台全能工作流 文生视频图生视频多模态_2098829057545822210.json, 视频生成/文生视频/MiniMax导演台全能版｜文生视频图生视频视频生视频全打通｜一站式创作_2099109263422607361.json, 视频生成/文生视频/minimax h3导演全能工作台｜文生视频文生图图生图_2100801737908117505.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/minimax导演台 长视频多段编排视频生成_2104689816385445890.json、视频生成/图生视频/minimax导演台图生视频｜分镜掌控感拉满的导演级工具_2104576913363791874.json、视频生成/图生视频/minimax导演台长视频多段编排 视频生成工作流_2104976866355531778.json、视频生成/文生视频/MiniMax导演台全能工作流 文生视频图生视频多模态_2098829057545822210.json、视频生成/文生视频/MiniMax导演台全能版｜文生视频图生视频视频生视频全打通｜一站式创作_2099109263422607361.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 3/6 个有
- `ImageFromBatch` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `SeedVR2LoadDiTModel` —— 3/6 个有
- `SeedVR2LoadVAEModel` —— 3/6 个有
- `SeedVR2VideoUpscaler` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `easy showAnything` —— 3/6 个有

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
