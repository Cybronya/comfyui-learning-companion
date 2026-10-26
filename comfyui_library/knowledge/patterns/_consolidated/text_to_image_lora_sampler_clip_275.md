---
name: text_to_image_lora_sampler_clip_275
type: Text To Image
frequency: 8
level: strong
coverage: 0.886
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json, 视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json, 视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json, 视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json, 视频生成/文生视频/MiniMax H3 SelfLift版本｜768P通用生视频轻量出片｜文生视频_2099096873352126465.json, 视频生成/文生视频/MiniMax H3 SelfLift精修｜4K超清通用视频生成不糊帧｜文图双输入_2099102127078600705.json, 视频生成/文生视频/MiniMax H3 SelfLift通用生视频 768P多模态创作_2098829148855816193.json, 视频生成/文生视频/低显存12GB直出1080P高分辨率视频，BUNNY SelfLift混合工作流LoRA不模糊_2102864635153182721.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_275

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json、视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json、视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json、视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json、视频生成/文生视频/MiniMax H3 SelfLift版本｜768P通用生视频轻量出片｜文生视频_2099096873352126465.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `SaveImage` —— 5/8 个有
- `LoraLoaderBypassModelOnly` —— 4/8 个有
- `MiniMaxH3AVDecodeT8` —— 4/8 个有
- `ModelAttentionBackend` —— 4/8 个有
- `SelfLiftAvatarH3Sampler` —— 4/8 个有
- `SelfLiftAvatarH3TST` —— 4/8 个有
- `SelfLiftH3Sampler` —— 4/8 个有
- `SolAttnMiniMax` —— 4/8 个有
- `VAEDecodeAudio` —— 4/8 个有
- `MiniMaxChunkFeedForward` —— 3/8 个有
- `MiniMaxLowVRAMAttention` —— 3/8 个有
- `ModelPreviewOverrideKJ` —— 3/8 个有
- `RH_DLSS5FrameInterpolation` —— 3/8 个有
- `EmptyImage` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `Int` —— 1/8 个有
- `LTXVSeparateAVLatent` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `LoraLoader` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `SeedVR2BlockSwap` —— 1/8 个有

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
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

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
