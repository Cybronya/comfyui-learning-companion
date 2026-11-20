---
name: text_to_image_video_lora_sampler_80
type: Text To Image
frequency: 10
level: strong
coverage: 0.8529
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速版双时钟版官流原版合集｜MinimaxH3视频参考生成视频生视频_2088138270730444801.json, 视频生成/图生视频/换装加动作迁移视频编辑｜MiniMaxH3全节点注释视频生视频_2088735225936441345.json, 视频生成/图生视频/视频换背景提示词编辑｜MiniMaxH3视频生视频场景一键替换_2090468441949036546.json, 视频生成/图生视频/视频换背景支持参考图｜MiniMaxH3视频编辑实战_2101143111773802497.json, 视频生成/图生视频/视频换背景编辑｜MiniMaxH3人物特效动作迁移处理_2094593810511781890.json, 视频生成/图生视频/视频换背景随意换｜MiniMaxH3 视频编辑动作迁移_2096263348093542402.json, 视频生成/图生视频/视频编辑MiniMax H3视频换背景工作流，人物类特效视频运镜图生视频方案_2108448538760933377.json, 视频生成/图生视频/视频编辑换装动作迁移｜MiniMaxH3全节点注释版_2090911739268390914.json, 视频生成/文生视频/MiniMaxH3视频编辑｜文生视频换背景轻松搞定_2101170318881677313.json, 视频生成/视频生视频/MiniMax H3视频换背景视频编辑工作流_人物特效视频生视频处理工具_2106155529885282305.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/加速版双时钟版官流原版合集｜MinimaxH3视频参考生成视频生视频_2088138270730444801.json、视频生成/图生视频/换装加动作迁移视频编辑｜MiniMaxH3全节点注释视频生视频_2088735225936441345.json、视频生成/图生视频/视频换背景提示词编辑｜MiniMaxH3视频生视频场景一键替换_2090468441949036546.json、视频生成/图生视频/视频换背景支持参考图｜MiniMaxH3视频编辑实战_2101143111773802497.json、视频生成/图生视频/视频换背景编辑｜MiniMaxH3人物特效动作迁移处理_2094593810511781890.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/10 个有
- `VRAM_Debug` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `GetNode` —— 7/10 个有
- `ImageConcanate` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `LoadImage` —— 4/10 个有
- `CR Text` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `EasyCache` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `GetCurrentTimeNode` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `LazySwitch1way` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `PurgeVRAM_UTK` —— 1/10 个有
- `SomethingToString` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
