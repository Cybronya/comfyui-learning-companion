---
name: text_to_image_video_lora_sampler_10
type: Text To Image
frequency: 33
level: strong
coverage: 0.539273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参考生视频｜字节DMAD加速双倍高清放大_2107644291471466498.json, 视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json, 视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json, 视频生成/图生视频/Minimax H3动作迁移2.0进阶｜视频生视频史诗级强化_2103047047137021954.json, 视频生成/图生视频/双倍高清放大MiniMax H3多参考生视频字节DMAD加速版工作流，图生视频_2107922679855669249.json, 视频生成/图生视频/多参生视频优化版｜MiniMax H3支持9图3音3视频参考_2095857101267628033.json, 视频生成/图生视频/多参考生视频4步加速｜MiniMax H3一采二采双输出_2095968881948061697.json, 视频生成/图生视频/多参考生视频720p高清｜MiniMax H3场景特效生成_2096685620121919489.json, 视频生成/图生视频/多参考生视频优化版｜MiniMax H3开源角色一致性_2094562356952125442.json, 视频生成/图生视频/多参考生视频优化版｜MiniMax H3开源角色一致性设计_2094363837834293250.json, 视频生成/图生视频/多参考生视频加速优化版工作流，图生视频多参考视频生成方案_2108335231181877250.json, 视频生成/图生视频/开源多参考优化版｜MiniMax H3角色一致性生视频_2094474289755021314.json, 视频生成/图生视频/首尾帧生成视频｜MiniMax H3官方工作流图生视频_2090268705291849730.json, 视频生成/文生视频/H3动作迁移2.0单图参考版视频生成处理工具包_2100995556775645185.json, 视频生成/文生视频/H3多参考7P3A2V生视频二采优化版工具_2100646011814371329.json, 视频生成/文生视频/H3最强全能工作流言出法随 视频生成处理工具_2100673673299587074.json, 视频生成/文生视频/H3最强双采FL2-736P高清PRO焚诀展开篇｜文生视频视频生视频图生视频全链路_2100454010141626369.json, 视频生成/文生视频/H3虚幻引擎赛璐璃风格漫画流双采FL2高清PRO处理_2100642569272254465.json, 视频生成/文生视频/H3言出法随至尊工作流｜文生图生视频全能生成_2097497018427072514.json, 视频生成/文生视频/Jason二采H3多参考生视频优化版V2｜三模式视频生成_2108420583481499650.json, 视频生成/文生视频/Jason二采H3多参考生视频优化版｜不油腻二采高清放大更耐看_2101906733156364290.json, 视频生成/文生视频/MiniMax H3 全能视频生成｜文生图生视频多合一极速二采优化_2097497016648683521.json, 视频生成/文生视频/MiniMax H3多参考7P3A2V二采优化版｜多素材混合生视频，画面节奏更耐看_2100487458340294657.json, 视频生成/文生视频/MiniMax H3多参考7P3A2V生视频优化版｜文生视频视频生视频全都能接_2100485687203155970.json, 视频生成/文生视频/MiniMax H3多参考生视频9图片3视频3音频处理工具_2102119756018044929.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版，文生视频视频生视频图生视频方案_2107247870394064897.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜文生视频图生视频画质更稳_2104532274321645569.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜文生视频视频生视频_2106990754123051010.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜高质量生成_2095587743173799938.json, 视频生成/文生视频/MiniMax H3多参考生视频最新优化版 多模态输入方案_2105415601509462017.json, 视频生成/文生视频/MiniMax H3多参考生视频｜优化版高质量生成_2095226419768029186.json, 视频生成/文生视频/MiniMax H3多参考生视频｜最新优化版效果再升级_2105135308315648002.json, 视频生成/文生视频/MiniMax H3多图多音频视频参考｜无水印优化版_2095227965956247554.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参考生视频｜字节DMAD加速双倍高清放大_2107644291471466498.json、视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json、视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json、视频生成/图生视频/Minimax H3动作迁移2.0进阶｜视频生视频史诗级强化_2103047047137021954.json、视频生成/图生视频/双倍高清放大MiniMax H3多参考生视频字节DMAD加速版工作流，图生视频_2107922679855669249.json…）

- **类型**：Text To Image
- **样本数**：33
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 33 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Text` —— 32/33 个有
- `LTXVConcatAVLatent` —— 31/33 个有
- `LTXVSeparateAVLatent` —— 31/33 个有
- `LoadAudio` —— 31/33 个有
- `MinimaxH3LatentUpscaler3D` —— 31/33 个有
- `SplitSigmas` —— 31/33 个有
- `VAEDecodeAudio` —— 31/33 个有
- `VHS_LoadVideo` —— 31/33 个有
- `easy float` —— 29/33 个有
- `SaveImage` —— 10/33 个有
- `忽略多组孤海` —— 5/33 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/33 个有
- `MiniMaxH3AVDecodeT8` —— 4/33 个有
- `Astra` —— 2/33 个有
- `Fast Groups Bypasser (rgthree)` —— 2/33 个有
- `ImageFromBatch` —— 2/33 个有
- `Int` —— 2/33 个有
- `LoadVideo` —— 2/33 个有
- `PreviewImage` —— 2/33 个有
- `RunningHub Deepcleaner` —— 2/33 个有
- `SaveVideo` —— 2/33 个有
- `easy showAnything` —— 2/33 个有
- `获取视频信息` —— 2/33 个有
- `BlockSparseAttention` —— 1/33 个有
- `PrimitiveBoolean` —— 1/33 个有
- `图像缩放范围孤海` —— 1/33 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 33 | 100% |
| 高度 | 80 | 80 - 80 | 33 | 100% |
| 采样步数 | 4 | 4 - 4 | 33 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 33 | 100% |
| 采样算法 | er_sde | - | 33 | 100% |
| 调度器 | beta | - | 33 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 33 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 34/33 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，33 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，33 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，33 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，33 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，33 个样本，一致性 100%
- 调度器 最常用 beta，33 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 高发问题（34/33 个样本）：Steps较低可能导致细节不足
