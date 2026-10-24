---
name: text_to_image_lora_sampler_clip_48
type: Text To Image
frequency: 19
level: strong
coverage: 0.896
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json, 视频生成/图生视频/MiniMax H3多图参考优化版｜音频参考极速生视频_2106612379277680642.json, 视频生成/图生视频/MiniMax H3多图参考生成视频，图生视频与视频生视频全能参考方案_2102813018273968130.json, 视频生成/图生视频/MiniMax H3多图参考生视频图生视频处理生成工具_2101745060818808833.json, 视频生成/图生视频/MiniMax H3多图参考生视频工作流，视频生视频图生视频多素材融合方案_2105760424162586626.json, 视频生成/图生视频/MiniMax H3多图参考生视频｜几张图一起喂｜人物场景一致性拉满_2102579245317967874.json, 视频生成/图生视频/MiniMax H3多图参考生视频｜多素材参考一致性视频生成_2108015949080260609.json, 视频生成/图生视频/MiniMax H3多图参考音频参考加速优化版，图生视频高效产出工具_2105720092976836609.json, 视频生成/图生视频/MiniMax H3多图参考｜图生视频多图生成_2090449654759645186.json, 视频生成/图生视频/MiniMax H3极速生视频优化版｜多图加音频参考全支持_2111086493161836545.json, 视频生成/图生视频/MiniMax H3武打导演9组预设，视频生视频战斗特效_2111214317717770241.json, 视频生成/图生视频/MiniMax H3首尾帧加速版｜图生视频出片更快更稳_2111084749388341249.json, 视频生成/图生视频/MiniMax H3首尾帧加速版｜图生视频运镜更流畅_2106610629435019266.json, 视频生成/图生视频/MiniMax H3首尾帧视频加速版，图生视频更流畅_2111203485525037057.json, 视频生成/图生视频/MiniMax+H3加速版图文一键生视频｜运镜丝滑出片快_2111327354969747458.json, 视频生成/图生视频/加速版MiniMax_H3图文直出视频｜一句话配一张图，成片一键拿_2099445108864282625.json, 视频生成/图生视频/加速版MiniMax_H3多参生视频｜图像音频一起喂，出片速度起飞_2099442755004096513.json, 视频生成/文生视频/MiniMax H3加速版首尾帧图生视频处理工具_2101022392209461249.json, 视频生成/文生视频/MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多图加音频参考，极速生视频优化方案_2111205029150547969.json、视频生成/图生视频/MiniMax H3多图参考优化版｜音频参考极速生视频_2106612379277680642.json、视频生成/图生视频/MiniMax H3多图参考生成视频，图生视频与视频生视频全能参考方案_2102813018273968130.json、视频生成/图生视频/MiniMax H3多图参考生视频图生视频处理生成工具_2101745060818808833.json、视频生成/图生视频/MiniMax H3多图参考生视频工作流，视频生视频图生视频多素材融合方案_2105760424162586626.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
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
- `LoadAudio` —— 13/19 个有
- `MiniMaxH3ReferenceToVideo` —— 13/19 个有
- `EasyCache` —— 11/19 个有
- `PathchSageAttentionKJ` —— 11/19 个有
- `PrimitiveFloat` —— 11/19 个有
- `ResolutionSelector` —— 11/19 个有
- `ShowAnything|Mie` —— 11/19 个有
- `CR Prompt Text` —— 10/19 个有
- `ImageResizeKJv2` —— 9/19 个有
- `PrimitiveStringMultiline` —— 9/19 个有
- `Int` —— 8/19 个有
- `MiniMaxH3ImageToVideo` —— 8/19 个有
- `SaveImage` —— 8/19 个有
- `CM_IntToFloat` —— 4/19 个有
- `intToFloat _O` —— 4/19 个有
- `ComfySwitchNode` —— 3/19 个有
- `DF_Int_to_Float` —— 3/19 个有
- `ImpactSwitch` —— 3/19 个有
- `PrimitiveInt` —— 3/19 个有
- `EmptyImage` —— 2/19 个有
- `GetVideoComponents` —— 2/19 个有
- `LoadVideo` —— 2/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/19 个有
- `PreviewImage` —— 2/19 个有
- `PrimitiveBoolean` —— 2/19 个有
- `Fast Bypasser (rgthree)` —— 1/19 个有
- `LoraLoaderBypassModelOnly` —— 1/19 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/19 个有
- `MinimaxH3LatentUpscaler3DRefineHandoff` —— 1/19 个有
- `PT_H3ConcatAVLatent` —— 1/19 个有
- `VAEEncode` —— 1/19 个有
- `VAEEncodeAudio` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
