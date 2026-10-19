---
name: text_to_image_lora_sampler_clip_41
type: Text To Image
frequency: 16
level: strong
coverage: 0.895625
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json, 视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json, 视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099191168692219906.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099573312807591938.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099189481143365633.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099571650248400898.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099192888298139649.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099574994182434818.json, 视频生成/文生视频/MiniMax H3 SelfLift双采4步Lora6步均衡版视频处理工具_2102182079902609410.json, 视频生成/文生视频/MiniMax H3 SelfLift双采8步Lora12步质量版视频处理工具_2102183788070662146.json, 视频生成/文生视频/MiniMax H3 SelfLift版本｜768P通用生视频轻量出片｜文生视频_2099096873352126465.json, 视频生成/文生视频/MiniMax H3 SelfLift精修｜4K超清通用视频生成不糊帧｜文图双输入_2099102127078600705.json, 视频生成/文生视频/MiniMax H3 SelfLift通用生视频 768P多模态创作_2098829148855816193.json, 视频生成/文生视频/Minimax H3 self-lift双采 BF16加sage四步加速lora高质量高速_2098296538933059585.json, 视频生成/文生视频/低显存12GB直出1080P高分辨率视频，BUNNY SelfLift混合工作流LoRA不模糊_2102864635153182721.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json、视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json、视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json、视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099191168692219906.json、视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099573312807591938.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 15/16 个有
- `MiniMaxH3AVDecodeT8` —— 13/16 个有
- `SaveImage` —— 13/16 个有
- `MiniMaxChunkFeedForward` —— 12/16 个有
- `MiniMaxLowVRAMAttention` —— 12/16 个有
- `SelfLiftH3Sampler` —— 12/16 个有
- `LayerUtility: PurgeVRAM V2` —— 9/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/16 个有
- `VHS_VideoCombine` —— 9/16 个有
- `CreateVideo` —— 7/16 个有
- `SaveVideo` —— 7/16 个有
- `LoadAudio` —— 6/16 个有
- `LoraLoaderBypassModelOnly` —— 4/16 个有
- `SelfLiftAvatarH3Sampler` —— 4/16 个有
- `SelfLiftAvatarH3TST` —— 4/16 个有
- `SolAttnMiniMax` —— 4/16 个有
- `ModelAttentionBackend` —— 3/16 个有
- `ModelPreviewOverrideKJ` —— 3/16 个有
- `RH_DLSS5FrameInterpolation` —— 3/16 个有
- `VAEDecodeAudio` —— 3/16 个有
- `EmptyImage` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `Int` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `SeedVR2` —— 1/16 个有
- `SeedVR2BlockSwap` —— 1/16 个有

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
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
