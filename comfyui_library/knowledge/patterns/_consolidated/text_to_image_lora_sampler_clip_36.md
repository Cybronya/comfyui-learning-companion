---
name: text_to_image_lora_sampler_clip_36
type: Text To Image
frequency: 17
level: strong
coverage: 0.919588
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json, 视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json, 视频生成/文生视频/图生视频5秒1080p｜MiniMax-H3八分钟全节点注释_2090913102907920385.json, 视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json, 视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json, 视频生成/文生视频/多图+音频参考加速｜MiniMax H3优化版生视频_2094745022984974337.json, 视频生成/文生视频/多图参考加音频参考｜MiniMax H3 加速优化版 参考生视频更听话_2105490121989648386.json, 视频生成/文生视频/多图参考音频参考加速优化版｜MiniMax H3文生视频生成_2097027445839978498.json, 视频生成/文生视频/多图参考音频参考加速优化｜MiniMax H3文生图生视频_2091270580233400322.json, 视频生成/文生视频/多图参考音频参考加速版｜MiniMax H3图生视频生成_2097046537246433282.json, 视频生成/文生视频/多图参考音频参考加速版｜MiniMax H3文生视频_2092342768986320898.json, 视频生成/文生视频/多图参考音频参考极速生视频｜MiniMax H3优化版_2092070354985508866.json, 视频生成/文生视频/多图参考音频参考｜MiniMax H3加速版图生视频_2090895313207910402.json, 视频生成/文生视频/多图参考音频参考｜MiniMax H3极速生视频优化版_2090662418232991745.json, 视频生成/文生视频/多图音频参考加速版｜MiniMax H3图生视频_2091193733667704834.json, 视频生成/文生视频/极速生视频优化版｜MiniMax H3多图音频参考生成_2094750958134841346.json, 视频生成/文生视频/音频参考极速生视频｜MiniMax H3多图参考优化版_2090836383433842690.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json、视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json、视频生成/文生视频/图生视频5秒1080p｜MiniMax-H3八分钟全节点注释_2090913102907920385.json、视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json、视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 17 个 workflow 都包含：
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
- `ComfyMathExpression` —— 16/17 个有
- `MiniMaxH3ReferenceToVideo` —— 15/17 个有
- `PathchSageAttentionKJ` —— 15/17 个有
- `EasyCache` —— 14/17 个有
- `LoadAudio` —— 14/17 个有
- `Int` —— 13/17 个有
- `ImageResizeKJv2` —— 12/17 个有
- `ShowAnything|Mie` —— 12/17 个有
- `intToFloat _O` —— 11/17 个有
- `CR Prompt Text` —— 8/17 个有
- `PrimitiveStringMultiline` —— 6/17 个有
- `ResolutionSelector` —— 4/17 个有
- `PrimitiveFloat` —— 3/17 个有
- `SaveImage` —— 3/17 个有
- `VHS_LoadVideo` —— 2/17 个有
- `AudioAdjustVolume` —— 1/17 个有
- `CR Text` —— 1/17 个有
- `MiniMaxH3Easy` —— 1/17 个有
- `MiniMaxH3EasyLoader` —— 1/17 个有
- `MiniMaxH3EasyOutput` —— 1/17 个有
- `MiniMaxH3ImageToVideo` —— 1/17 个有
- `Text` —— 1/17 个有
- `VideoInfoLoaded` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
