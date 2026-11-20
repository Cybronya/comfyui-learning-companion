---
name: text_to_image_video_upscale_latent_upscale
type: Text To Image
frequency: 19
level: strong
coverage: 0.564632
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3 8步武术动作控制 视频生成处理工具_2100656957408501761.json, 视频生成/文生视频/H3动作迁移2.0单图参考版视频生成处理工具包_2100995556775645185.json, 视频生成/文生视频/H3多参考7P3A2V生视频二采优化版工具_2100646011814371329.json, 视频生成/文生视频/H3开源数字人口播带货 多图生视频电商内容制作_2098851175243280386.json, 视频生成/文生视频/H3数字人口播工作流｜人物场景图加音频生成 自然Vlog口播视频_2104049801779306497.json, 视频生成/文生视频/H3最强全能工作流言出法随 视频生成处理工具_2100673673299587074.json, 视频生成/文生视频/H3电影级LORA双采去油PRO版 巅峰画质视频生成_2098288538583392257.json, 视频生成/文生视频/H3虚幻引擎赛璐璃风格漫画流双采FL2高清PRO处理_2100642569272254465.json, 视频生成/文生视频/H3言出法随至尊工作流｜文生图生视频全能生成_2097497018427072514.json, 视频生成/文生视频/MiniMax H3多参考生视频9图片3视频3音频处理工具_2102119756018044929.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版，文生视频视频生视频图生视频方案_2107247870394064897.json, 视频生成/文生视频/MiniMax H3多参考生视频最新优化版 多模态输入方案_2105415601509462017.json, 视频生成/文生视频/MiniMax H3多参考生视频｜最新优化版效果再升级_2105135308315648002.json, 视频生成/文生视频/MiniMax H3多合一极速生视频｜二采优化全能工作流_2097533751998898178.json, 视频生成/文生视频/MiniMax+H3多参考生视频｜9图片3视频3音频任意混搭｜多角色锁定_2101896037253337090.json, 视频生成/文生视频/Minimax h3 多参考双采打斗｜武打动作影视级生成工作流_2096854645028253697.json, 视频生成/文生视频/多参考双采打斗工作流｜Minimax h3文生视频战斗生成_2096666047398105090.json, 视频生成/文生视频/武打动作真实流畅｜MiniMax H3格斗生视频专用_2096560442037596161.json, 视频生成/文生视频/武打动作视频生成｜MiniMax H3战斗特效工作流_2096312632931340290.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/文生视频/H3 8步武术动作控制 视频生成处理工具_2100656957408501761.json、视频生成/文生视频/H3动作迁移2.0单图参考版视频生成处理工具包_2100995556775645185.json、视频生成/文生视频/H3多参考7P3A2V生视频二采优化版工具_2100646011814371329.json、视频生成/文生视频/H3开源数字人口播带货 多图生视频电商内容制作_2098851175243280386.json、视频生成/文生视频/H3数字人口播工作流｜人物场景图加音频生成 自然Vlog口播视频_2104049801779306497.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 19 个 workflow 都包含：
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
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/19 个有
- `PrimitiveFloat` —— 18/19 个有
- `VAEDecodeAudio` —— 18/19 个有
- `LoadAudio` —— 17/19 个有
- `VHS_LoadVideo` —— 16/19 个有
- `SplitSigmas` —— 15/19 个有
- `SaveImage` —— 12/19 个有
- `Text` —— 12/19 个有
- `easy float` —— 11/19 个有
- `Fast Groups Bypasser (rgthree)` —— 6/19 个有
- `AudioCrop` —— 5/19 个有
- `H3SigmaRefiner` —— 5/19 个有
- `LayerUtility: PurgeVRAM` —— 5/19 个有
- `LoraLoader` —— 5/19 个有
- `PathchSageAttentionKJ` —— 5/19 个有
- `PrimitiveInt` —— 5/19 个有
- `ShowText|pysssss` —— 5/19 个有
- `Text Concatenate` —— 5/19 个有
- `easy positive` —— 5/19 个有
- `MiniMaxLowVRAMAttention` —— 3/19 个有
- `AILab_QwenVL_PromptEnhancer` —— 2/19 个有
- `ConditioningZeroOut` —— 2/19 个有
- `CreateVideo` —— 2/19 个有
- `EasyCache` —— 2/19 个有
- `LayerUtility: PurgeVRAM V2` —— 2/19 个有
- `ModelPreviewOverrideKJ` —— 2/19 个有
- `RIFE VFI` —— 2/19 个有
- `RTXVideoSuperResolution` —— 2/19 个有
- `SaveVideo` —— 2/19 个有
- `Float` —— 1/19 个有
- `ManualSigmas` —— 1/19 个有
- `easy cleanGpuUsed` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.3 - 0.5 | 5 | 82% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
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

- LoRA 模型强度 中位数 0.4，观测区间 0.3 - 0.5，5 个样本，取值集中（一致性 82%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
