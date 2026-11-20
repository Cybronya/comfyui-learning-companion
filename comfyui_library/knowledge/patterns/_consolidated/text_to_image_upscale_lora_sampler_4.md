---
name: text_to_image_upscale_lora_sampler_4
type: Text To Image
frequency: 19
level: strong
coverage: 0.883684
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3DirectorRefine, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3导演台ref2va，全能参考图生视频方案_2111237770525106178.json, 视频生成/图生视频/MiniMax H3导演台人物去油，图生视频全能方案_2111289077042601985.json, 视频生成/图生视频/fl2v图生视频｜MiniMax H3导演台全能工作流_2092914595471126529.json, 视频生成/图生视频/fl2v导演台全能｜MiniMax H3人物类特效图生视频_2092576351906787329.json, 视频生成/图生视频/fl2v导演台全能｜MiniMax H3图生视频生成_2091763159051890689.json, 视频生成/图生视频/fl2v导演台全能｜MiniMax H3图生视频生成_2092064759645564929.json, 视频生成/图生视频/ref2va全能参考｜MiniMax H3导演台全能工作流_2092704060947386370.json, 视频生成/图生视频/ref2va全能参考｜MiniMax H3导演台图生视频生视频_2092892930460708865.json, 视频生成/图生视频/ref2va全能参考｜MiniMax H3导演台工作流_2091198014990934017.json, 视频生成/图生视频/导演台ref2va工作流｜MiniMax H3图生视频直出_2091667555638398977.json, 视频生成/图生视频/导演台全能工作流fl2v｜MiniMax H3图生视频直出_2091592035697516546.json, 视频生成/图生视频/导演台全能工作流｜MiniMax H3 ref2va全能参考_2090897981406015489.json, 视频生成/图生视频/无水印导演台全能流｜MiniMax H3开源角色设计图生视频_2092719967396524033.json, 视频生成/图生视频/无水印版开源导演台｜MiniMax H3场景特效图生视频_2092919674605498369.json, 视频生成/文生视频/H3图生视频高清版 无水印高清视频生成工具_2099215533198635010.json, 视频生成/文生视频/H3图生视频高清版 无水印高清视频生成工具_2099595930357035010.json, 视频生成/文生视频/H3漫剧导演台 文生视频图生视频创作工具_2100317759417708546.json, 视频生成/文生视频/MiniMax H3 导演台满血版｜Ref2va全能工作流文生图生视频_2097524361732386817.json, 视频生成/文生视频/MiniMax H3导演台全能工作流｜文生视频多模式生成_2097523465933905921.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3导演台ref2va，全能参考图生视频方案_2111237770525106178.json、视频生成/图生视频/MiniMax H3导演台人物去油，图生视频全能方案_2111289077042601985.json、视频生成/图生视频/fl2v图生视频｜MiniMax H3导演台全能工作流_2092914595471126529.json、视频生成/图生视频/fl2v导演台全能｜MiniMax H3人物类特效图生视频_2092576351906787329.json、视频生成/图生视频/fl2v导演台全能｜MiniMax H3图生视频生成_2091763159051890689.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3DirectorRefine`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/19 个有
- `VHS_VideoCombine` —— 18/19 个有
- `MiniMaxH3Director` —— 17/19 个有
- `PreviewAny` —— 15/19 个有
- `SaveImage` —— 6/19 个有
- `CreateVideo` —— 3/19 个有
- `BasicScheduler` —— 2/19 个有
- `CR Load LoRA` —— 2/19 个有
- `ComfyMiniMaxH3Director` —— 2/19 个有
- `CustomCombo` —— 2/19 个有
- `SaveVideo` —— 2/19 个有
- `StringToNumber` —— 2/19 个有
- `TextSwitchCase` —— 2/19 个有
- `BasicGuider` —— 1/19 个有
- `KSamplerSelect` —— 1/19 个有
- `LTXVConcatAVLatent` —— 1/19 个有
- `LTXVSeparateAVLatent` —— 1/19 个有
- `ManualSigmas` —— 1/19 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/19 个有
- `PathchSageAttentionKJ` —— 1/19 个有
- `SamplerCustomAdvanced` —— 1/19 个有
- `VAEEncode` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（20/19 个样本）：Steps较低可能导致细节不足
