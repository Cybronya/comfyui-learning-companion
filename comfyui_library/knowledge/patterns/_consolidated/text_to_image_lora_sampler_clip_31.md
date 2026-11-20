---
name: text_to_image_lora_sampler_clip_31
type: Text To Image
frequency: 22
level: strong
coverage: 0.8765
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒135S长视频_2110360650903023617.json, 视频生成/图生视频/MiniMax H3首尾帧图生视频 多模式视频生成处理工具_2113357272276619265.json, 视频生成/图生视频/MiniMax-H3 Ref2va参考生视频标准版｜高质量_2095566940180930561.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2086208730663841794.json, 视频生成/图生视频/MiniMaxH3参考生视频量化加速版｜文本图像音频视频全模态，图生视频更快出活_2100449477902553090.json, 视频生成/图生视频/MiniMax_H3 I2V加速多参考生视频，高效图生视频工具_2110532068039028738.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考生视频，高效图生视频工具_2111269686322225154.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考视频生成工作流，图生视频高效创作工具_2109863281748963329.json, 视频生成/图生视频/MiniMax_H3_I2V加速首尾帧工作流，图生视频高效创作工具_2110535989906202626.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频图生视频与视频生视频全能参考方案_2109448439166750721.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频，图生视频与视频生视频全能参考方案_2106558188098248705.json, 视频生成/图生视频/MiniMax_H3开源版首尾帧8步加速工作流，数字人图生视频处理工具_2109441379188436993.json, 视频生成/图生视频/MiniMax参考生视频视频生视频图生视频_2086540228310945793.json, 视频生成/图生视频/Minimax H3单人极速人物替换，角色一致性动作迁移_2110538185297186818.json, 视频生成/图生视频/Minimax_H3单人极速人物替换，角色一致性动作迁移_2110892482811744258.json, 视频生成/图生视频/minimax最强动作武打视频生视频，战斗特效一步到位_2111187364122030082.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2106530579587096577.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2106881388426383362.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2109439827979628546.json, 视频生成/图生视频/无限长视频流生成 多镜头角色表演图生视频_2098817794715504642.json, 视频生成/文生视频/MiniMax H3超长视频流一次直出2分15秒视频135秒，图生视频长视频方案_2107164033324511233.json, 视频生成/文生视频/MiniMax H3超长视频流｜一次直出2分15秒135S成片｜文生图生全支持_2101875396814917633.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒135S长视频_2110360650903023617.json、视频生成/图生视频/MiniMax H3首尾帧图生视频 多模式视频生成处理工具_2113357272276619265.json、视频生成/图生视频/MiniMax-H3 Ref2va参考生视频标准版｜高质量_2095566940180930561.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2086208730663841794.json、视频生成/图生视频/MiniMaxH3参考生视频量化加速版｜文本图像音频视频全模态，图生视频更快出活_2100449477902553090.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：88%

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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 20/22 个有
- `PrimitiveStringMultiline` —— 18/22 个有
- `SaveImage` —— 17/22 个有
- `MiniMaxH3ReferenceToVideo` —— 16/22 个有
- `孤海注释` —— 15/22 个有
- `CreateVideo` —— 14/22 个有
- `SaveVideo` —— 12/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/22 个有
- `EmptyImage` —— 10/22 个有
- `PreviewImage` —— 10/22 个有
- `VHS_VideoCombine` —— 10/22 个有
- `AudioConcat` —— 8/22 个有
- `GetImageRangeFromBatch` —— 8/22 个有
- `ImageBatchMulti` —— 8/22 个有
- `MiniMaxH3AddGuide` —— 8/22 个有
- `LayerColor: ColorAdapter` —— 7/22 个有
- `SaveAudio` —— 7/22 个有
- `MiniMaxH3ImageToVideo` —— 6/22 个有
- `LoadAudio` —— 5/22 个有
- `VHS_LoadVideo` —— 5/22 个有
- `MuyeTextEditOutput` —— 2/22 个有
- `VHS_VideoInfoLoaded` —— 2/22 个有
- `BlockSparseAttention` —— 1/22 个有
- `EasyCache` —— 1/22 个有
- `LoadVideo` —— 1/22 个有
- `ManualSigmas` —— 1/22 个有
- `ModelAttentionBackend` —— 1/22 个有
- `ModelPreviewOverrideKJ` —— 1/22 个有
- `SaveAudioAdvanced` —— 1/22 个有

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
| Steps较低可能导致细节不足 | 28/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（28/22 个样本）：Steps较低可能导致细节不足
