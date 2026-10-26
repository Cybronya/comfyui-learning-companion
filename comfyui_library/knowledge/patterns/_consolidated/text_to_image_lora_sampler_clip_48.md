---
name: text_to_image_lora_sampler_clip_48
type: Text To Image
frequency: 17
level: strong
coverage: 0.638353
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json, 图片生成/反推提示词/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json, 图片生成/文生图/Minimaxh3视频复刻伪原创，selflift版反推洗图_2110833772068425729.json, 视频生成/图生视频/H3 SelfLift完整逻辑判断版 全能视频生成处理工具_2113726712482717697.json, 视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099213820353933314.json, 视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099567116251910145.json, 视频生成/图生视频/MiniMax H3终极篇 视频参考音频参考图生视频处理工具_2113053661508231169.json, 视频生成/图生视频/MiniMax H3终极篇一 单图参考图生视频处理工具_2113342774278971394.json, 视频生成/图生视频/MiniMax H3终极篇三 多图参考图生视频处理工具_2113420381666238466.json, 视频生成/图生视频/MiniMax H3终极篇二 双图参考图生视频处理工具_2113344348384485377.json, 视频生成/图生视频/MiniMax H3终极篇文武双全 二采1080P直出处理工具_2113825893926920193.json, 视频生成/图生视频/MiniMax H3终极篇文武双全工作流，文生视频武戏动态两相宜高清直出_2114431782882992130.json, 视频生成/图生视频/MiniMax H3终极篇文武双全版 高质量图生视频工具_2113756923609833473.json, 视频生成/图生视频/MiniMax H3终极篇文武双全版｜文戏武戏图生视频全掌握_2113573804252422146.json, 视频生成/图生视频/Minimax H3 Ref2V最佳动作 文生视频图生视频处理工具_2113335034068422657.json, 视频生成/文生视频/MiniMax H3终极篇文生视频 文本转视频处理工具_2114116327693701122.json, 视频生成/文生视频/短剧助手加速双采 self-lift模式高效视频生成_2098298081249947650.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/反推提示词/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json、图片生成/反推提示词/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json、图片生成/文生图/Minimaxh3视频复刻伪原创，selflift版反推洗图_2110833772068425729.json、视频生成/图生视频/H3 SelfLift完整逻辑判断版 全能视频生成处理工具_2113726712482717697.json、视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099213820353933314.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SelfLiftH3Sampler` —— 16/17 个有
- `GetNode` —— 15/17 个有
- `MiniMaxChunkFeedForward` —— 15/17 个有
- `SaveImage` —— 15/17 个有
- `SetNode` —— 15/17 个有
- `LoadImage` —— 14/17 个有
- `VHS_VideoCombine` —— 13/17 个有
- `BlockSparseAttention` —— 11/17 个有
- `MiniMaxH3SigmaShift` —— 11/17 个有
- `Text` —— 10/17 个有
- `VHS_LoadVideo` —— 10/17 个有
- `GoohaiUniversalSlider` —— 9/17 个有
- `LoadAudio` —— 8/17 个有
- `H3SigmaRefiner` —— 7/17 个有
- `PrimitiveStringMultiline` —— 7/17 个有
- `MiniMaxLowVRAMAttention` —— 6/17 个有
- `CreateVideo` —— 5/17 个有
- `LoadAudioFromUrl` —— 4/17 个有
- `SaveVideo` —— 4/17 个有
- `Anything Everywhere3` —— 3/17 个有
- `ComfySwitchNode` —— 3/17 个有
- `MiniMaxH3MediaLoaderFantastic` —— 3/17 个有
- `MiniMaxH3ReferenceSplitter` —— 3/17 个有
- `Prompts Everywhere` —— 3/17 个有
- `YK_LoadImageFromURL` —— 3/17 个有
- `PathchSageAttentionKJ` —— 2/17 个有
- `PlaySound|pysssss` —— 1/17 个有
- `QwenH3PromptLocal` —— 1/17 个有
- `SelfLiftAvatarH3Sampler` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
