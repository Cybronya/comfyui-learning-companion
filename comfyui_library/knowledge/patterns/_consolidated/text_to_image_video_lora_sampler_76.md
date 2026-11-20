---
name: text_to_image_video_lora_sampler_76
type: Text To Image
frequency: 10
level: strong
coverage: 0.6574
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3一键角色替换 图生视频换人剪辑神器工作流推荐_2094810569621725186.json, 视频生成/图生视频/H3加速版文生视频｜文字一键快速生成视频工作流_2094732479742701569.json, 视频生成/图生视频/H3动作迁移2.0进阶史诗强化，图生视频自带放大_2110857064611405825.json, 视频生成/图生视频/H3动作迁移2.0进阶版史诗强化工作流，图生视频动作迁移处理工具_2107948212886786049.json, 视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json, 视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json, 视频生成/图生视频/H3角色替换工作流｜视频人物替换图生视频生成_2094905654396940289.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106878349405671426.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/H3一键角色替换 图生视频换人剪辑神器工作流推荐_2094810569621725186.json、视频生成/图生视频/H3加速版文生视频｜文字一键快速生成视频工作流_2094732479742701569.json、视频生成/图生视频/H3动作迁移2.0进阶史诗强化，图生视频自带放大_2110857064611405825.json、视频生成/图生视频/H3动作迁移2.0进阶版史诗强化工作流，图生视频动作迁移处理工具_2107948212886786049.json、视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：66%

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
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 9/10 个有
- `LTXVSeparateAVLatent` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `MinimaxH3LatentUpscaler3D` —— 9/10 个有
- `SplitSigmas` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `GetNode` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `easy float` —— 7/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `CR Prompt Text` —— 5/10 个有
- `MiniMaxH3PromptEnhancerT8` —— 5/10 个有
- `PreviewAny` —— 5/10 个有
- `RH_Translator` —— 5/10 个有
- `easy saveText` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `LoadAudio` —— 4/10 个有
- `easy indexTTSForceCleanup` —— 4/10 个有
- `FlashVSRNode` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `Sleep` —— 3/10 个有
- `H3SigmaRefiner` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `MiniMaxLowVRAMAttention` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `Text` —— 2/10 个有
- `GH_AudioVideoMerger` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `MiniMaxH3ImageToVideo` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SeedVR2LoadDiTModel` —— 1/10 个有
- `SeedVR2LoadVAEModel` —— 1/10 个有
- `SeedVR2VideoUpscaler` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足
