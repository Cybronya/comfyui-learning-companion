---
name: text_to_image_lora_sampler_clip_17
type: Text To Image
frequency: 25
level: strong
coverage: 0.84952
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json, 视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json, 视频生成/图生视频/MiniMax H3全能参考三图版｜三图输入视频生成_2094516324448948226.json, 视频生成/图生视频/MiniMax H3全能参考双图版｜双图输入视频生成_2094519227574218754.json, 视频生成/图生视频/MiniMax H3全能参考四图版｜多图输入视频生成_2094508021375397889.json, 视频生成/图生视频/MiniMax H3全能参考工作流｜图生视频万能底座_2105278066246373377.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2095811312990375938.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2100008105735184386.json, 视频生成/图生视频/MiniMax H3参考生视频 官方全能多模态创作工具_2098824046145269762.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频 加速版电商内容制作_2098699036625821698.json, 视频生成/图生视频/MiniMax H3多图参考｜图生视频多图生成_2090449654759645186.json, 视频生成/图生视频/MiniMax H3开源加速版，音频驱动图片跳舞人物特效_2110843023394435074.json, 视频生成/图生视频/MiniMax H3开源加速版｜音频驱动图片跳舞人物特效出片_2110731793975570434.json, 视频生成/图生视频/MiniMax H3开源图片跳舞加速｜音频驱动角色设计图生视频_2110734968224837633.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版人物特效_2094874446220840962.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版角色表演_2094881447520858113.json, 视频生成/图生视频/MiniMax多参考生成视频R2V图生视频处理工具_2102478493312442370.json, 视频生成/图生视频/图片跳舞｜MiniMax H3开源加速版，音频驱动角色表演_2099882356789301249.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速版 MiniMax H3开源人物类特效方案_2093215341110452226.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速｜MiniMax H3开源人物特效图生视频_2089726628791406594.json, 视频生成/图生视频/数字人音频驱动图片跳舞｜MiniMax H3开源人物类特效加速版_2091293535025844225.json, 视频生成/图生视频/音频驱动&图片跳舞｜MiniMax H3开源加速版生成_2095081150728462338.json, 视频生成/图生视频/音频驱动图片跳舞加速版开源｜MiniMax H3人物类特效角色设计图生视频_2088105811947114497.json, 视频生成/图生视频/音频驱动图片跳舞数字人｜MiniMax H3开源人物特效加速版_2093758821327007745.json, 视频生成/图生视频/音频驱动图片跳舞｜MiniMax H3开源加速，人物类特效一步到位_2099894171938152449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json、视频生成/图生视频/MiniMax H3九图参考生音视频｜高质量加速电商版_2095579312127827970.json、视频生成/图生视频/MiniMax H3全能参考三图版｜三图输入视频生成_2094516324448948226.json、视频生成/图生视频/MiniMax H3全能参考双图版｜双图输入视频生成_2094519227574218754.json、视频生成/图生视频/MiniMax H3全能参考四图版｜多图输入视频生成_2094508021375397889.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 24/25 个有
- `KSamplerSelect` —— 24/25 个有
- `MiniMaxH3ReferenceToVideo` —— 24/25 个有
- `VAEDecodeAudio` —— 24/25 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 21/25 个有
- `PrimitiveStringMultiline` —— 21/25 个有
- `LoadAudio` —— 20/25 个有
- `GetNode` —— 16/25 个有
- `SetNode` —— 16/25 个有
- `PathchSageAttentionKJ` —— 15/25 个有
- `LayerUtility: PurgeVRAM V2` —— 13/25 个有
- `PainterVRAM` —— 13/25 个有
- `VRAM_Debug` —— 13/25 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 13/25 个有
- `ComfySwitchNode` —— 6/25 个有
- `PrimitiveBoolean` —— 6/25 个有
- `PrimitiveInt` —— 6/25 个有
- `CR Prompt Text` —— 4/25 个有
- `SaveImage` —— 4/25 个有
- `VHS_LoadVideo` —— 4/25 个有
- `Fast Groups Bypasser (rgthree)` —— 3/25 个有
- `Fast Bypasser (rgthree)` —— 1/25 个有
- `LoraLoaderBypassModelOnly` —— 1/25 个有
- `MiniMaxH3AVDecodeT8` —— 1/25 个有
- `MiniMaxH3AudioConditioningT8` —— 1/25 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/25 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/25 个有
- `SolAttnMiniMax` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高发问题（27/25 个样本）：Steps较低可能导致细节不足
