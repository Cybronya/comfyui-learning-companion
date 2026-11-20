---
name: text_to_image_lora_sampler_clip_23
type: Text To Image
frequency: 24
level: strong
coverage: 0.806
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json, 视频生成/图生视频/全能参考图生视频美少女｜miniMAXH3视频生成工作流_2088145573164707841.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2089305534913667073.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2090649252212076545.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3自定义背景人物迁移_2090938897554567170.json, 视频生成/图生视频/全能多参生视频自用版｜Minimax H3 人物场景类特效_2089349057071378433.json, 视频生成/图生视频/加速版图生视频｜MiniMaxH3人物特效快速出片_2093142943912783874.json, 视频生成/图生视频/动作迁移图生视频｜Minimax视频动作迁移工作流_2087218060968161281.json, 视频生成/图生视频/单人数字人直播｜MiniMax H3图生视频驱动口播_2089027921309691906.json, 视频生成/图生视频/单人版数字人直播｜MiniMax H3图生视频口播生成_2088700833398607873.json, 视频生成/图生视频/单人音频驱动数字人（最高15秒）MiniMax-H3_2087437541388673025.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速版 MiniMax H3开源人物类特效方案_2093215341110452226.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速｜MiniMax H3开源人物特效图生视频_2089726628791406594.json, 视频生成/图生视频/数字人音频驱动图片跳舞｜MiniMax H3开源人物类特效加速版_2091293535025844225.json, 视频生成/图生视频/自定义背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2089320676988637185.json, 视频生成/图生视频/自定义背景人物参考｜MiniMax H3动作迁移图生视频_2093084247081963522.json, 视频生成/图生视频/音频驱动&图片跳舞｜MiniMax H3开源加速版生成_2095081150728462338.json, 视频生成/图生视频/音频驱动图片跳舞加速版开源｜MiniMax H3人物类特效角色设计图生视频_2088105811947114497.json, 视频生成/图生视频/音频驱动图片跳舞数字人｜MiniMax H3开源人物特效加速版_2093758821327007745.json, 视频生成/图生视频/音频驱动图片跳舞｜MiniMax H3开源加速，人物类特效一步到位_2099894171938152449.json, 视频生成/文生视频/minimaxH3数字人唱歌｜音频驱动口播视频生成_2095236856601468930.json, 视频生成/文生视频/minimaxH3数字人音频驱动｜音频生成口播视频工作流_2094870008924041217.json, 视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频音频参考_2085178835024306178.json, 视频生成/文生视频/数字人唱歌视频生成｜minimaxH3文生视频一键直出_2095506914233905153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json、视频生成/图生视频/全能参考图生视频美少女｜miniMAXH3视频生成工作流_2088145573164707841.json、视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2089305534913667073.json、视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2090649252212076545.json、视频生成/图生视频/全能参考生视频｜MiniMax H3自定义背景人物迁移_2090938897554567170.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 23/24 个有
- `PrimitiveFloat` —— 23/24 个有
- `SaveVideo` —— 23/24 个有
- `孤海注释` —— 23/24 个有
- `ComfyMathExpression` —— 22/24 个有
- `ResolutionSelector` —— 22/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 21/24 个有
- `LoadAudio` —— 19/24 个有
- `VAEDecodeAudio` —— 18/24 个有
- `GetNode` —— 17/24 个有
- `PathchSageAttentionKJ` —— 17/24 个有
- `SetNode` —— 17/24 个有
- `PrimitiveStringMultiline` —— 16/24 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 13/24 个有
- `LayerUtility: PurgeVRAM V2` —— 8/24 个有
- `PainterVRAM` —— 7/24 个有
- `VHS_LoadVideo` —— 7/24 个有
- `VRAM_Debug` —— 7/24 个有
- `AudioCrop` —— 6/24 个有
- `CR Prompt Text` —— 6/24 个有
- `SoundFlow_GetLength` —— 6/24 个有
- `Fast Groups Bypasser (rgthree)` —— 5/24 个有
- `ModelPreviewOverrideKJ` —— 3/24 个有
- `PrimitiveInt` —— 2/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/24 个有
- `Load Lora` —— 1/24 个有
- `MathExpression|pysssss` —— 1/24 个有
- `VHS_VideoCombine` —— 1/24 个有
- `easy cleanGpuUsed` —— 1/24 个有
- `easy mathInt` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高发问题（27/24 个样本）：Steps较低可能导致细节不足
