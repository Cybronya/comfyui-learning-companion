---
name: text_to_image_lora_sampler_clip_18
type: Text To Image
frequency: 26
level: strong
coverage: 0.797808
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json, 视频生成/图生视频/二关键帧视频生成｜MiniMaxH3 KeyFarmes X2工作流_2095116824059928577.json, 视频生成/图生视频/全能参考图生视频美少女｜miniMAXH3视频生成工作流_2088145573164707841.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2089305534913667073.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2090649252212076545.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3自定义背景人物迁移_2090938897554567170.json, 视频生成/图生视频/全能多参生视频自用版｜Minimax H3 人物场景类特效_2089349057071378433.json, 视频生成/图生视频/加速版图生视频｜MiniMaxH3人物特效快速出片_2093142943912783874.json, 视频生成/图生视频/四关键帧视频生成｜MiniMaxH3 KeyFarmes X4工作流_2095078270608953346.json, 视频生成/图生视频/图片跳舞｜MiniMax H3开源加速版，音频驱动角色表演_2099882356789301249.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速版 MiniMax H3开源人物类特效方案_2093215341110452226.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速｜MiniMax H3开源人物特效图生视频_2089726628791406594.json, 视频生成/图生视频/数字人音频驱动图片跳舞｜MiniMax H3开源人物类特效加速版_2091293535025844225.json, 视频生成/图生视频/自定义背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2089320676988637185.json, 视频生成/图生视频/自定义背景人物参考｜MiniMax H3动作迁移图生视频_2093084247081963522.json, 视频生成/图生视频/角色一致动作迁移人物替换｜H3智能反推提示词图生视频_2092363921817686017.json, 视频生成/图生视频/角色一致动作迁移｜MiniMax H3人物替换智能反推方案_2093472951667609602.json, 视频生成/图生视频/角色一致动作迁移｜Minimax H3人物替换智能反推图生视频_2089457405968076801.json, 视频生成/图生视频/角色一致动作迁移｜Minimax H3人物替换智能反推图生视频_2091250634946334721.json, 视频生成/图生视频/角色一致动作迁移｜Minimax H3智能反推人物替换_2090884451969622017.json, 视频生成/图生视频/音频驱动&图片跳舞｜MiniMax H3开源加速版生成_2095081150728462338.json, 视频生成/图生视频/音频驱动图片跳舞加速版开源｜MiniMax H3人物类特效角色设计图生视频_2088105811947114497.json, 视频生成/图生视频/音频驱动图片跳舞数字人｜MiniMax H3开源人物特效加速版_2093758821327007745.json, 视频生成/图生视频/音频驱动图片跳舞｜MiniMax H3开源加速，人物类特效一步到位_2099894171938152449.json, 视频生成/视频生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2106531233084821505.json, 视频生成/视频生视频/智能反推提示词免手写 Minimax H3角色一致性人物替换图生视频方案_2106158187798941698.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json、视频生成/图生视频/二关键帧视频生成｜MiniMaxH3 KeyFarmes X2工作流_2095116824059928577.json、视频生成/图生视频/全能参考图生视频美少女｜miniMAXH3视频生成工作流_2088145573164707841.json、视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2089305534913667073.json、视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2090649252212076545.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 26 个 workflow 都包含：
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
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 25/26 个有
- `PrimitiveFloat` —— 25/26 个有
- `孤海注释` —— 25/26 个有
- `ResolutionSelector` —— 24/26 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 22/26 个有
- `GetNode` —— 21/26 个有
- `SetNode` —— 21/26 个有
- `LoadAudio` —— 13/26 个有
- `PrimitiveStringMultiline` —— 13/26 个有
- `Fast Groups Bypasser (rgthree)` —— 12/26 个有
- `VHS_LoadVideo` —— 12/26 个有
- `PathchSageAttentionKJ` —— 11/26 个有
- `PrimitiveInt` —— 9/26 个有
- `LayerUtility: PurgeVRAM V2` —— 8/26 个有
- `PainterVRAM` —— 8/26 个有
- `VRAM_Debug` —— 8/26 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 8/26 个有
- `EasyCache` —— 7/26 个有
- `RHHiddenNodes` —— 7/26 个有
- `easy showAnything` —— 7/26 个有
- `CR Prompt Text` —— 5/26 个有
- `easy cleanGpuUsed` —— 3/26 个有
- `MiniMaxH3AddGuide` —— 2/26 个有
- `ModelAttentionBackend` —— 2/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/26 个有
- `Load Lora` —— 1/26 个有
- `easy mathInt` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 26 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 26 | 100% |
| 采样算法 | er_sde | - | 26 | 100% |
| 调度器 | beta | - | 26 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| 宽度 | 80 | 80 - 80 | 26 | 100% |
| 高度 | 80 | 80 - 80 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 34/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，26 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，26 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，26 个样本，一致性 100%
- 调度器 最常用 beta，26 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 高发问题（34/26 个样本）：Steps较低可能导致细节不足
