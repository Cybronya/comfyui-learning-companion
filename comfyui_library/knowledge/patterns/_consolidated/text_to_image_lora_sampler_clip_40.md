---
name: text_to_image_lora_sampler_clip_40
type: Text To Image
frequency: 16
level: strong
coverage: 0.8765
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/人物三视图生成｜MinimaxH3老金驿站高细节工作流_2090834916031426562.json, 视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json, 视频生成/图生视频/多参考图生视频｜Minimax H3一键生成直出_2092083542187667457.json, 视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频多素材融合_2088699208495882241.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2092760928600285186.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2093795328280584193.json, 视频生成/图生视频/多图参考生视频｜MiniMaxH3图生视频一键生成_2092741832886276098.json, 视频生成/图生视频/多图生视频+音频+视频接入｜MiniMax H3场景特效_2092205364438720514.json, 视频生成/图生视频/多图生视频音频视频接入｜MiniMax H3场景特效生成_2092018470065106945.json, 视频生成/图生视频/海螺MiniMax-H3开源版图片开口说话数字人-图像音频参考图生视频_2087385959053742082.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3一键直出_2090902980487892993.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3文生图生视频_2092019899022528514.json, 视频生成/文生视频/多参考全模态生成器｜MiniMax H3文生视频生视频_2091215931107266561.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/人物三视图生成｜MinimaxH3老金驿站高细节工作流_2090834916031426562.json、视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json、视频生成/图生视频/多参考图生视频｜Minimax H3一键生成直出_2092083542187667457.json、视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 15/16 个有
- `PrimitiveFloat` —— 15/16 个有
- `VAEDecodeAudio` —— 15/16 个有
- `CreateVideo` —— 14/16 个有
- `LoadAudio` —— 14/16 个有
- `SaveVideo` —— 14/16 个有
- `GetVideoComponents` —— 5/16 个有
- `LoadVideo` —— 5/16 个有
- `MiniMaxChunkFeedForward` —— 3/16 个有
- `AILab_QwenVL` —— 2/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/16 个有
- `MiniMaxLowVRAMAttention` —— 2/16 个有
- `VHS_VideoCombine` —— 2/16 个有
- `AudioCrop` —— 1/16 个有
- `ImageFromBatch` —— 1/16 个有
- `ImageStitch` —— 1/16 个有
- `JoinStrings` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有
- `ModelAttentionBackend` —— 1/16 个有
- `ModelPatchTorchSettings` —— 1/16 个有
- `SaveImage` —— 1/16 个有
- `StringConcatenate` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
