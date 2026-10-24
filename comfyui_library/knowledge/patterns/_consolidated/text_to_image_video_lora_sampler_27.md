---
name: text_to_image_video_lora_sampler_27
type: Text To Image
frequency: 22
level: strong
coverage: 0.697091
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json, 视频生成/图生视频/MiniMax H3打斗双采｜高质量图生视频生成_2095602888709066753.json, 视频生成/图生视频/MiniMax H3数字人带货视频｜多图直生成模特产品展示_2103033669408608258.json, 视频生成/图生视频/MiniMax H3最强二采工作流｜音画俱佳战斗特效人物视频_2108009547691544578.json, 视频生成/图生视频/MiniMax H3电影感引擎｜人物场景特效加持，帧帧都是大片质感_2099408061910835201.json, 视频生成/图生视频/MiniMax H3电影感视频生成 每一帧电影级画面质感_2099207360228184066.json, 视频生成/图生视频/MiniMax+H3二采多参考生视频，图片视频音频混合输入_2110487892341641217.json, 视频生成/图生视频/MiniMax+H3多参考生视频二采，9图片3视频3音频全兼容_2110467435626319874.json, 视频生成/图生视频/MiniMax-H3开源多图生视频｜数字人视频带货电商口播好帮手_2104534112320180225.json, 视频生成/图生视频/MiniMax-H3开源数字人视频带货｜多图生视频电商口播神器_2104495131775815681.json, 视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json, 视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars电商好帮手_2111119123915821058.json, 视频生成/图生视频/MiniMax_H3多参考7P3A2V生视频优化版｜图生视频_2100805403243278338.json, 视频生成/图生视频/MiniMax_H3多参考生视频优化版，文生视频视频生视频图生视频方案_2109447215457587202.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大工作流，文生视频视频生视频图生视频_2109816691227185154.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大，三种生视频模式_2110541129706987521.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大，三种生视频模式_2110888174443655170.json, 视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json, 视频生成/图生视频/h3 二阶+sigma+latent 采样组合｜数字人图生视频_2096896924396900353.json, 视频生成/图生视频/海螺智能提示词双采样｜minimaxH3加速高清放大图生视频_2093734526240518145.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json、视频生成/图生视频/MiniMax H3打斗双采｜高质量图生视频生成_2095602888709066753.json、视频生成/图生视频/MiniMax H3数字人带货视频｜多图直生成模特产品展示_2103033669408608258.json、视频生成/图生视频/MiniMax H3最强二采工作流｜音画俱佳战斗特效人物视频_2108009547691544578.json、视频生成/图生视频/MiniMax H3电影感引擎｜人物场景特效加持，帧帧都是大片质感_2099408061910835201.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 22 个 workflow 都包含：
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 21/22 个有
- `LTXVSeparateAVLatent` —— 21/22 个有
- `MinimaxH3LatentUpscaler3D` —— 21/22 个有
- `PrimitiveFloat` —— 20/22 个有
- `GetNode` —— 18/22 个有
- `SetNode` —— 18/22 个有
- `孤海注释` —— 18/22 个有
- `SplitSigmas` —— 14/22 个有
- `Text` —— 13/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/22 个有
- `VHS_LoadVideo` —— 11/22 个有
- `ManualSigmas` —— 10/22 个有
- `LoadAudio` —— 8/22 个有
- `SaveImage` —— 8/22 个有
- `easy float` —— 8/22 个有
- `ModelAttentionBackend` —— 7/22 个有
- `CreateVideo` —— 5/22 个有
- `EmptyImage` —— 5/22 个有
- `MiniMaxH3SigmaShift` —— 5/22 个有
- `ModelPreviewOverrideKJ` —— 5/22 个有
- `PreviewImage` —— 5/22 个有
- `Fast Groups Bypasser (rgthree)` —— 4/22 个有
- `ImageResizeKJv2` —— 4/22 个有
- `SaveVideo` —— 4/22 个有
- `CR Text` —— 2/22 个有
- `ExtendIntermediateSigmas` —— 2/22 个有
- `Float` —— 2/22 个有
- `H3SigmaRefiner` —— 2/22 个有
- `SolAttnMiniMax` —— 2/22 个有
- `GetImageSize` —— 1/22 个有
- `ImageConcatMulti` —— 1/22 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/22 个有
- `PathchSageAttentionKJ` —— 1/22 个有
- `RH_LLMAPI_Pro_Node` —— 1/22 个有
- `ShowText|pysssss` —— 1/22 个有
- `StariAI-MiniMaxH3-Skill` —— 1/22 个有
- `TextOverlay` —— 1/22 个有
- `easy showAnything` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（24/22 个样本）：Steps较低可能导致细节不足
