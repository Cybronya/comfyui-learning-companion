---
name: text_to_image_lora_sampler_clip_44
type: Text To Image
frequency: 16
level: strong
coverage: 0.888687
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json, 视频生成/文生视频/MiniMax H3视频生成导演台｜文生视频视频生视频调度，镜头语言自己说了算_2100509465702387714.json, 视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2090530166060707841.json, 视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2094308048687951873.json, 视频生成/文生视频/Seedance 2.5图生视频处理生成工具_2102525837089263617.json, 视频生成/文生视频/Seedance 2.5文生视频处理生成工具_2102527398846754817.json, 视频生成/文生视频/Seedance2.5图生视频工作流，高质量图像到视频生成方案_2103542632843669506.json, 视频生成/文生视频/Seedance2.5图生视频工作流｜高质量图像驱动视频生成_2097761537908887554.json, 视频生成/文生视频/minimax H3导演台工作流｜文生图生视频一站式_2094560745752195073.json, 视频生成/文生视频/minmax生图工作流｜多人姿势迁移视频制作_2097811139928354818.json, 视频生成/文生视频/导演台全能工作流无水印版｜MiniMax H3三合一_2092367887234322434.json, 视频生成/文生视频/导演台工作流｜minimax H3三模视频一键生成_2094760059535450113.json, 视频生成/文生视频/导演台无限长视频玩法｜MiniMax H3文生图生视频直出_2091281323360079874.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092724076027662337.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092927901426601985.json, 视频生成/文生视频/电影级运镜导演台｜MiniMax H3二采精修分镜合成加速_2096303944883597313.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json、视频生成/文生视频/MiniMax H3视频生成导演台｜文生视频视频生视频调度，镜头语言自己说了算_2100509465702387714.json、视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2090530166060707841.json、视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2094308048687951873.json、视频生成/文生视频/Seedance 2.5图生视频处理生成工具_2102525837089263617.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 15/16 个有
- `MiniMaxH3Director` —— 9/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/16 个有
- `VHS_VideoCombine` —— 8/16 个有
- `PathchSageAttentionKJ` —— 6/16 个有
- `SaveImage` —— 6/16 个有
- `SaveVideo` —— 6/16 个有
- `LoadImage` —— 4/16 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 3/16 个有
- `MiniMaxH3DirectorRefine` —— 2/16 个有
- `ModelAttentionBackend` —— 2/16 个有
- `RH_BytedanceSeedance25TokenTextToVideo` —— 2/16 个有
- `UpscaleModelLoader` —— 2/16 个有
- `CreateVideo` —— 1/16 个有
- `PreviewAny` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
