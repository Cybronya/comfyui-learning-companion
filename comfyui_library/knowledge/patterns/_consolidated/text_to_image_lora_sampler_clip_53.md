---
name: text_to_image_lora_sampler_clip_53
type: Text To Image
frequency: 15
level: strong
coverage: 0.863867
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json, 视频生成/图生视频/minimax双图参考生视频｜两张图搞定人物场景视频_2111131778227462145.json, 视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json, 视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json, 视频生成/图生视频/主打图生视频通用工作流｜简易上手多场景视频生成_2108412438193459202.json, 视频生成/图生视频/全能参考图生视频美少女｜miniMAXH3视频生成工作流_2088145573164707841.json, 视频生成/图生视频/全能多参生视频自用版｜Minimax H3 人物场景类特效_2089349057071378433.json, 视频生成/图生视频/加速版图生视频｜MiniMaxH3人物特效快速出片_2093142943912783874.json, 视频生成/图生视频/动作迁移图生视频｜Minimax视频动作迁移工作流_2087218060968161281.json, 视频生成/图生视频/单人数字人直播｜MiniMax H3图生视频驱动口播_2089027921309691906.json, 视频生成/图生视频/单人版数字人直播｜MiniMax H3图生视频口播生成_2088700833398607873.json, 视频生成/图生视频/参考生视频玩法升级｜MiniMax H3 视频生视频双通道_2096253067581812737.json, 视频生成/图生视频/双图版全能参考｜MiniMax H3图生视频高质量生成_2094740772443738114.json, 视频生成/图生视频/多图参考生成视频｜图生视频多图融合一键出片_2093775806538534914.json, 视频生成/图生视频/多图参考直出｜MiniMax H3图生视频一致性生成_2090271687425220609.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json、视频生成/图生视频/minimax双图参考生视频｜两张图搞定人物场景视频_2111131778227462145.json、视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json、视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json、视频生成/图生视频/主打图生视频通用工作流｜简易上手多场景视频生成_2108412438193459202.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 14/15 个有
- `PrimitiveStringMultiline` —— 13/15 个有
- `ResolutionSelector` —— 13/15 个有
- `VAEDecodeAudio` —— 13/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/15 个有
- `LoadAudio` —— 7/15 个有
- `PrimitiveInt` —— 7/15 个有
- `PathchSageAttentionKJ` —— 6/15 个有
- `ComfySwitchNode` —— 5/15 个有
- `PrimitiveBoolean` —— 5/15 个有
- `AudioCrop` —— 2/15 个有
- `SoundFlow_GetLength` —— 2/15 个有
- `VHS_LoadVideo` —— 2/15 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/15 个有
- `EmptyAudio` —— 1/15 个有
- `Fast Bypasser (rgthree)` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `Load Lora` —— 1/15 个有
- `MiniMaxChunkFeedForward` —— 1/15 个有
- `MiniMaxH3AddGuide` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `Text` —— 1/15 个有
- `VideoCombineV2` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
