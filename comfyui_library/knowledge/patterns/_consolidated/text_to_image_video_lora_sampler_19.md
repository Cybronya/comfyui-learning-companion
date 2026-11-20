---
name: text_to_image_video_lora_sampler_19
type: Text To Image
frequency: 26
level: strong
coverage: 0.543346
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AITUDOU H3 Skill2.0全能参考版｜单采直出视频_2098755113656610818.json, 视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json, 视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json, 视频生成/图生视频/AITUDOU MiniMax H3短剧公司版｜短剧批量制作团队方案_2113558862644203521.json, 视频生成/图生视频/AI影视剧制作MiniMaxH3多参视频生成发布版 多模态输入_2109729477717741570.json, 视频生成/图生视频/Fused-MiniMax H3战斗增强双采｜图生视频火力全开_2097934793827766274.json, 视频生成/图生视频/H3最强二采吊打SelfLift虚空折叠流工作流，人物类特效图生视频方案_2107910096905920513.json, 视频生成/图生视频/H3最强二采唐僧彩蛋工作流，人物类特效场景类特效图生视频方案_2108293181078073346.json, 视频生成/图生视频/H3最强二采音画俱佳工作流，人物类特效战斗特效图生视频方案_2108346316232417282.json, 视频生成/图生视频/H3最强二采飓风京剧工作流，人物类特效场景类特效图生视频方案_2108289982774464514.json, 视频生成/图生视频/H3电影LORA巅峰双采去油PRO版视频生成处理工具_2101017420696739841.json, 视频生成/图生视频/H3电影感视频生成 每一帧电影级画面质感_2099578194558017538.json, 视频生成/图生视频/H3电影感视频生成 每帧电影级画面质感 高品质输出_2099579950520160258.json, 视频生成/图生视频/H3虚空折叠流最强二采 视频动态超越SelfLift_2110355960790343681.json, 视频生成/图生视频/H3超强工作流图生视频高质量视频生成方案 动态生成优化_2108717274050940929.json, 视频生成/图生视频/H3超强工作流，图生视频高质量视频生成方案_2107999971776749569.json, 视频生成/图生视频/MiniMax H3 Turbo V4｜Realism真人写实参考生视频｜超写实图生视频流_2108004956178567169.json, 视频生成/图生视频/MiniMax H3 多参考生视频 720p｜一采快二采质量高支持特效_2096841455523422209.json, 视频生成/图生视频/MiniMax H3动作迁移2.0史诗强化进阶版，视频生视频动态姿势迁移工具_2103188261547102209.json, 视频生成/图生视频/MiniMax H3动作迁移9分钟出视频，图生视频视频生视频高效产出方案_2103599685733801986.json, 视频生成/图生视频/MiniMax H3动作迁移9分钟出视频，图生视频视频生视频高效产出方案_2103930965801398273.json, 视频生成/图生视频/MiniMax H3多参生视频 图生视频多模态参考创作_2099194857146376194.json, 视频生成/图生视频/MiniMax H3多参考生视频 快速高质量图生视频_2098830853072834562.json, 视频生成/图生视频/MiniMax H3多参考生视频快速高质量版｜图生视频速度画质兼得_2099143441149157378.json, 视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json, 视频生成/图生视频/双采样潜空间放大DSW｜MiniMax H3二次优化生成_2095951614468251650.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/AITUDOU H3 Skill2.0全能参考版｜单采直出视频_2098755113656610818.json、视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json、视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json、视频生成/图生视频/AITUDOU MiniMax H3短剧公司版｜短剧批量制作团队方案_2113558862644203521.json、视频生成/图生视频/AI影视剧制作MiniMaxH3多参视频生成发布版 多模态输入_2109729477717741570.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 26 个 workflow 都包含：
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
- `ResolutionSelector`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 25/26 个有
- `RandomNoise` —— 25/26 个有
- `SamplerCustomAdvanced` —— 25/26 个有
- `SplitSigmas` —— 24/26 个有
- `Text` —— 24/26 个有
- `MinimaxH3LatentUpscaler3D` —— 22/26 个有
- `LTXVSeparateAVLatent` —— 20/26 个有
- `LoadAudio` —— 20/26 个有
- `LTXVConcatAVLatent` —— 19/26 个有
- `SaveImage` —— 19/26 个有
- `VHS_LoadVideo` —— 19/26 个有
- `PrimitiveFloat` —— 18/26 个有
- `easy float` —— 17/26 个有
- `Float` —— 7/26 个有
- `Fast Groups Bypasser (rgthree)` —— 6/26 个有
- `H3SigmaRefiner` —— 3/26 个有
- `ModelAttentionBackend` —— 3/26 个有
- `PT_H3ConcatAVLatent` —— 3/26 个有
- `AudioSeparation` —— 2/26 个有
- `CR Prompt Text` —— 2/26 个有
- `ConditioningZeroOut` —— 2/26 个有
- `JWFloat` —— 2/26 个有
- `MiniMaxH3AVLatentSeparateT8` —— 2/26 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/26 个有
- `SelfLiftH3Sampler` —— 2/26 个有
- `SolAttnMiniMax` —— 2/26 个有
- `VHS_LoadAudioUpload` —— 2/26 个有
- `VRAM_Debug` —— 2/26 个有
- `LoraLoaderBypassModelOnly` —— 1/26 个有
- `MiniMaxChunkFeedForward` —— 1/26 个有
- `MiniMaxH3VoiceLibraryLoadT8` —— 1/26 个有
- `MiniMaxLowVRAMAttention` —— 1/26 个有
- `PreviewImage` —— 1/26 个有
- `easy cleanGpuUsed` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 26 | 100% |
| 高度 | 80 | 80 - 80 | 26 | 100% |
| 采样步数 | 4 | 4 - 4 | 26 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 26 | 100% |
| 采样算法 | er_sde | - | 26 | 100% |
| 调度器 | beta | - | 26 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，26 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，26 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，26 个样本，一致性 100%
- 调度器 最常用 beta，26 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 高发问题（29/26 个样本）：Steps较低可能导致细节不足
