---
name: text_to_image_lora_sampler_clip_87
type: Text To Image
frequency: 15
level: strong
coverage: 0.874067
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json, 视频生成/图生视频/多参考图生视频｜Minimax H3一键生成直出_2092083542187667457.json, 视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频多素材融合_2088699208495882241.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2092760928600285186.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2093795328280584193.json, 视频生成/图生视频/多图参考生视频｜MiniMaxH3图生视频一键生成_2092741832886276098.json, 视频生成/图生视频/多图生视频+音频+视频接入｜MiniMax H3场景特效_2092205364438720514.json, 视频生成/图生视频/多图生视频音频视频接入｜MiniMax H3场景特效生成_2092018470065106945.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093430390005518337.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093761824507383810.json, 视频生成/图生视频/海螺MiniMax-H3开源版图片开口说话数字人-图像音频参考图生视频_2087385959053742082.json, 视频生成/文生视频/3视频)3音频全能参考(9图H3加速优化版MiniMax_2086537090464047105.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/h3开源版H3数字人单人版MiniMax图生视频口播数字人参考音频_2086449565611413505.json、视频生成/图生视频/多参考图生视频｜Minimax H3一键生成直出_2092083542187667457.json、视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 14/15 个有
- `ResolutionSelector` —— 14/15 个有
- `VAEDecodeAudio` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `LoadAudio` —— 13/15 个有
- `CreateVideo` —— 11/15 个有
- `SaveVideo` —— 11/15 个有
- `VHS_VideoCombine` —— 4/15 个有
- `LoadVideo` —— 3/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/15 个有
- `AudioCrop` —— 2/15 个有
- `GetVideoComponents` —— 2/15 个有
- `MiniMaxChunkFeedForward` —— 2/15 个有
- `MiniMaxLowVRAMAttention` —— 2/15 个有
- `AILab_QwenVL` —— 1/15 个有
- `Fast Groups Muter (rgthree)` —— 1/15 个有
- `Int` —— 1/15 个有
- `JWIntegerToString` —— 1/15 个有
- `JoinStrings` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `RTXVideoSuperResolution` —— 1/15 个有
- `SimpleMath+` —— 1/15 个有
- `VHS_LoadVideo` —— 1/15 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

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
