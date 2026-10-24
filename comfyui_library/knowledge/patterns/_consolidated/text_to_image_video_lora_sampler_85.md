---
name: text_to_image_video_lora_sampler_85
type: Text To Image
frequency: 9
level: strong
coverage: 0.897222
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Seedance2.5文生视频工作流｜视频运镜高质量生成_2097809713382649858.json, 视频生成/图生视频/h3开源加速版MINIMAX-H3合集｜单图生多图参考4步lora加速_2097965293799825409.json, 视频生成/图生视频/light2v8步lora正式版双时钟｜minimax图生视频工作流_2088212552772841473.json, 视频生成/图生视频/minimax h3多参工作流｜多参考图生视频高质量生成_2097060954776367106.json, 视频生成/图生视频/minimax h3多参工作流｜多图参考图生视频生成_2094887223530450946.json, 视频生成/图生视频/minimax h3电商带货视频自动提示词模特产品展示_2088181792762318849.json, 视频生成/图生视频/minmax生图工作流｜图生视频配套生图方案_2097990295555235841.json, 视频生成/图生视频/动作镜头参考洗稿｜MiniMax-H3视频运镜生成_2093772942814572545.json, 视频生成/图生视频/镜头动作参考洗稿｜MiniMax-H3视频运镜图生视频_2093442197000646657.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Seedance2.5文生视频工作流｜视频运镜高质量生成_2097809713382649858.json、视频生成/图生视频/h3开源加速版MINIMAX-H3合集｜单图生多图参考4步lora加速_2097965293799825409.json、视频生成/图生视频/light2v8步lora正式版双时钟｜minimax图生视频工作流_2088212552772841473.json、视频生成/图生视频/minimax h3多参工作流｜多参考图生视频高质量生成_2097060954776367106.json、视频生成/图生视频/minimax h3多参工作流｜多图参考图生视频生成_2094887223530450946.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DualClockSamplerT8` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `CR Text` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `ModelAttentionBackend` —— 3/9 个有
- `SaveImage` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `ImageConcanate` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `MiniMaxH3BlockCacheT8` —— 2/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/9 个有
- `MiniMaxH3TurboLoRA` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `easy int` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `UniBlockSwap` —— 1/9 个有

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
