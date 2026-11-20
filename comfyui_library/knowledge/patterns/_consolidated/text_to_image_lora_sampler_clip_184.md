---
name: text_to_image_lora_sampler_clip_184
type: Text To Image
frequency: 10
level: strong
coverage: 0.9068
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MINIMAX-H3文戏利器｜多图参考生视频手动版API调用_2105106295446663170.json, 视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json, 视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频 加速版电商内容制作_2098699036625821698.json, 视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json, 视频生成/图生视频/MiniMax H3多图参考优化版｜音频参考极速生视频_2106612379277680642.json, 视频生成/图生视频/MiniMax H3多图参考音频参考加速优化版，图生视频高效产出工具_2105720092976836609.json, 视频生成/图生视频/MiniMax H3极速生视频优化版｜多图加音频参考全支持_2111086493161836545.json, 视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json, 视频生成/图生视频/多图参考角色一致｜MINIMAX-H3图生视频视频生视频直出_2093757341844983809.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3文戏利器｜多图参考生视频手动版API调用_2105106295446663170.json、视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json、视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json、视频生成/图生视频/MiniMax H3图片参考生成带货视频 加速版电商内容制作_2098699036625821698.json、视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

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
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `CreateVideo` —— 7/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `PrimitiveFloat` —— 6/10 个有
- `ResolutionSelector` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `PathchSageAttentionKJ` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `CR Prompt Text` —— 4/10 个有
- `EasyCache` —— 4/10 个有
- `Int` —— 4/10 个有
- `LoraLoaderBypassModelOnly` —— 4/10 个有
- `SaveImage` —— 4/10 个有
- `ShowAnything|Mie` —— 4/10 个有
- `intToFloat _O` —— 4/10 个有
- `ExtendIntermediateSigmas` —— 3/10 个有
- `H3SigmaRefiner` —— 3/10 个有
- `INTConstant` —— 3/10 个有
- `PT_H3ConcatAVLatent` —— 3/10 个有
- `VAEEncode` —— 3/10 个有
- `VAEEncodeAudio` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `MiniMaxH3AVDecodeT8` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `PreviewAudio` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `SoundFlow_GetLength` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
