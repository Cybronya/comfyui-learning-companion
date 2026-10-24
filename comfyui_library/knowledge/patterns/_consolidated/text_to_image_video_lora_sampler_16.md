---
name: text_to_image_video_lora_sampler_16
type: Text To Image
frequency: 28
level: strong
coverage: 0.735786
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解_2090069695356563458.json, 视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜_2091171813098344450.json, 视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜图生视频_2091249300000034818.json, 视频生成/图生视频/15秒卡点混剪｜MinimaxH3像素幻想Lab转场特效_2090885714388013057.json, 视频生成/图生视频/H3多图数字人最新优化版 多图参考数字人视频生成_2099199642356510721.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版 高质量图生视频工具_2099190175938207745.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版｜多图参考更听话，画面更贴需求_2099467720621387777.json, 视频生成/图生视频/MiniMax H3多参考生视频工作流，图生视频多素材融合方案_2103581304431407106.json, 视频生成/图生视频/MiniMax H3多参考生视频快速高质量版｜图生视频速度画质兼得_2099143441149157378.json, 视频生成/图生视频/MiniMax H3多图参考数字人唱歌精准对话 数字人口播方案_2109353184165715970.json, 视频生成/图生视频/MiniMax H3开源数字人唱歌说唱口播虚拟主播电商产品讲解自动版工作流_2107966601273372673.json, 视频生成/图生视频/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解角色设计_2090077928905330689.json, 视频生成/图生视频/MiniMax-H3开源数字人｜唱歌口播虚拟主播全自动版_2107672106023608321.json, 视频生成/图生视频/MiniMax-H3开源数字人｜唱歌说唱口播虚拟主播电商讲解_2095217698312642562.json, 视频生成/图生视频/MiniMaxH3多图数字人优化新版｜多图驱动更稳，口播视频更自然_2099508624107335682.json, 视频生成/图生视频/MiniMaxH3多图数字人最新优化版｜图生视频驱动口播人物更自然_2101848347656146946.json, 视频生成/图生视频/口播说唱唱歌电商讲解｜MiniMax H3自动数字人_2091192351791341570.json, 视频生成/图生视频/开源数字人自动版｜MiniMax-H3唱歌说唱口播讲解_2093766167809843202.json, 视频生成/图生视频/开源数字人｜MiniMax H3唱歌说唱口播全能，虚拟主播自动生成_2099920276535463937.json, 视频生成/图生视频/数字人唱歌说唱口播｜MiniMax-H3开源虚拟主播电商讲解自动版_2095554696181272577.json, 视频生成/图生视频/数字人唱歌说唱口播｜MiniMax-H3开源虚拟主播讲解_2093436709731127298.json, 视频生成/图生视频/数字人自动版｜MiniMax-H3唱歌说唱口播虚拟主播产品讲解_2089792313785675777.json, 视频生成/图生视频/虚拟主播电商产品讲解｜MiniMax-H3开源数字人唱歌说唱自动版_2095556325643210753.json, 视频生成/文生视频/H3 8步武术动作控制 视频生成处理工具_2100656957408501761.json, 视频生成/文生视频/Minimax h3 多参考双采打斗｜武打动作影视级生成工作流_2096854645028253697.json, 视频生成/文生视频/多参考双采打斗工作流｜Minimax h3文生视频战斗生成_2096666047398105090.json, 视频生成/文生视频/武打动作真实流畅｜MiniMax H3格斗生视频专用_2096560442037596161.json, 视频生成/文生视频/武打动作视频生成｜MiniMax H3战斗特效工作流_2096312632931340290.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解_2090069695356563458.json、视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜_2091171813098344450.json、视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜图生视频_2091249300000034818.json、视频生成/图生视频/15秒卡点混剪｜MinimaxH3像素幻想Lab转场特效_2090885714388013057.json、视频生成/图生视频/H3多图数字人最新优化版 多图参考数字人视频生成_2099199642356510721.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 28 个 workflow 都包含：
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 26/28 个有
- `LoadAudio` —— 25/28 个有
- `ComfyMathExpression` —— 24/28 个有
- `PrimitiveFloat` —— 24/28 个有
- `llama_cpp_instruct_adv` —— 22/28 个有
- `llama_cpp_model_loader` —— 22/28 个有
- `llama_cpp_parameters` —— 22/28 个有
- `AudioCrop` —— 21/28 个有
- `GetNode` —— 21/28 个有
- `SetNode` —— 21/28 个有
- `ModelAttentionBackend` —— 19/28 个有
- `Audio Duration (mtb)` —— 16/28 个有
- `AudioSeparation` —— 16/28 个有
- `MathExpression|pysssss` —— 16/28 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 16/28 个有
- `SaveText` —— 12/28 个有
- `VAEDecodeAudio` —— 12/28 个有
- `Fast Groups Bypasser (rgthree)` —— 9/28 个有
- `LTXVConcatAVLatent` —— 9/28 个有
- `LTXVSeparateAVLatent` —— 9/28 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/28 个有
- `MinimaxH3LatentUpscaler3D` —— 9/28 个有
- `VHS_LoadVideo` —— 9/28 个有
- `H3SigmaRefiner` —— 8/28 个有
- `easy float` —— 8/28 个有
- `SaveImage` —— 6/28 个有
- `SplitSigmas` —— 6/28 个有
- `LayerUtility: PurgeVRAM` —— 5/28 个有
- `LoraLoader` —— 5/28 个有
- `PathchSageAttentionKJ` —— 5/28 个有
- `PrimitiveInt` —— 5/28 个有
- `Text Concatenate` —— 5/28 个有
- `easy positive` —— 5/28 个有
- `Text` —— 4/28 个有
- `MiniMaxLowVRAMAttention` —— 3/28 个有
- `AILab_QwenVL_PromptEnhancer` —— 2/28 个有
- `ConditioningZeroOut` —— 2/28 个有
- `CreateVideo` —— 2/28 个有
- `EasyCache` —— 2/28 个有
- `LayerUtility: PurgeVRAM V2` —— 2/28 个有
- `ModelPreviewOverrideKJ` —— 2/28 个有
- `RIFE VFI` —— 2/28 个有
- `RTXVideoSuperResolution` —— 2/28 个有
- `SaveVideo` —— 2/28 个有
- `MuyeTextEditOutput` —— 1/28 个有
- `PreviewAny` —— 1/28 个有
- `easy cleanGpuUsed` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 28 | 100% |
| 高度 | 80 | 80 - 80 | 28 | 100% |
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 28 | 100% |
| 采样算法 | er_sde | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |
| LoRA 模型强度 | 0.4 | 0.3 - 0.5 | 5 | 82% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，观测区间 0.3 - 0.5，5 个样本，取值集中（一致性 82%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（29/28 个样本）：Steps较低可能导致细节不足
