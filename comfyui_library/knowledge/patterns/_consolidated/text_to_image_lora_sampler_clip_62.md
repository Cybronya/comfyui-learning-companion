---
name: text_to_image_lora_sampler_clip_62
type: Text To Image
frequency: 13
level: strong
coverage: 0.892769
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/宗门神曲多人替换演示导演台加速版全能工作流MiniMax_2087431272393166850.json, 视频生成/图生视频/导演台1分钟直出｜MiniMax H3 8步lora+sage加速图生视频_2089779895378472961.json, 视频生成/图生视频/导演台AIMixer｜MiniMax H3 4step加速图生视频_2090886550669324290.json, 视频生成/图生视频/导演台全能工作流｜Dasiwa-MiniMax H3图生视频_2095813511552258049.json, 视频生成/图生视频/导演台全能工作流｜MiniMax H3 图生视频进阶版_2096248407588429825.json, 视频生成/图生视频/导演台长视频生成段间引导turbo｜H3数字人图生视频工作流_2088165576559652865.json, 视频生成/图生视频/段间引导turbo加速H3导演台长视频生成图生视频工作流_2088353948892749825.json, 视频生成/图生视频/视频人物替换｜参考图换脸改衣风格迁移视频生成_2090197858346692609.json, 视频生成/文生视频/FZ-MinimaxH3视频导演台加速版｜像导演一样控片_2097202638852022273.json, 视频生成/文生视频/FZ-MinimaxH3视频导演台加速版｜文生视频图生视频生成_2097105561631412225.json, 视频生成/文生视频/H3漫剧导演台 文生视频图生视频创作工具_2100317759417708546.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流｜人物去油效果稳_2096887110086254594.json, 视频生成/文生视频/MiniMax H3导演台全能工作流｜文生视频多模式生成_2097523465933905921.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/宗门神曲多人替换演示导演台加速版全能工作流MiniMax_2087431272393166850.json、视频生成/图生视频/导演台1分钟直出｜MiniMax H3 8步lora+sage加速图生视频_2089779895378472961.json、视频生成/图生视频/导演台AIMixer｜MiniMax H3 4step加速图生视频_2090886550669324290.json、视频生成/图生视频/导演台全能工作流｜Dasiwa-MiniMax H3图生视频_2095813511552258049.json、视频生成/图生视频/导演台全能工作流｜MiniMax H3 图生视频进阶版_2096248407588429825.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/13 个有
- `PathchSageAttentionKJ` —— 9/13 个有
- `PreviewAny` —— 9/13 个有
- `SaveVideo` —— 9/13 个有
- `VHS_VideoCombine` —— 8/13 个有
- `MiniMaxH3DirectorRefine` —— 4/13 个有
- `UpscaleModelLoader` —— 4/13 个有
- `BasicGuider` —— 3/13 个有
- `SaveImage` —— 3/13 个有
- `LoraLoaderBypassModelOnly` —— 2/13 个有
- `ModelAttentionBackend` —— 2/13 个有
- `BasicScheduler` —— 1/13 个有
- `ImageConcatMulti` —— 1/13 个有
- `KSamplerSelect` —— 1/13 个有
- `LTXVConcatAVLatent` —— 1/13 个有
- `LTXVSeparateAVLatent` —— 1/13 个有
- `ManualSigmas` —— 1/13 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `SamplerCustomAdvanced` —— 1/13 个有
- `VAEEncode` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 17/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（17/13 个样本）：Steps较低可能导致细节不足
