---
name: text_to_image_video_lora_sampler_19
type: Text To Image
frequency: 26
level: weak
coverage: 0.605462
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/多图生视频超强数字人带货｜多人场景视频制作一文搞定_2114674540256251905.json, 图片生成/文生图/多图生视频，超强数字人视频带货！可用于多人场景视频制作_2114335595865657346.json, 图片生成/文生图/文生图，图生视频_2114339756279689217.json, 图片生成/文生图/文生视频 MiniMax H3_2097845481618624513.json, 数字人/数字人/H3二采二次采样流｜数字人画质细节双提升_2111791019443449858.json, 数字人/数字人/MiniMax H3多参考生视频优化版，数字人文生视频两开花_2112678299272040449.json, 数字人/数字人/MiniMaxH3多图生视频数字人，带货视频角色一致性在线_2112674959268081665.json, 数字人/数字人/Singularity V2最强一致性 多参考双采视频生成工具_2114074031975657474.json, 数字人/数字人/电影质感数字人视频生成｜数字人出演大片氛围一键制作_2113527856457408514.json, 视频生成/图生视频/2采五段加速流 视频生成加速方案高效出片_2104985692295229442.json, 视频生成/图生视频/H3动作迁移2.0进阶版史诗强化工作流，图生视频动作迁移处理工具_2107948212886786049.json, 视频生成/图生视频/H3多参考双采5秒一致性版 Singularity精修短片_2098842004485664770.json, 视频生成/图生视频/H3多参考双采5秒一致性版｜多图参考短平快出片不跑脸_2099124913448767489.json, 视频生成/图生视频/H3最强二采吊打SelfLift虚空折叠流工作流，人物类特效图生视频方案_2107910096905920513.json, 视频生成/图生视频/H3最强二采唐僧彩蛋工作流，人物类特效场景类特效图生视频方案_2108293181078073346.json, 视频生成/图生视频/H3最强二采音画俱佳工作流，人物类特效战斗特效图生视频方案_2108346316232417282.json, 视频生成/图生视频/H3最强二采飓风京剧工作流，人物类特效场景类特效图生视频方案_2108289982774464514.json, 视频生成/图生视频/H3电影感视频生成 每一帧电影级画面质感_2099578194558017538.json, 视频生成/图生视频/H3电影感视频生成 每帧电影级画面质感 高品质输出_2099579950520160258.json, 视频生成/图生视频/H3虚空折叠流最强二采 视频动态超越SelfLift_2110355960790343681.json, 视频生成/图生视频/H3超强工作流图生视频高质量视频生成方案 动态生成优化_2108717274050940929.json, 视频生成/图生视频/H3超强工作流，图生视频高质量视频生成方案_2107999971776749569.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版 高质量图生视频_2098861196861595649.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版｜多图融合一致性出片更稳｜图生视频_2099105339022073857.json, 视频生成/图生视频/MiniMax H3多参考生视频无限流五段二采串联处理工具_2102166646034100225.json, 视频生成/图生视频/五段式加速二采工作流｜角色表演视频一次成型｜图生视频高效出片_2104743299977400322.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/多图生视频超强数字人带货｜多人场景视频制作一文搞定_2114674540256251905.json、图片生成/文生图/多图生视频，超强数字人视频带货！可用于多人场景视频制作_2114335595865657346.json、图片生成/文生图/文生图，图生视频_2114339756279689217.json、图片生成/文生图/文生视频 MiniMax H3_2097845481618624513.json、数字人/数字人/H3二采二次采样流｜数字人画质细节双提升_2111791019443449858.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 26 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 25/26 个有
- `LTXVSeparateAVLatent` —— 25/26 个有
- `LoadImage` —— 25/26 个有
- `MiniMaxH3ReferenceToVideo` —— 25/26 个有
- `MinimaxH3LatentUpscaler3D` —— 25/26 个有
- `GetNode` —— 24/26 个有
- `SetNode` —— 24/26 个有
- `solarL_SaveImagesToZip` —— 23/26 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 22/26 个有
- `孤海注释` —— 22/26 个有
- `SplitSigmas` —— 21/26 个有
- `easy float` —— 21/26 个有
- `Text` —— 20/26 个有
- `SaveImage` —— 19/26 个有
- `VHS_LoadVideo` —— 19/26 个有
- `LoadAudio` —— 18/26 个有
- `ModelAttentionBackend` —— 9/26 个有
- `ManualSigmas` —— 4/26 个有
- `AudioConcat` —— 3/26 个有
- `CreateVideo` —— 3/26 个有
- `Fast Groups Bypasser (rgthree)` —— 3/26 个有
- `GetImageRangeFromBatch` —— 3/26 个有
- `ImageBatchMulti` —— 3/26 个有
- `Lora Loader Stack (rgthree)` —— 3/26 个有
- `MiniMaxH3AddGuide` —— 3/26 个有
- `SaveAudio` —— 3/26 个有
- `SaveVideo` —— 3/26 个有
- `SolAttnMiniMax` —— 3/26 个有
- `TrimAudioDuration` —— 3/26 个有
- `easy cleanGpuUsed` —— 3/26 个有
- `BlockSparseAttention` —— 2/26 个有
- `MiniMaxH3SigmaShift` —— 2/26 个有
- `PrimitiveInt` —— 2/26 个有
- `Text Multiline` —— 2/26 个有
- `easy loraStack` —— 2/26 个有
- `easy loraStackApply` —— 2/26 个有
- `LayerColor: ColorAdapter` —— 1/26 个有
- `MiniMaxH3ImageToVideo` —— 1/26 个有
- `VHS_LoadVideoFFmpeg` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 26 | 33% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 26 | 73% |
| 采样算法 | er_sde | - | 26 | 88% |
| 调度器 | beta | - | 26 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| 宽度 | 80 | 80 - 1024 | 26 | 0% |
| 高度 | 80 | 80 - 1024 | 26 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，26 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，26 个样本
- 采样算法 最常用 er_sde，26 个样本，一致性 88%
- 调度器 最常用 beta，26 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，26 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，26 个样本，取值分散，一致性仅 0%
- 高发问题（25/26 个样本）：Steps较低可能导致细节不足
