---
name: text_to_image_lora_sampler_clip_39
type: Text To Image
frequency: 16
level: strong
coverage: 0.867313
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json, 视频生成/图生视频/minimax双图参考生视频｜两张图搞定人物场景视频_2111131778227462145.json, 视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json, 视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json, 视频生成/图生视频/主打图生视频通用工作流｜简易上手多场景视频生成_2108412438193459202.json, 视频生成/图生视频/全能参考图生视频美少女｜miniMAXH3视频生成工作流_2088145573164707841.json, 视频生成/图生视频/加速版图生视频｜MiniMaxH3人物特效快速出片_2093142943912783874.json, 视频生成/图生视频/单人数字人直播｜MiniMax H3图生视频驱动口播_2089027921309691906.json, 视频生成/图生视频/单人版数字人直播｜MiniMax H3图生视频口播生成_2088700833398607873.json, 视频生成/图生视频/参考生视频玩法升级｜MiniMax H3 视频生视频双通道_2096253067581812737.json, 视频生成/图生视频/双图版全能参考｜MiniMax H3图生视频高质量生成_2094740772443738114.json, 视频生成/图生视频/多图参考直出｜MiniMax H3图生视频一致性生成_2090271687425220609.json, 视频生成/图生视频/对口型音频驱动MiniMax H3数字人唱歌工作流，一张图一段音频生成视频_2106864466716614658.json, 视频生成/图生视频/数字人单人极速版｜Minimax H3角色一致图生视频_2092026882165403650.json, 视频生成/图生视频/数字人唱歌口播｜MiniMax H3图生视频一键直出_2090220837587742722.json, 视频生成/图生视频/音频驱动对口型｜Minimax H3数字人人物特效图生视频_2089446222766624769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json、视频生成/图生视频/minimax双图参考生视频｜两张图搞定人物场景视频_2111131778227462145.json、视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json、视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json、视频生成/图生视频/主打图生视频通用工作流｜简易上手多场景视频生成_2108412438193459202.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 15/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/16 个有
- `SaveVideo` —— 12/16 个有
- `CreateVideo` —— 11/16 个有
- `LoadAudio` —— 10/16 个有
- `VAEDecodeAudio` —— 10/16 个有
- `PathchSageAttentionKJ` —— 7/16 个有
- `AudioCrop` —— 6/16 个有
- `PrimitiveInt` —— 6/16 个有
- `SoundFlow_GetLength` —— 6/16 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 6/16 个有
- `ComfySwitchNode` —— 5/16 个有
- `PrimitiveBoolean` —— 5/16 个有
- `PreviewAudio` —— 4/16 个有
- `VHS_VideoCombine` —— 4/16 个有
- `EmptyAudio` —— 2/16 个有
- `SaveImage` —— 2/16 个有
- `AudioConcat` —— 1/16 个有
- `Fast Bypasser (rgthree)` —— 1/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `MiniMaxChunkFeedForward` —— 1/16 个有
- `MiniMaxH3AddGuide` —— 1/16 个有
- `VideoCombineV2` —— 1/16 个有

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
