---
name: text_to_image_lora_sampler_clip_365
type: Text To Image
frequency: 6
level: strong
coverage: 0.878167
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json, 视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json, 视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json, 视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json, 视频生成/文生视频/MiniMax H3 SelfLift低分辨率采样器加速视频生成工具_2101028313874649090.json, 视频生成/文生视频/低显存12GB直出1080P高分辨率视频，BUNNY SelfLift混合工作流LoRA不模糊_2102864635153182721.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_365

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json、视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json、视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json、视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json、视频生成/文生视频/MiniMax H3 SelfLift低分辨率采样器加速视频生成工具_2101028313874649090.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `H3SigmaRefiner` —— 4/6 个有
- `LoraLoaderBypassModelOnly` —— 4/6 个有
- `MiniMaxH3AVDecodeT8` —— 4/6 个有
- `SelfLiftAvatarH3Sampler` —— 4/6 个有
- `SelfLiftAvatarH3TST` —— 4/6 个有
- `SolAttnMiniMax` —— 4/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `SelfLiftH3Sampler` —— 2/6 个有
- `VAEDecodeAudio` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `ExtendIntermediateSigmas` —— 1/6 个有
- `LTXVSeparateAVLatent` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `MiniMaxH3ReferenceToVideo` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
