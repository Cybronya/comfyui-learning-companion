---
name: text_to_image_lora_sampler_clip_114
type: Text To Image
frequency: 10
level: strong
coverage: 0.8935
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/多合一加速修复｜MiniMax H3热门IP模糊视频高清处理_2090232166843240449.json, 视频生成/文生视频/开源版文生视频｜MiniMax-H3提示词一键出片_2089012717008023553.json, 视频生成/文生视频/开源版文生视频｜MiniMax-H3纯文本生成视频开源工作流_2088773720985923585.json, 视频生成/文生视频/文生视频直出｜MiniMax H3高清一键生成_2089797615142658050.json, 视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速_2089249506813636609.json, 视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速刘神_2094117560072626177.json, 视频生成/文生视频/最新8步增速5分钟出10秒｜Minimax H3文生视频+视频放大_2089036367534845953.json, 视频生成/文生视频/最新最快4步8步增速工作流Minimax H3文生视频图生视频_2088410988835074049.json, 视频生成/文生视频/最新最快4步和8步增速｜Minimax H3文生图生视频工作流_2088388313551040514.json, 视频生成/文生视频/海螺MiniMax H3开源版Turbo全模式视频整合流处理工具_2101755741546835970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/多合一加速修复｜MiniMax H3热门IP模糊视频高清处理_2090232166843240449.json、视频生成/文生视频/开源版文生视频｜MiniMax-H3提示词一键出片_2089012717008023553.json、视频生成/文生视频/开源版文生视频｜MiniMax-H3纯文本生成视频开源工作流_2088773720985923585.json、视频生成/文生视频/文生视频直出｜MiniMax H3高清一键生成_2089797615142658050.json、视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速_2089249506813636609.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/10 个有
- `SaveVideo` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `BasicScheduler` —— 7/10 个有
- `KSamplerSelect` —— 7/10 个有
- `LoraLoaderBypassModelOnly` —— 5/10 个有
- `LoadImage` —— 4/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 4/10 个有
- `GetVideoComponents` —— 3/10 个有
- `LoadAudio` —— 3/10 个有
- `LoadVideo` —— 3/10 个有
- `MiniMaxH3ReferenceToVideo` —— 3/10 个有
- `CR Float To Integer` —— 2/10 个有
- `CR Text` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `Any Switch (rgthree)` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `ImpactConditionalBranch` —— 1/10 个有
- `Int` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `VHS_VideoCombine` —— 1/10 个有
- `easy boolean` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
