---
name: text_to_image_lora_sampler_clip_54
type: Text To Image
frequency: 15
level: strong
coverage: 0.894267
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json, 视频生成/图生视频/一键换脸生成新人物｜MiniMax H3角色替换图生视频 视频生视频_2090814396544151553.json, 视频生成/图生视频/加速版图生视频｜H3高质量快速生成工作流_2095093795384811522.json, 视频生成/图生视频/加速版图生视频｜h3图片转视频工作流_2088324394362957826.json, 视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json, 视频生成/图生视频/去除ai感转场运镜｜minimax h3全能参考图生视频_2093764750915231745.json, 视频生成/图生视频/参考生视频Sage加速｜MiniMax H3数字人视频处理2608_2095551559856902146.json, 视频生成/图生视频/图像+视频+音频参考｜H3生成视频多模态工作流_2094735141095694338.json, 视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json, 视频生成/图生视频/极致电影质感｜Minimax-H3转场运镜图生视频_2093229463424299009.json, 视频生成/图生视频/电影级视频多参版v1.0｜minimax H3制作工作流_2093475759825440770.json, 视频生成/图生视频/电影质感极致呈现｜Minimax-H3运镜转场图生视频_2093071322497769473.json, 视频生成/文生视频/H3真实电影质感全能参考 文生视频图生视频_2100309862587654145.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频生成_2094051162357063682.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频直出_2093845276451753986.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json、视频生成/图生视频/一键换脸生成新人物｜MiniMax H3角色替换图生视频 视频生视频_2090814396544151553.json、视频生成/图生视频/加速版图生视频｜H3高质量快速生成工作流_2095093795384811522.json、视频生成/图生视频/加速版图生视频｜h3图片转视频工作流_2088324394362957826.json、视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `PrimitiveFloat`
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
- `VAEDecodeAudio` —— 14/15 个有
- `LoadAudio` —— 13/15 个有
- `MiniMaxH3ReferenceToVideo` —— 13/15 个有
- `PathchSageAttentionKJ` —— 13/15 个有
- `VHS_LoadVideo` —— 13/15 个有
- `CreateVideo` —— 11/15 个有
- `SaveVideo` —— 11/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/15 个有
- `MiniMaxH3BlockCacheT8` —— 10/15 个有
- `easy anythingIndexSwitch` —— 10/15 个有
- `MiniMaxH3ImageToVideo` —— 8/15 个有
- `Fast Groups Bypasser (rgthree)` —— 6/15 个有
- `LoraLoaderBypassModelOnly` —— 6/15 个有
- `easy showAnything` —— 6/15 个有
- `DisableNoise` —— 5/15 个有
- `H3SigmaRefiner` —— 5/15 个有
- `SaveImage` —— 5/15 个有
- `SplitSigmas` —— 5/15 个有
- `VHS_VideoCombine` —— 5/15 个有
- `FlashVSRNode` —— 4/15 个有
- `Sleep` —— 4/15 个有
- `EasyCache` —— 2/15 个有
- `SolAttnPatch` —— 2/15 个有
- `FlashVSRInitPipe` —— 1/15 个有
- `FlashVSRNodeAdv` —— 1/15 个有
- `PainterVRAM` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
