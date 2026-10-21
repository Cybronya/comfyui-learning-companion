---
name: text_to_image_lora_sampler_clip_182
type: Text To Image
frequency: 7
level: strong
coverage: 0.893429
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Easy, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 VDN加SelfLift采样直出1080P 图生视频工具_2099586843141562370.json, 视频生成/图生视频/MINIMAXH3双采样V3全面升级｜文戏不油武戏不糊双模式_2110702226032386049.json, 视频生成/图生视频/数字人15秒直出1080P图生视频处理生成工具_2101408406874714114.json, 视频生成/文生视频/MinimaxH3双采样V3文不油武不糊 全面升级视频生成工作流_2098694116875001857.json, 视频生成/文生视频/文戏提示词练习工作流 文生视频图生视频参数调试_2099202759265443842.json, 视频生成/文生视频/文戏提示词练习工作流 文生视频图生视频参数调试_2099584922162913282.json, 视频生成/文生视频/文戏提示词练习工作流｜文生视频图生视频两用，台词戏感慢慢磨_2099459096524181506.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3 VDN加SelfLift采样直出1080P 图生视频工具_2099586843141562370.json、视频生成/图生视频/MINIMAXH3双采样V3全面升级｜文戏不油武戏不糊双模式_2110702226032386049.json、视频生成/图生视频/数字人15秒直出1080P图生视频处理生成工具_2101408406874714114.json、视频生成/文生视频/MinimaxH3双采样V3文不油武不糊 全面升级视频生成工作流_2098694116875001857.json、视频生成/文生视频/文戏提示词练习工作流 文生视频图生视频参数调试_2099202759265443842.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyMediaLoader`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 6/7 个有
- `GetLatentSizeAndCount` —— 6/7 个有
- `ModelAttentionBackend` —— 6/7 个有
- `RandomNoise` —— 6/7 个有
- `SamplerCustomAdvanced` —— 6/7 个有
- `SelfLiftH3Sampler` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `SaveImage` —— 5/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `CreateVideo` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有
- `SaveVideo` —— 2/7 个有
- `easy imageChooser` —— 2/7 个有
- `kkVideoFirstLastFrames` —— 2/7 个有
- `LTXVAudioVAEEncode` —— 1/7 个有
- `LTXVConcatAVLatent` —— 1/7 个有
- `LTXVSeparateAVLatent` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `MiniMaxH3EasyMediaSplitter` —— 1/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/7 个有
- `MiniMaxH3SigmaShift` —— 1/7 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SelfLiftAvatarH3Sampler` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `SolidMask` —— 1/7 个有
- `easy promptConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
