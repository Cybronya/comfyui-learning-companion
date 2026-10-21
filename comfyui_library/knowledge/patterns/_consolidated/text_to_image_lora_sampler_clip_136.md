---
name: text_to_image_lora_sampler_clip_136
type: Text To Image
frequency: 9
level: strong
coverage: 0.874444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json, 视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json, 视频生成/文生视频/多参图像音频极速生视频｜加速版MiniMax H3生成_2096328491850625026.json, 视频生成/文生视频/多参考全模态生成器｜MiniMax H3文生视频生视频_2091215931107266561.json, 视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json, 视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json, 视频生成/文生视频/多素材联合参考video_minimax_h3_r2v_2085451709555499009.json, 视频生成/文生视频/新4步LoRa参考图｜MiniMax H3角色一致图生视频_2092736016280023041.json, 视频生成/文生视频/量化加速参考生视频｜MiniMaxH3 文本图像音视频全参考_2089345982659121153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json、视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json、视频生成/文生视频/多参图像音频极速生视频｜加速版MiniMax H3生成_2096328491850625026.json、视频生成/文生视频/多参考全模态生成器｜MiniMax H3文生视频生视频_2091215931107266561.json、视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `MiniMaxH3ReferenceToVideo` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `LoadAudio` —— 7/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `PathchSageAttentionKJ` —— 4/9 个有
- `EasyCache` —— 2/9 个有
- `GetVideoComponents` —— 2/9 个有
- `LoadVideo` —— 2/9 个有
- `AudioAdjustVolume` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `MiniMaxH3Easy` —— 1/9 个有
- `MiniMaxH3EasyLoader` —— 1/9 个有
- `MiniMaxH3EasyOutput` —— 1/9 个有
- `ShowAnything|Mie` —— 1/9 个有
- `Text` —— 1/9 个有
- `VideoInfoLoaded` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

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
