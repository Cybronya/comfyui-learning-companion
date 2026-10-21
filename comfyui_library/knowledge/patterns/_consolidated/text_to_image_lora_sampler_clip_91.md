---
name: text_to_image_lora_sampler_clip_91
type: Text To Image
frequency: 11
level: strong
coverage: 0.887818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json, 视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json, 视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json, 视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json, 视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json, 视频生成/图生视频/MinimaxH3 Easy动作迁移人物替换｜1080高画质服装替换全注释_2089453564925136898.json, 视频生成/图生视频/MinimaxH3 Easy角色服装替换动作迁移｜1080高画质全节点注释视频生视频_2089719236200583170.json, 视频生成/图生视频/漫剧林辰图生视频｜短剧角色动起来 图生视频一键成片_2104102680842039298.json, 视频生成/图生视频/漫剧林辰角色动态演绎 图生视频一键生成流畅画面_2104279422512754690.json, 视频生成/图生视频/电影感多参迅捷｜minimax H3防拉丝图生视频工作流_2093110076662968321.json, 视频生成/图生视频/短剧漫剧参考图生视频工作流，图生视频短剧制作方案_2103604319982542850.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json、视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json、视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json、视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json、视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `CR Text` —— 8/11 个有
- `MiniMaxH3Easy` —— 8/11 个有
- `MiniMaxH3EasyLoader` —— 8/11 个有
- `MiniMaxH3EasyOutput` —— 8/11 个有
- `LoadImage` —— 7/11 个有
- `LoadVideo` —— 6/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `CreateVideo` —— 5/11 个有
- `SaveVideo` —— 5/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `ComfyMathExpression` —— 3/11 个有
- `MiniMaxH3ReferenceToVideo` —— 3/11 个有
- `PrimitiveFloat` —— 3/11 个有
- `ResolutionSelector` —— 3/11 个有
- `SaveImage` —— 3/11 个有
- `BiRefNetRMBG` —— 2/11 个有
- `LoadAudio` —— 2/11 个有
- `MiniMaxH3SigmaShift` —— 2/11 个有
- `DuckHideNode` —— 1/11 个有
- `H3SigmaRefiner` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `MiniMaxH3EasyModelAdapter` —— 1/11 个有
- `MiniMaxH3TurboLoRA` —— 1/11 个有
- `MiniMaxH3TurboSampler` —— 1/11 个有
- `PlaySound|pysssss` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
