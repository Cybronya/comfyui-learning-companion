---
name: text_to_image_lora_sampler_clip_126
type: Text To Image
frequency: 9
level: strong
coverage: 0.889778
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json, 视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json, 视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json, 视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json, 视频生成/文生视频/MiniMax H3 SelfLift版本｜768P通用生视频轻量出片｜文生视频_2099096873352126465.json, 视频生成/文生视频/MiniMax H3 SelfLift精修｜4K超清通用视频生成不糊帧｜文图双输入_2099102127078600705.json, 视频生成/文生视频/MiniMax H3 SelfLift通用生视频 768P多模态创作_2098829148855816193.json, 视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json, 视频生成/文生视频/Minimax H3加速双采｜Self-Lift工作流提速出片两不误_2101510468241289218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json、视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json、视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json、视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json、视频生成/文生视频/MiniMax H3 SelfLift版本｜768P通用生视频轻量出片｜文生视频_2099096873352126465.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `MiniMaxH3AudioConditioningT8` —— 7/9 个有
- `ModelAttentionBackend` —— 6/9 个有
- `SelfLiftH3Sampler` —— 6/9 个有
- `VAEDecodeAudio` —— 6/9 个有
- `MiniMaxChunkFeedForward` —— 5/9 个有
- `MiniMaxLowVRAMAttention` —— 5/9 个有
- `ModelPreviewOverrideKJ` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `LoadAudio` —— 3/9 个有
- `LoraLoaderBypassModelOnly` —— 3/9 个有
- `MiniMaxH3AVDecodeT8` —— 3/9 个有
- `RH_DLSS5FrameInterpolation` —— 3/9 个有
- `SelfLiftAvatarH3Sampler` —— 3/9 个有
- `SelfLiftAvatarH3TST` —— 3/9 个有
- `SolAttnMiniMax` —— 3/9 个有
- `MiniMaxH3ReferenceToVideo` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `Int` —— 1/9 个有
- `LTXVSeparateAVLatent` —— 1/9 个有
- `LoraLoader` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SeedVR2` —— 1/9 个有
- `SeedVR2BlockSwap` —— 1/9 个有

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
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

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
