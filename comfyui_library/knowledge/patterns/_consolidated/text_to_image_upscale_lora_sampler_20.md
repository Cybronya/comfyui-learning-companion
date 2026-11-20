---
name: text_to_image_upscale_lora_sampler_20
type: Text To Image
frequency: 10
level: strong
coverage: 0.8914
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, SaveVideo, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMaxH3 AIO造梦工厂｜图生视频文生视频视频生视频一站搞定_2097879124835659777.json, 视频生成/文生视频/fl2v导演台全能｜MiniMax H3文生视频生成_2092560452915126274.json, 视频生成/文生视频/一次60秒全能生成｜海螺H3搅拌手大佬版导演台_2092749641665306626.json, 视频生成/文生视频/一次60秒出片｜海螺 H3 导演台搅拌手大佬版_2090893932635967490.json, 视频生成/文生视频/全能导演台驾到｜MiniMax H3运镜二采分镜加速_2096592640203649025.json, 视频生成/文生视频/全能导演工作台｜minimax视频生成一站式_2091202175820193794.json, 视频生成/文生视频/导演台+二采｜minimax_h3_director文生图生视频直出_2090211119091769345.json, 视频生成/文生视频/导演台一次60秒｜海螺H3搅拌手大佬版全能s_2091190910787874818.json, 视频生成/文生视频/搅拌手大佬版导演台｜海螺H3全能60秒生成_2091195180161519618.json, 视频生成/文生视频/电影级运镜导演台｜MiniMax H3二采精修分镜合成加速_2096303944883597313.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMaxH3 AIO造梦工厂｜图生视频文生视频视频生视频一站搞定_2097879124835659777.json、视频生成/文生视频/fl2v导演台全能｜MiniMax H3文生视频生成_2092560452915126274.json、视频生成/文生视频/一次60秒全能生成｜海螺H3搅拌手大佬版导演台_2092749641665306626.json、视频生成/文生视频/一次60秒出片｜海螺 H3 导演台搅拌手大佬版_2090893932635967490.json、视频生成/文生视频/全能导演台驾到｜MiniMax H3运镜二采分镜加速_2096592640203649025.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SaveVideo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 9/10 个有
- `PreviewAny` —— 9/10 个有
- `BasicScheduler` —— 6/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `FastGroupsBypassSwitch` —— 4/10 个有
- `LoraLoaderBypassModelOnly` —— 4/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `PixaromaLoraLoader` —— 1/10 个有
- `RIFE VFI` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
